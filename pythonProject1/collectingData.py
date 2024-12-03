import re
import time
import lyricsgenius
import pandas as pd
import pathlib
import csv
import langid

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
    'year': [],
}


def compare_strings(str1, str2):
    # Remove all non-alphanumeric characters (including spaces)
    cleaned_str1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
    cleaned_str2 = re.sub(r'[^a-zA-Z0-9]', '', str2)

    # Compare the cleaned strings
    return cleaned_str1.lower() == cleaned_str2.lower()

# this should work fine if it does not replace
# every thing before the name of the csv file with absolute path to foldername => data_original
billboardFile = "billboard_current_week_100.csv"
pitchforkfile = "pitchfork.csv"
pathtobillboard= str(pathlib.Path().resolve()) +"/"+ folder_name + "/" + billboardFile
pathtopitchfork= str(pathlib.Path().resolve()) + "/"+ folder_name + "/" + pitchforkfile
i = 0
with open(pathtopitchfork, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    print(lines)
    time.sleep(2)
    song = genius.search_song(title=lines[0], artist=lines[1])
    if song is not None:
        # not working correctly
        # if  langid.classify(song.lyrics) == 'en': # dose not include if Lyrics are not in english
            if not (lines[1].lower() in song.artist.lower() or song.artist.lower() in lines[
                1].lower()) and not compare_strings(song.artist, lines[1]):
                # if not compare_strings(song.artist, lines[1]) and not compare_strings(song.title, lines[0]):
                print("Getting incorrect lyrics...")
                print(song.title, song.artist)
                print(lines[0], lines[1], lines[2])
                print("Getting incorrect lyrics...")
            else:
                # print(song.lyrics)
                # song_dict['Index'].append(str(i))
                song_dict['artist'].append(song.artist)
                song_dict['title'].append(song.title)
                song_dict['url'].append(song.url)
                song_dict['song_id'].append(song.id)
                song_dict['lyrics'].append(song.lyrics)
                song_dict['year'].append(lines[2])
                # i+=1
        # else:
        #     print("song not in english")
    else:
        print("song not found")


# the following is not giving correct data might need to look into it further
# possibly try this:  Genius,9345566,May 2024 Singles Release Calendar,https://genius.com/Genius-may-2024-singles-release-calendar-annotated,"15 ContributorsMay 2024 Singles Release Calendar Lyrics5/1
# adore - ""did i tell u that i miss u""


# Data here is too bad to use needs to be addressed before usable
# page = 1
# tags = ['pop', 'rock', 'country']
# for tag in tags:
#     res = genius.tag(tag)
#     for hit in res['hits']:
#         # song_lyrics = genius.lyrics(song_url=hit['url'])
#         song = genius.search_song(hit['title'])
#         if song != None:
#             # print(song.lyrics)
#             # song_dict['Index'].append(str(i))
#             song_dict['artist'].append(song.artist)
#             song_dict['title'].append(song.title)
#             song_dict['url'].append(song.url)
#             song_dict['song_id'].append(song.id)
#             song_dict['lyrics'].append(song.lyrics)
#             # i+=1

df = pd.DataFrame(song_dict)

# this should work fine if incase this does not work replace
# every thing before the name of the csv file with absolute path to foldername => data_original
# like the below
# pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"

pathToFolder = str(pathlib.Path().resolve()) +"/"+ folder_name + "/"
df.to_csv(pathToFolder+'ArtistwithLyrics.csv',index=False)

