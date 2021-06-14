#To use this code you need to first install steganography
#You can install it by entering sudo python -m pip install steganography
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

output_path = "secret_image.png"

# read secret text from image
secret_text = Steganography.decode(output_path)

print(secret_text)
