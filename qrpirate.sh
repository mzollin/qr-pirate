#!/bin/bash
# crawling search engines for images matching description
./qrcrawler.py "$1"

# convert all images to PNG
printf "converting images to PNG. this may take a while...\n"
for PATHNAME in ./qrbooty/google/*; do FILENAME=$(basename "$PATHNAME"); mv "$PATHNAME" "./qrbooty/google_$FILENAME"; done
for PATHNAME in ./qrbooty/bing/*; do FILENAME=$(basename "$PATHNAME"); mv "$PATHNAME" "./qrbooty/bing_$FILENAME"; done
for PATHNAME in ./qrbooty/baidu/*; do FILENAME=$(basename "$PATHNAME"); mv "$PATHNAME" "./qrbooty/baidu_$FILENAME"; done
mogrify -format png ./qrbooty/*.*
printf "converting done.\n\n"

# read private keys from QR codes in images
./qr2key.py

# remove duplicates
sort keylist.txt | uniq > keylist_unique.txt
