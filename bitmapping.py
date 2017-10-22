import PIL
from PIL import Image

# create the image to be processed
img = Image.open("max.jpg")
# create a new variable with a bitmap type image
bmimg = img.convert('1')
# show the bitmap version of the image
bmimg.show()
