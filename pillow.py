from PIL import Image

img = Image.open("dajiuhu-005.jpg")
print(img.size)
print(img.format)   # JPEG
print(img.mode)     # RGB

area = (0, 100, 400, img.height)
cropped_img = img.crop(area)

# img.show()
# cropped_img.show()

# 贴纸
smile_cry = Image.open("smile_cry.jpg")
paste_area = (100, 100, 100 + smile_cry.width, 100 + smile_cry.height)

img.paste(smile_cry, paste_area)

# img.show()

# Getting Individual Channels
r, g, b = img.split()
r.show()
g.show()
b.show()
