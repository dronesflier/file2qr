# Simple python file-to-QR-code(s) Generator

This is a proof-of-concept, so, just, don't store important files in it :)
Anyway, here's how to use it:
## Usage:
Clone this using ```git clone https://github.com/JuliusS123/file2qr```
Then to encode run (in the dir): ```python3 createqrcode.py``` and just follow the instructions.
To decode run:```python3 decodeqrcode.py``` and follow the instructions.
I want to stress again that this is a proof-of-concept, because if you give it a big file, it *will* fill your entire folder with QR codes!

## How it works:
The file is read, converted to base64 and stored in QR code(s). If the file is over 2.8 kilobytes large, then It will split the base64 code and store it in multiple QR codes.
## Limitations:
One QR code can only store 2.88 KB of data, so big files will fill up your directory pretty quickly.