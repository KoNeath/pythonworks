import requests

from lxml import etree


request.header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                         'Chrome/51.0.2704.63 Safari/537.36'}

response=requests.get('https://piyao.sina.cn/')

html=etree.HTML(response.content)

date=html.xpath('')