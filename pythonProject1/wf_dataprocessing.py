import random
import string
from operator import truediv

import langid
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download(["stopwords","vader_lexicon","punkt","wordnet"])
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import pathlib

from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0



def preprocess_text(text):
    # Tokenise words & ignore punctuation
    text = text.split("Lyrics")[1] # removes the first part of the content before lyrics start
    text = text.split("Embed")[0] # removes the last part that is not part of the lyrics
    text = text.strip()
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
    word_count = len(processed_words)
    unique_words_count = len(set(processed_words))
    processed_words = ' '.join(word for word in processed_words)

    return processed_words, word_count, unique_words_count


def detect_languages(text):
    # langid detection
    langid_lang, _ = langid.classify(text)

    # langdetect detection
    try:
        langdetect_lang = detect(text)
    except:
        langdetect_lang = "unknown"

    if langid_lang == langdetect_lang:
        return langid_lang
    else:
        return

def findlang(song):

    song = song.split("Lyrics")[1] # removes the first part of the content before lyrics start
    song = song.split("Embed")[0] # removes the last part that is not part of the lyrics
    lines = song.split("\n\n")
    sublanguages = set()
    for line in lines:
        sublanguages.add(detect_languages(line))  # Add sublanguage code

    my_list = [item for item in sublanguages if item is not None]

    if(my_list == []):
        my_list.append(detect(song))

    return my_list


def find_love(text):
    love_song_words = [
        "love", "heart", "forever", "baby", "kiss", "darling", "desire",
        "romance", "passion", "dream", "soulmate", "sweetheart", "honey",
        "angel", "beautiful", "need", "miss", "adore", "affection",
        "devotion", "embrace", "longing", "crush", "bliss", "cuddle",
        "cherish", "tender", "beloved", "amour", "yearn", "together",
        "always", "promise", "eternal", "destiny", "faithful", "true",
        "aching", "comfort", "joy", "heaven", "caress", "flutter",
        "treasure", "spark", "magic", "warmth", "bond", "connection"
    ]

    love_count = 0
    for word in text.split(' '):
        if word in love_song_words:
            love_count += 1
    if love_count > 0:
        return 1
    else:
        return 0

def find_sadness(text):
    sad_song_words = [
        "sad", "tears", "cry", "broken", "pain", "heartache", "lonely",
        "goodbye", "lost", "hurt", "grief", "empty", "alone", "blue",
        "sorrow", "regret", "miss", "farewell", "cold", "dark", "mourning",
        "gone", "goodnight", "aching", "bitter", "longing", "shadow",
        "melancholy", "goodbye", "sorry", "lost", "memories", "silent",
        "goodnight", "falling", "gone", "anguish", "bleeding", "fade",
        "distance", "gray", "weep", "darkness", "fragile", "despair",
        "brokenhearted", "shattered", "emptiness", "aching", "wistful",
        "farewell", "tragedy"
    ]

    sad_count = 0
    for word in text.split(' '):
        if word in sad_song_words:
            sad_count += 1
    if sad_count > 0:
        return 1
    else:
        return 0


def find_happy(text):
    happy_words = [
        "joy", "love", "smile", "sunshine", "bliss", "laugh", "cheerful", "happy",
        "celebrate", "laughter", "dance", "shine", "hope", "dream", "light", "good vibes",
        "fun", "excited", "joyful", "free", "party", "positive", "grateful", "carefree",
        "sweet", "radiant", "peace", "content", "delight", "heartfelt", "beautiful",
        "bright", "wonderful", "grinning", "alive", "together", "best", "amazing"
    ]

    happy_count = 0
    for word in text.split(' '):
        if word in happy_words:
            happy_count += 1
    if happy_count > 0:
        return 1
    else:
        return 0

def find_anger(text):
    angry_defiant_words = [
        "rage", "burn", "war", "battle", "revenge", "rebel",
        "scream", "anger", "destroy", "riot", "defiance",
        "fury", "enemy", "resist", "violence", "unleash",
        "dominance", "vengeance", "wrath", "raw", "wreck",
        "unyielding", "ferocity", "torment"
    ]

    anger_count = 0
    for word in text.split(' '):
        if word in angry_defiant_words:
            anger_count += 1
    return anger_count

