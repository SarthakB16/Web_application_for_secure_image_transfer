
from src.Encrypter import Encrypter
from src.Decrypter import Decrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
import base64
from Crypto.Cipher import AES
import os
import sys
import io


def dec():
    myKey = "1234"
    file  = "./src/encrypted.txt"
    text=open(file).read()
    cipher= text.encode('utf-8')
    x = Decrypter(cipher)
    image=x.decrypt_image(myKey)
    print(type(image))
    imag = Img.open(io.BytesIO(image))
    imag.save('./src/decryptedimage.png')

    