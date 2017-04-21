from PIL import Image
from PIL import ImageEnhance,ImageFilter
from rec_image import image_to_string

im = Image.open('7039.jpg')
imgry = im.convert('L')
#imgry.show()


threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
#out.show()

#图片降噪
im2 = Image.open("2hhh.jpg")
#im2.show()
im2 = im2.filter(ImageFilter.MedianFilter())
#im2.show()
enhancer = ImageEnhance.Contrast(im2)
im2 = enhancer.enhance(2)
im2 = im2.convert('1')
im2.show()



#print(image_to_string('7039.jpg', plus='-psm 7'))