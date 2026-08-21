from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://www.google.com/search"

token = "sk-proj-1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
headers = {
    "Authorization": f"Bearer {token}",    # openai / finmind 購買 api 後填入 token
    "Content-Type": "application/json",
}

params = {
    "q": "2330"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers , params=params)
response.raise_for_status() #有異常就終止



soup = BeautifulSoup(response.text, "html.parser")  #  html原始碼透過 html.parser分析
pprint(f'網頁內容: {soup.text}')
