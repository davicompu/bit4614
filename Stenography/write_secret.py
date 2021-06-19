#To use this code you need to first install steganography
#You can install it by entering sudo python -m pip install steganography

from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

# hide text to image
path = "image.png"
output_path = "secret_image.png"
text = 'Here you place your secret message'
Steganography.encode(path, output_path, text)

