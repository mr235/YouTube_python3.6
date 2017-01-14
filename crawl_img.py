import requests
from bs4 import BeautifulSoup

host = "http://www.ivsky.com"

def trade_spider(max_pages):
    pages = 1
    while pages <= max_pages:
        url = "http://www.ivsky.com/tupian/ziranfengguang/index_" + str(pages) + ".html"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll("div", {"class":"il_img"}):
            atag = link.a
            print(atag.get("title"))
            href = host + atag.get("href")
            get_all_big_img(href)

        pages += 1

def get_all_big_img(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.find_all("div", {"class":"il_img"}):
        href = host + link.a.get("href")
        img = get_big_img(href)
        print(img)


def get_big_img(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    img = soup.find("img", {"id":"imgis"})
    href = img.get("src")
    return href


trade_spider(1)
