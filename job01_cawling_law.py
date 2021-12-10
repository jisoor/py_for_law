from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument('lang=ko_KR')
options.add_argument('disable_gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
#{'titles': titles, 'laws': laws, 'dates': dates}


titles = []
laws = []
dates = []
url = 'https://glaw.scourt.go.kr/wsjo/panre/sjo050.do#'
driver.get(url)

search_box = driver.find_element_by_name("srchw")  # 검색어 위치 연결
search_box.send_keys("대법원")  # 검색어 보내기
driver.find_element_by_xpath('//*[@id="search"]/div[2]/fieldset/a[1]').click()  # 검색버튼
time.sleep(0.2)
driver.find_element_by_xpath('//*[@id="search"]/div[2]/fieldset/div/p/a').click()  # 자동완성 창 닫기
time.sleep(0.5)
#driver.find_element_by_xpath('//*[@id="groupList"]/li[5]/ul/li[1]/a').click()
#time.sleep(0.5)
#driver.find_element_by_xpath('//*[@id="tabwrap"]/div/div/div[1]/div[3]/fieldset/ul/li[2]/a/span[1]').click()


next_button_xpath = '//*[@id="tabwrap"]/div/div/div[1]/div[3]/div/fieldset/p/a[1]'  #herf , get-atttribute
next_button_xpath_2 = '//*[@id="tabwrap"]/div/div/div[1]/div[3]/div/fieldset/p/a[2]'
next_button_xpath_3 = '//*[@id="tabwrap"]/div/div/div[1]/div[3]/div/fieldset/p/a[3]'

try:
    for i in range(1,2567): #  2568페이지
        try:
            driver.find_element_by_xpath(next_button_xpath_3).click()
        except:
            driver.find_element_by_xpath(next_button_xpath_2).click()
            try:
                driver.find_element_by_xpath(next_button_xpath).click()
            except:
                print('error0')

        for i in range(0, 20): # 0번ㅇ부터 19번까지 총 20개
            time.sleep(0.5)
            title_xpath = '//*[@id="ln{}"]/td[2]/dl/dt/a[1]/strong/strong'.format(i)
            title = driver.find_element_by_xpath(title_xpath).text
            driver.find_element_by_xpath(title_xpath).click()
            time.sleep(0.5)
            law_xpath = '//*[@id="areaDetail"]/div[2]/div'
            law = driver.find_element_by_xpath(law_xpath).text
            titles.append(title)
            laws.append(law)
except:
    print('error')

#print(titles)
#print(laws)