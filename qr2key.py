#!/usr/bin/env python3
from PIL import Image
import zbarlight
import glob
import re

count_images = 0
count_qrcodes = 0
count_privkeys = 0

with open('./keylist.txt', 'a') as key_list:
    print('scanning images for QR codes with bitcoin private keys...')
    for image_path in glob.glob('./qrbooty/*.*'):
        with open(image_path, 'rb') as image_file:
            count_images += 1
            image = Image.open(image_file)
            image.load()
            codes = zbarlight.scan_codes('qrcode', image)
            for code in (codes or []):
                code = code.decode('ascii', errors='replace')
                count_qrcodes += 1
                if ((re.match(r'5(H|J|K).{49}$', code) or      # match private key (WIF, uncompressed pubkey) with length 51
                   re.match(r'(K|L).{51}$', code) or           # match private key (WIF, compressed pubkey) with length 52
                   re.match(r'S(.{21}|.{29})$', code)) and     # match mini private key with length 22 (deprecated) or 30
                   re.match(r'[1-9A-HJ-NP-Za-km-z]+', code)):  # match only BASE58
                    count_privkeys += 1
                    key_list.write(code + '\n')
                    print('potential booty found!: %s' % code)
   print('qr2key done. scanned %s images, with %s QR codes containing %s bitcoin private keys' % (count_images, count_qrcodes, count_privkeys))
   print('saved private keys to keylist.txt')
   