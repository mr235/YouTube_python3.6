from urllib import request

# http://finance.yahoo.com/ 从这里找数据
baidu_url = "http://chart.finance.yahoo.com/table.csv?s=BIDU.SW&a=11&b=11&c=2016&d=0&e=11&f=2017&g=d&ignore=.csv"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"baidu.csv"
    fw = open(dest_url, "w")
    for line in lines:
        fw.write(line + "\n")
    fw.close()

download_stock_data(baidu_url)
