from selenium import webdriver
import time

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('D:/python/crawling/chromedriver.exe')
# 크롬을 통해 네이버 로그인 화면 접속
driver.get('https://nid.naver.com/nidlogin.login')

time.sleep(1)
driver.find_element_by_name('id').send_keys('or_lln')
time.sleep(1)
driver.find_element_by_name('pw').send_keys('80dkgus14!')

# xpath //*[@id="log.login"]/fieldset/input
driver.find_element_by_xpath('//*[@id="log.login"]').click()

# from bs4 import BeautifulSoup as bs
# driver.get('https://mail.naver.com/')
# html = driver.page_source
# soup = bs(html, "html.parser")
# title_list = soup.find_all('strong','mail_title')
#
# for title in title_list:
#     print(title.get_text())