import pyqrcode
import base64
whichfiletoopen = input("Input the path to the file you want to convert:\n")
with open(whichfiletoopen, 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    n = 2800
    chunks = []

    i = 0
    while i < len(base64_message):
        if i+n < len(base64_message):
            chunks.append(base64_message[i:i+n])
        else:
            chunks.append(base64_message[i:len(base64_message)])
        i += n
i = 0
contiune = input("I will make " + str(len(chunks)) + " qr codes. Do you want to continue? y/n\n")
if contiune == "y":
    for _ in range(len(chunks)):
        qr = pyqrcode.create(chunks[i], error="L")
        qr.png("output" + str(i) + ".png", scale=5)
        i = i + 1