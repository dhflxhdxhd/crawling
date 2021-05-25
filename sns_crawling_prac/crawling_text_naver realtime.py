# naver realtime crawling
import requests
from bs4 import BeautifulSoup

# 서버에서 bot으로 인지 -> 차단 => USER 설정
# headers = {'User-Agent' : '유저정보'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.48 Safari/537.36'}
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')

i=1
print("\nNaver realtime Data")
for anchor in soup.select("span.item_title"):
    print('%2s위 %s'%(str(i),anchor.get_text()))
    i += 1

