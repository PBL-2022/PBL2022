#Webスクレイピングし指定した内容をファイルに出力するコード

# BeautifulSoupをインポート
import requests
import datetime
from bs4 import BeautifulSoup

#URLを指定
url = "https://www.sendai-nct.ac.jp/sclife/kyuko/ku_hirose/"

# ページのHTMLを取得
html = requests.get(url)

# BeautifulSoupで解析
soup = BeautifulSoup(html.text, 'html.parser')

contents = soup.find('table' ,cellpadding="0") #table cellpadding="0"から/tableまで

out = contents.get_text() #テキスト取得

dt_now = datetime.datetime.now() #今日の日付と現在時刻のデータを取得

f = open('main.txt', 'a') #ファイルを開く

#ファイルの中に出力
f.writelines(out)
f.write('更新日時:' + str(dt_now))

f.close() #ファイルを開く