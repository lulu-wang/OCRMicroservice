#https://pypi.python.org/pypi/tesserocr
from PIL import Image
import tesserocr
def receiptReader(location):
    image = Image.open(location)
    print tesserocr.image_to_text(image)
    return tesserocr.image_to_text(image)
