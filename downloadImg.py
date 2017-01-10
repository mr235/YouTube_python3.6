import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://img.ivsky.com/img/tupian/pic/201512/07/baixueaiai_de_jingse-005.jpg")