# Everytime timetable subject name

import requests
from bs4 import BeautifulSoup as bs

url = 'https://everytime.kr/timetable'
response = requests.get(url)

soup = bs(response.content, 'html.parser')

print("\nEverytime timetable subject")

