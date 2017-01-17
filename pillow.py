from PIL import Image
from PIL import ImageFilter

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

def transposeImg():
    dajiuhu = Image.open("dajiuhu-005.jpg")
    square_img = dajiuhu.resize((300, 300))
    flip_img = dajiuhu.transpose(Image.FLIP_TOP_BOTTOM)
    spin_img = dajiuhu.transpose(Image.ROTATE_90)

    dajiuhu.show()
    square_img.show()
    flip_img.show()
    spin_img.show()

def filterImg():
    dajiuhu = Image.open("dajiuhu-005.jpg")
    black_white = dajiuhu.convert("L")
    blur = dajiuhu.filter(ImageFilter.BLUR)
    detail = dajiuhu.filter(ImageFilter.DETAIL)
    edges = dajiuhu.filter(ImageFilter.FIND_EDGES)

    dajiuhu.show()
    black_white.show()
    blur.show()
    detail.show()
    edges.show()


# imgInfo()
# cropImg()
# pasteImg()
# channelsImg()
# mergeImg()
# transposeImg()
filterImg()