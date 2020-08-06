from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

# url분석
baseurl = 'https://www.instagram.com/'
plusurl = input('검색어 입력 : ')

# quote_plus()을 사용하여 검색어 아스키코드로 변환
# 실제 검색에는 아스키코드
url = baseurl + quote_plus(plusurl) + "/"
print(url)

html = urlopen(url)

# bs4이용 분석
soup = bs(html, "html.parser")
img = soup.find_all(class_='FFVAD')

print(img[0])

