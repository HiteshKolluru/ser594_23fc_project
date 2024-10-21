import lyricsgenius
import pandas as pd
import pathlib
import csv

#please change this path as required as your path will be different from mine
folder_name = "data_original"


token = "mKu246Cbo3UL41cYIsjLLD3WN7dl5tjyYYQvIIZ5kI028e_3JuzY_jN9HRpvePi7"
genius = lyricsgenius.Genius(token, timeout = 500, remove_section_headers = True, verbose = False, skip_non_songs= True)
# getting a few non songs need to be figured out even after sending skip_non_songs as true

# field_names= ['artist', 'lyrics']
song_dict = {
    # 'Index' : [],
    'artist': [],
    'song_id': [],
    'title': [],
    'url' : [],
    'lyrics': [],
    # 'Lang' : [], can be added to detect language before it is stored
}

# this should work fine if it does not replace
# every thing before the name of the csv file with absolute path to foldername => data_original
billboardFile = "billboard_current_week_100.csv"
pathtobillboard= str(pathlib.Path().resolve()) +"/"+ folder_name + "/" + billboardFile
i = 0
with open(pathtobillboard, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    print(lines)
    song = genius.search_song(lines[0], artist=lines[1])
    if song != None:
        # print(song.lyrics)
        # song_dict['Index'].append(str(i))
        song_dict['artist'].append(song.artist)
        song_dict['title'].append(song.title)
        song_dict['url'].append(song.url)
        song_dict['song_id'].append(song.id)
        song_dict['lyrics'].append(song.lyrics)
        # i+=1


# the following is not giving correct data might need to look into it further
# possibly try this:  Genius,9345566,May 2024 Singles Release Calendar,https://genius.com/Genius-may-2024-singles-release-calendar-annotated,"15 ContributorsMay 2024 Singles Release Calendar Lyrics5/1
# adore - ""did i tell u that i miss u""
page = 1
tags = ['pop', 'rock', 'country']
for tag in tags:
    res = genius.tag(tag)
    for hit in res['hits']:
        # song_lyrics = genius.lyrics(song_url=hit['url'])
        song = genius.search_song(hit['title'])
        if song != None:
            # print(song.lyrics)
            # song_dict['Index'].append(str(i))
            song_dict['artist'].append(song.artist)
            song_dict['title'].append(song.title)
            song_dict['url'].append(song.url)
            song_dict['song_id'].append(song.id)
            song_dict['lyrics'].append(song.lyrics)
            # i+=1

df = pd.DataFrame(song_dict)

# this should work fine if incase this does not work replace
# every thing before the name of the csv file with absolute path to foldername => data_original
# like the below
# pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"

pathToFolder = str(pathlib.Path().resolve()) +"/"+ folder_name + "/"
df.to_csv(pathToFolder+'ArtistwithLyrics.csv',index=False)

