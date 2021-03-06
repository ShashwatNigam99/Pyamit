import os
import webbrowser

import requests
from bs4 import BeautifulSoup


'''
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''
query = input('Enter the title of the video: ')
query = query.replace(' ', '+')

url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url,timeout=10)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]
link = song['href']
webbrowser.open('https://www.youtube.com' + link)