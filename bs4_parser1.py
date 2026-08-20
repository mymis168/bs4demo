from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://mymis168.github.io/bs4demo/apple.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.raise_for_status() #有異常就終止
#pprint( response.text)

#將網頁內容交給 bs 分析
soup = BeautifulSoup(response.text, "html.parser")  #  html原始碼透過 html.parser分析

#soup 代表APPLE.HTML 的結構
print(f'網頁的title是{soup.title}')