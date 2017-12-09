#!/usr/bin/env python
from PIL import Image
import zbarlight
import glob
import re

count_images = 0
count_qrcodes = 0
count_privkeys = 0

with open('./keylist.txt', 'a') as key_list:
   print('scanning PNG images for QR codes with bitcoin private keys...')
   for png_path in glob.glob('./qrbooty/*.png'):
      with open(png_path, 'rb') as png_file:
         count_images += 1
         image = Image.open(png_file)
         image.load()
         codes = zbarlight.scan_codes('qrcode', image)
         for code in (codes or []):
            count_qrcodes += 1
            # TODO: match only BASE58 chars
            if(re.match('5(H|J|K).{49}$', code) or   # match private key (WIF, uncompressed pubkey): length 51, BASE58
               re.match('(K|L).{51}$', code) or      # match private key (WIF, compressed pubkey): length 52, BASE58
               re.match('S(.{21}|.{29})$', code)):   # match mini private key: length 30 or 22 (deprecated), BASE58
               count_privkeys += 1
               key_list.write(code + '\n')
               print('potential booty found!: %s' % code)
   print('qr2key done. scanned %s images, with %s QR codes containing %s bitcoin private keys' % (count_images, count_qrcodes, count_privkeys))
   print('saved private keys to keylist.txt')
