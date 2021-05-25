from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

# url분석
baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusurl = input('검색어 입력 : ')

# quote_plus()을 사용하여 검색어 아스키코드로 변환
# 실제 검색에는 아스키코드
url = baseurl + quote_plus(plusurl)
print(url)

html = urlopen(url)

# bs4이용 분석
soup = bs(html, "html.parser")
img = soup.select('._img')

# print(img[0])

n = 1
for i in img:
    # print(img[0])출력 확인 -> data-source를 가져와야함.
    imgurl = i['data-source']
    with urlopen(imgurl) as f:
        # image : binary file , wb : to write binary file
        with open('./img/' + plusurl + str(n)+'.jpg','wb') as save:
            img = f.read()
            save.write(img)
    n += 1

print('downloaded.')