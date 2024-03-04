import requests
from bs4 import BeautifulSoup

url = "https://atcoder.jp/contests/abc310/tasks/abc310_b"

# URLからHTMLを取得
response = requests.get(url)
response.raise_for_status()  # 応答がエラーの場合は例外を発生させる

# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')

# '<div class="part">' タグで囲まれた部分を検索
parts = soup.find_all('div', class_='part')

# 抽出したテキストを保存するファイルを開く
with open('scraped_content.txt', 'w', encoding='utf-8') as file:
    for part in parts:
        # テキストをファイルに書き込む
        file.write(part.get_text() + '\n\n')
