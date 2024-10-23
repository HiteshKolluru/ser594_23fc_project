import string
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download(["stopwords","vader_lexicon","punkt","wordnet"])
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import pathlib

def preprocess_text(text):
    # Tokenise words & ignore punctuation
    text = text.split("Lyrics")[1] # removes the first part of the content before lyrics start
    text = text.split("Embed")[0] # removes the last part that is not part of the lyrics

    #unsure if I can remove all numbers as in some context it could be vital
    text = ''.join([i for i in text if not i.isdigit()])
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    # print(text)

    tokeniser = RegexpTokenizer(r'\w+')
    tokens = tokeniser.tokenize(text)
    stop_words = set(stopwords.words('english'))

    data_token = [token.lower() for token in tokens]
    processed_words = [word for word in data_token if not word in stop_words]
    # when accessing this in visualization it is coming up as a list will look into this.
    processed_words = ' '.join(word for word in processed_words)

    return processed_words

# need to work on
# def isItEnglish(text):
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#     text_vocab = set(w.lower() for w in text if w.lower().isalpha())
#     unusual = text_vocab.difference(english_vocab)
#
#     return unusual

def maindata():
    # this should work fine if it does not replace
    # every thing before the name of the csv file with absolute path to foldername => data_original
    folder_name = "data_original"
    csvOG = "ArtistwithLyrics.csv"
    pathToFolder = str(pathlib.Path().resolve()) + "/" + folder_name + "/" + csvOG
    songs = pd.read_csv(pathToFolder)

    songs_dict = songs.to_dict('list')
    # print(songs_dict)
    lyrics = []
    Laguage = []
    song_sent = []
    sid = SentimentIntensityAnalyzer()
    for song in songs_dict['lyrics']:
        # will be skipping languages other than english
        # this part needs work as it is tough to identify if the lyric is entirely in english
        # or it just has parts of english

        # to be implemented.
        # Laguage.append('English' if len(isItEnglish(song)) > 0 else 'Not English')

        text = preprocess_text(song)
        song_sent.append(sid.polarity_scores(text))
        lyrics.append(text)

    # songs_dict.update({'Lagnuage': Laguage})
    songs_dict.update({'Lyrics_Processed': lyrics})
    songs_dict.update({'Sentiment of lyrics': song_sent})

    df = pd.DataFrame(songs_dict)

    # this should work fine if incase this does not work replace
    # every thing before the name of the csv file with absolute path to foldername => data_original
    # like the below
    # pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"

    pathToFolder2 = str(pathlib.Path().resolve()) + "/" + folder_name + "/"
    csvProcessed = 'ArtistwithLyricsProcessed.csv'
    df.to_csv(pathToFolder2 + csvProcessed, index=False)

if __name__ == "__main__":
    maindata()