def find_foul_lang(text):
    explicit_words = [
        "fuck", "shit", "damn", "bitch", "ass", "motherfucker",
        "hell", "piss", "bastard", "dick", "pussy", "cunt",
        "crap", "slut", "whore", "nigga", "hoe", "freak",
        "balls", "cock", "suck", "jerk", "prick", "hella",
        "goddamn", "arse", "faggot", "freaking"
    ]

    foul_lang_count = 0
    for word in text.split(' '):
        if word in explicit_words:
            foul_lang_count += 1

    return foul_lang_count


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
    song_sent = []
    # song_sent_all = []
    sid = SentimentIntensityAnalyzer()
    languages = []
    song_word_count = []
    song_word_count_unique = []
    love_counter = []
    sadness_counter = []
    happy_counter = []
    anger_counter = []
    foul_lang_counter = []
    lyrical_density = []
    song_sent2 = []
    negative = []
    neutral = []
    positive = []
    compound = []
    for song in songs_dict['lyrics']:

        temp = str()
        for lan in findlang(song):
            temp = temp + " " + lan
        languages.append(temp)

        text, word_count, unique_word_count = preprocess_text(song)
        song_word_count.append(word_count)
        song_word_count_unique.append(unique_word_count)
        lyrical_density.append(unique_word_count/word_count*100)
        temp_sent = sid.polarity_scores(text)
        if temp_sent['compound'] >= 0.05:
            song_sent2.append('positive')
            song_sent.append(1)
        elif temp_sent['compound'] <= -0.05:
            song_sent2.append('negative')
            song_sent.append(0)
        else:
            song_sent2.append('neutral')
            if temp_sent['pos'] >= temp_sent['neg']:
                song_sent.append(1)
            else:
                song_sent.append(0)

        negative.append(temp_sent['neg'])
        neutral.append(temp_sent['neu'])
        positive.append(temp_sent['pos'])
        compound.append(temp_sent['compound'])

        happy_counter.append(find_happy(text))
        love_counter.append(find_love(text))
        sadness_counter.append(find_sadness(text))
        anger_counter.append(find_anger(text))
        foul_lang_counter.append(find_foul_lang(text))

        lyrics.append(text)

    songs_dict.update({'Lyrics_Processed': lyrics})
    songs_dict.update({'Sentiment of lyrics': song_sent})
    songs_dict.update({'compound_sentiment': song_sent2})
    songs_dict.update({'negative': negative})
    songs_dict.update({'neutral': neutral})
    songs_dict.update({'positive': positive})
    songs_dict.update({'compound': compound})

    songs_dict.update({'Languages': languages})
    songs_dict.update({'word_count': song_word_count})
    songs_dict.update({'word_count_unique': song_word_count_unique})
    songs_dict.update({'lyrical_density': lyrical_density})

    songs_dict.update({'happy': love_counter})
    songs_dict.update({'love': love_counter})
    songs_dict.update({'sadness': sadness_counter})
    songs_dict.update({'anger': anger_counter})
    songs_dict.update({'foul': foul_lang_counter})


    shuffled_data = list(zip(*songs_dict.values()))
    random.shuffle(shuffled_data)

    # Unzip the shuffled data back into the dictionary
    shuffled_data_dict = {key: list(value) for key, value in zip(songs_dict.keys(), zip(*shuffled_data))}

    df = pd.DataFrame(shuffled_data_dict)

    # this should work fine if incase this does not work replace
    # every thing before the name of the csv file with absolute path to foldername => data_original
    # like the below
    # pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/"

    processed_folder_name = "data_processed"
    pathToFolder2 = str(pathlib.Path().resolve()) + "/" + processed_folder_name + "/"
    csvProcessed = 'ArtistwithLyricsProcessed.csv'
    df.to_csv(pathToFolder2 + csvProcessed, index=False)

if __name__ == "__main__":
    maindata()