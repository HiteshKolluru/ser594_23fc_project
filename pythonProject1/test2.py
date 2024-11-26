import pathlib
import pandas as pd

# Load your dataset of song lyrics

path = str(pathlib.Path().resolve())
folder_name = "data_processed"
pathToFolder = path + "/" + folder_name + "/"
csvProcessed = 'ArtistwithLyricsProcessed.csv'
songs = pd.read_csv(pathToFolder + csvProcessed)
# songs_dict = songs.to_dict('list')

pathToModelFolder = path + "/" + "models" + "/"


songs_dict = songs.to_dict('list')

X = pd.DataFrame({
        'year': songs_dict['year'],
        'negative' : songs_dict['negative'],
        'neutral' : songs_dict['neutral'],
        'positive' : songs_dict['positive'],
        'compound' : songs_dict['compound'],
    })


means_df = X.groupby(['year']).mean()

print(means_df)

