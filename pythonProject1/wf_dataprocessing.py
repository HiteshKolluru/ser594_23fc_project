import string
import pandas as pd
import nltk
nltk.download(["stopwords","vader_lexicon","punkt","wordnet"])
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import pathlib


# this should work fine if it does not replace
# every thing before the name of the csv file with absolute path to foldername => data_original
folder_name = "data_original"
csvOG = "ArtistwithLyrics.csv"
pathToFolder= str(pathlib.Path().resolve())+"/"+ folder_name + "/" + csvOG
songs = pd.read_csv(pathToFolder)

songs_dict = songs.to_dict('list')
# print(songs_dict)
nltk.download('punkt_tab')

def preprocess_text(text):
    # Tokenise words & ignore punctuation

    text = text.split("Lyrics")[1]
    text = text.split("Embed")[0]
    #unsure if I can remove all numbers as in some context it could be vital
    text = ''.join([i for i in text if not i.isdigit()])
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    print(text)

    tokeniser = RegexpTokenizer(r'\w+')
    tokens = tokeniser.tokenize(text)
    stop_words = set(stopwords.words('english'))

    data_token = [token.lower() for token in tokens]
    processed_words = [w for w in data_token if not w in stop_words]
    return processed_words


def isItEnglish(text):
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    text_vocab = set(w.lower() for w in text if w.lower().isalpha())
    unusual = text_vocab.difference(english_vocab)

    return unusual

lyrics = []
Laguage = []
for song in songs_dict['lyrics']:
    # will be skipping languages other than english
    # this part needs work as it is tough to identify if the lyric is entirely in english
    # or it just has parts of english

    whatlag = 'english' if len(isItEnglish(song)) > 0 else 'Not English'
    Laguage.append(whatlag)
    lyrics.append(preprocess_text(song))


songs_dict.update({'Lagnuage' : Laguage})
songs_dict.update({'Lyrics_Processed' : lyrics})
# print(songs_dict)
for procced in songs_dict['Lyrics_Processed']:
    print(procced)

df = pd.DataFrame(songs_dict)

# this should work fine if incase this does not work replace
# every thing before the name of the csv file with absolute path to foldername => data_original
# like the below
# pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"

pathToFolder2= str(pathlib.Path().resolve()) +"/"+ folder_name + "/"
csvProcessed = 'ArtistwithLyricsProcessed.csv'
df.to_csv(pathToFolder2+csvProcessed,index=False)

