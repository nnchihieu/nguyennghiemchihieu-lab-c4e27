from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content, "html.parser")
sec = soup.find("section", "section chart-grid")
div = sec.find("div", "section-content")
ul = div.find("ul")
li_list = sec.find_all("li")
news_list = []
for li in li_list:
    news = OrderedDict({'song_name':li.h3.string,'artist':li.h4.string})
    news_list.append(news)

pyexcel.save_as(records=news_list, dest_file_name='chart_song.xlsx')

songs = []
for i in news_list:
    song = i["song_name"] + " " + i["artist"]
    songs.append(song)
options = { 
    "default_search" : "ytsearch",
    "max_downloads" : len(songs),
}
dl = YoutubeDL(options)
dl.download(songs)
