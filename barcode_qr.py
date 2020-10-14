# 1D Barcode
# https://pypi.org/project/python-barcode/
import barcode
from barcode.writer import ImageWriter
EAN = barcode.get_barcode_class('ean13')
#ean = EAN('5901234123457')
ean = EAN('5901234123457', writer=ImageWriter())
ean.save('ean_bar')

# https://pypi.org/project/qrcode/
import qrcode
img = qrcode.make('Some Data here! https://pypi.org/project/python-barcode/')
img.save('img.png')

# https://pypi.org/project/pyzbar/
from pyzbar.pyzbar import decode 
from PIL import Image

d = decode(Image.open('ean_bar.png'))
print(d)
print(d[0].data.decode("utf-8"))

d = decode(Image.open('img.png'))
print(d)
print(d[0].data.decode("utf-8"))

