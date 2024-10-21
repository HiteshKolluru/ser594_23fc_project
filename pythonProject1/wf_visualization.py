import pathlib
import pandas as pd



# this should work fine if it does not replace
# every thing before the name of the csv file with absolute path to foldername => data_original
folder_name = "data_original"
pathToFolder= str(pathlib.Path().resolve()) +"/"+ folder_name + "/"
csvProcessed = 'ArtistwithLyricsProcessed.csv'
songs = pd.read_csv(pathToFolder+csvProcessed)

songs_dict = songs.to_dict('list')

print(songs_dict)



