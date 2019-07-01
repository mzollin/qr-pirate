# qr-pirate
<p>
  <img alt="qr-pirate logo"src="qrpirate.png" align="left" width="150" height="150">
  <b>crawl QR-codes from search engines and look for Bitcoin wallet private keys</b><br>
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/qr-pirate"><img alt="Updates" src="https://pyup.io/repos/github/mzollin/qr-pirate/shield.svg"></a>
  <a href="https://pyup.io/repos/github/mzollin/qr-pirate"><img alt="Python3" src="https://pyup.io/repos/github/mzollin/qr-pirate/python-3-shield.svg"></a><br><br>
  <b>Disclaimer: You probably won't find any private keys of wallets that still contain Bitcoins. If you do, please leave them where they are, this tool is for demonstration purposes only. Also don't put photos of your private keys on the internet.</b>
<p><br>

## Setup and usage:
- sudo apt install python3-dev python3-setuptools python3-pip libzbar0 libzbar-dev
- pip3 install -r requirements.txt

**example usage:** ./qrpirate.sh "bitcoin qr"<br>
**output:** keylist_unique.txt
<br>
The balance of the wallet associated with each found private key will be output on the terminal.

## Details
You can use the qrpirate.sh bash script to automate the whole process from search keyword input to private key output, or use the qrcrawler.py and qr2key.py tools on their own. <b>The bash script automates the following steps:</b>

1. Calls qrcrawler.py with the provided search keywords as an argument to crawl google, bing and baidu for images. They will be downloaded to a qrbooty folder with subfolders for every search engine.

2. Renames and moves the files up from the subfolders to the qrbooty folder with unique names.

3. Calls qr2key.py to scan the downloaded images in the qrbooty folder for QR-codes and checks if they contain Bitcoin wallet private keys. The keys will be saved in a keylist.txt file.

4. Removes duplicates in keylist.txt and outputs the unique keys to a keylist_unique.txt file

## Python dependencies:
- icrawler
- pillow
- zbarlight
- pycoin
