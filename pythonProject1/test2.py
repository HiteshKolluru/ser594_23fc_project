import pathlib
import pickle
import re

import lyricsgenius
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error

from gensim.models import Word2Vec


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

