from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('qr.jpg'))
print(f" The Decoded data is {decocdeQR[0].data.decode('ascii')}")