# Use Beautifulsoup & Selenium
# 단점 : 속도가 느리다.

# Selenium은 주로 웹앱을 테스트하는데 이용하는 프레임워크
# webdriver라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를 제어

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
# Selenium은 실제 웹 브라우저가 동작하기 때문에 JS로 렌더링이 완료된 후의 DOM결과물에 접근이 가능
from selenium import webdriver
import time


baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색어 입력 : ')
url = baseurl + quote_plus(plusurl)

# print(url)

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('D:/python/crawling/chromedriver.exe')

driver.get(url)

# time.sleep(3)
html = driver.page_source
soup = bs(html,"html.parser")
insta = soup.select('.v1Nh3.kIKUG._bz0w')

# print(insta[0])

n = 1
for i in insta:
    # img_source = i.a['href']
    # img_source_url = 'https://www.instagram.com/' + img_source
    # print(imgurl)

    imgurl = i.select_one('.KL4Bh').img['src']

    with urlopen(imgurl) as f:
        # image : binary file , wb : to write binary file
        with open('./img/' + plusurl + str(n) + '.jpg', 'wb') as save:
            img = f.read()
            save.write(img)

    n += 1

driver.close()
print('downloaded.')

