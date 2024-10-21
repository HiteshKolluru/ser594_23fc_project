from datetime import datetime

import lyricsgenius
import pandas as pd
from lyricsgenius import Genius

import os

folder_name = "data_original"
pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"


token = "mKu246Cbo3UL41cYIsjLLD3WN7dl5tjyYYQvIIZ5kI028e_3JuzY_jN9HRpvePi7"
genius = lyricsgenius.Genius(token, timeout = 500, remove_section_headers = True, verbose = False)

import csv
# field_names= ['artist', 'lyrics']
song_dict = {
    'artist': [],
    'song_id': [],
    'title': [],
    'url' : [],
    'lyrics': [],
}

with open('billboard_hot_100.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    print(lines)
    song = genius.search_song(lines[0], artist=lines[1])
    if song != None:
        # print(song.lyrics)
        song_dict['artist'].append(song.artist)
        song_dict['title'].append(song.title)
        song_dict['url'].append(song.url)
        song_dict['song_id'].append(song.id)
        song_dict['lyrics'].append(song.lyrics)


page = 1
tags = ['pop', 'rock', 'country']
for tag in tags:
    res = genius.tag(tag)
    for hit in res['hits']:
        # song_lyrics = genius.lyrics(song_url=hit['url'])
        song = genius.search_song(hit['title'])
        if song != None:
            # print(song.lyrics)
            song_dict['artist'].append(song.artist)
            song_dict['title'].append(song.title)
            song_dict['url'].append(song.url)
            song_dict['song_id'].append(song.id)
            song_dict['lyrics'].append(song.lyrics)


df = pd.DataFrame(song_dict)
df.to_csv(pathToFolder+'ArtistwithLyrics.csv')
