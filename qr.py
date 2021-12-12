import qrcode
from PIL import Image

#use the QRCode class: The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). 
#Set to None and use the fit parameter when making the code to determine this automatically.
#fill_color and back_color can change the background and the painting color of the QR, when using the default image factory. Both parameters accept RGB color tuples.

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.thefoodlibrary.co.ke/mercado/mercado-drinks-menu/')
qr.make(fit=True)
#img = qr.make_image(fill_color="black", back_color="violet").convert('RGB')
img = qr.make_image(back_color=( 255, 201, 23), fill_color=(64, 84, 178))

img.save("sample2.png") 