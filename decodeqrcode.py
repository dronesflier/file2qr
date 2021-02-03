import base64
from pyzbar.pyzbar import decode
from PIL import Image
howmanyfiles = input("How many qr codes are there?")
x = 0
ad = 0
for i in range(int(howmanyfiles)):
    base64_img = ""
    img = Image.open("output" + str(x) + ".png")
    print("Opening QR code " + str(x))
    result = decode(img)
    for i in result:
        base64_img = base64_img + (i.data.decode("utf-8"))
    base64_img_bytes = base64_img.encode('utf-8')
    if ad == 0:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        ad = 1
    else:
        decoded_image_data = decoded_image_data + base64.decodebytes(base64_img_bytes) # I know this is a really dumb way to do this, but i am also dumb and I can't think of another way :(

    x = x + 1



filename = input("What do you want to name the output file?")
with open(filename, 'wb') as file_to_save:
    
    file_to_save.write(decoded_image_data)