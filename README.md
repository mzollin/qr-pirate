# qr-pirate
crawl QR-codes from search engines and look for bitcoin private keys

**Disclaimer: You probably won't find any private keys of wallets that still contain Bitcoins. If you do, please leave them where they are, this tool is for demonstration purposes only.**

You can use the qrpirate.sh bash script to automate the whole process from search keyword input to private key output, or use the qrcrawler.py and qr2key.py tools on their own. The bash script automates the following steps:

1. Call qrcrawler.py with the provided search keywords as an argument to crawl google, bing and baidu for images. They will be downloaded to a qrbooty folder with subfolders for every search engine.

2. Rename and move the files up from the subfolders to the qrbooty folder and convert them all to PNG format using mogrify.

3. Call qr2key.py to scan the downloaded images in the qrbooty folder for QR-codes and check if they contain Bitcoin private keys. The keys will be saved in a keylist.txt file.

4. Remove duplicates in keylist.txt and output them to a keylist_unique.txt file

**usage: ./qrpirate.sh "bitcoin qr"**<br>
**output: keylist_unique.txt**

Python dependencies:
- icrawler
- pillow
- zbarlight
