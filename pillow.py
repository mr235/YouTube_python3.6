from PIL import Image

def imgInfo():

    img = Image.open("dajiuhu-005.jpg")
    print(img.size)
    print(img.format)   # JPEG
    print(img.mode)     # RGB

def cropImg():
    img = Image.open("dajiuhu-005.jpg")

    area = (0, 100, 400, img.height)
    cropped_img = img.crop(area)

    img.show()
    cropped_img.show()

def pasteImg():
    img = Image.open("dajiuhu-005.jpg")


    # 贴纸
    smile_cry = Image.open("smile_cry.jpg")
    paste_area = (100, 100, 100 + smile_cry.width, 100 + smile_cry.height)

    img.paste(smile_cry, paste_area)

    img.show()

def channelsImg():
    img = Image.open("dajiuhu-005.jpg")

    # Getting Individual Channels
    r, g, b = img.split()
    r.show()
    g.show()
    b.show()

def mergeImg():
    dajiuhu = Image.open("dajiuhu-005.jpg")
    luoye = Image.open("luoye-008.jpg")

    r1, g1, b1 = dajiuhu.split()
    r2, g2, b2 = luoye.split()

    new_img = Image.merge("RGB", (r1, g1, b2))
    new_img.show()


# imgInfo()
# cropImg()
# pasteImg()
# channelsImg()
mergeImg()