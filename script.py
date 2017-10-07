from PIL import Image
import tesserocr
def receiptReader(location):
    image = Image.open(location)
    return tesserocr.image_to_text(image) 
