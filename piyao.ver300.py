from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree


chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get("https://piyao.sina.cn/")
time.sleep(0.5)

for i in range(0,10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(1) 


html = driver.find_elements_by_xpath('//div[@class="zy_day"]')
for a in html:
    b=a.find_elements_by_xpath('/div[@class="day_date"]/following-sibling::ul//div[@class="left_title"]')
    for c in b:
        print(c.text)


