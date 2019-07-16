from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree


chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://piyao.sina.cn/")
time.sleep(1)

for i in range(0,30):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(2) 


html = driver.find_elements_by_xpath("//div[@class='left_title']")
fire=driver.find_elements_by_xpath("//div[@class='comment_text']")
title=[]
com=[]
for a in html:
    title.append(a.text)
for b in fire:
    com.append(int(b.text))
item=zip(title,com)
high=sorted(item,key=lambda x:x[1])
print("本季最热门:\t")
for a in high[-1:-11:-1]:
    print(a[0],'\t','\t',"评论数:",a[1],'\n')
    


