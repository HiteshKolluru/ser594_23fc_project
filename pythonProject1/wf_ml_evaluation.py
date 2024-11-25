import pathlib
import random
import re

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from nltk import WordNetLemmatizer, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from gensim.models import Word2Vec

import wf_ml_prediction
import wf_ml_training
import lyricsgenius


token = "mKu246Cbo3UL41cYIsjLLD3WN7dl5tjyYYQvIIZ5kI028e_3JuzY_jN9HRpvePi7"
genius = lyricsgenius.Genius(token, timeout = 500, remove_section_headers = True, verbose = False, skip_non_songs= True)


def preprocess_lyrics(lyrics):
    # Remove special characters and numbers
    lyrics = re.sub(r'[^a-zA-Z\s]', '', lyrics)
    # Tokenize and lowercase
    tokens = word_tokenize(lyrics.lower())
    # Remove stopwords and lemmatize
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return ' '.join(processed_tokens)  # Convert to lowercase and split into words


def compute_sentence_embedding(tokens, word2vec_model):
    vectors = [word2vec_model.wv[word] for word in tokens if word in word2vec_model.wv]
    if len(vectors) > 0:
        return np.mean(vectors, axis=0)  # Average the word vectors
    else:
        return np.zeros(word2vec_model.vector_size)  # Fallback for empty lyrics

def compute_average_embedding(text, word2vec_model):
    words = text.split()  # Tokenize the lyrics
    embeddings = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        return np.zeros(word2vec_model.vector_size)


if __name__ == "__main__":
    # Load your dataset of song lyrics
    path = str(pathlib.Path().resolve())
    folder_name = "data_processed"
    pathToFolder = path + "/" + folder_name + "/"
    csvProcessed = 'ArtistwithLyricsProcessed.csv'
    songs = pd.read_csv(pathToFolder + csvProcessed)

    pathToModelFolder = path + "/" + "models" + "/"

    # Basic Linear Regression
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(songs['Lyrics_Processed']).toarray()
    y = songs['Sentiment of lyrics']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=34)

    wf_ml_training.trainLinearmodel(X_train, y_train)
    wf_ml_prediction.linear_model_pred(X_test, y_test)

    # songlyric = vectorizer.fit_transform(random.sample(songs['Lyrics_Processed'], 1)).toarray()
    test_song = random.sample(songs['Lyrics_Processed'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_pred(vectorizer.transform(test_song).toarray(), songs['Sentiment of lyrics'][idx], test_song)

    test_song = random.sample(songs['Lyrics_Processed'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_pred(vectorizer.transform(test_song).toarray(), songs['Sentiment of lyrics'][idx], test_song)

    # Linear Regression with Word2Vec
    print()
    print()
    songs['tokenized_lyrics'] = songs['Lyrics_Processed'].fillna('').apply(preprocess_lyrics)

    w2v_model = Word2Vec(sentences=songs['tokenized_lyrics'], vector_size=100, window=4, min_count=2, workers=4)
    # Save the Word2Vec model for reuse
    # w2v_model.save(pathToModelFolder + "word2vec_model")
    # w2v_model = Word2Vec.load(pathToModelFolder+"word2vec_model")

    # Compute embeddings for each song
    songs['embedding'] = songs['tokenized_lyrics'].apply(lambda x: compute_sentence_embedding(x, w2v_model))

    # Convert embeddings to a 2D array for model input
    X = np.vstack(songs['embedding'].values)
    y = songs['Sentiment of lyrics']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

    wf_ml_training.trainWord2vecRegressionModel(X_train, y_train)
    wf_ml_prediction.word2vec_pred(X_test, y_test)

    test_song = str(random.sample(songs['Lyrics_Processed'].to_list(), 1))
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    embedding_lyric = compute_average_embedding(test_song, w2v_model)
    wf_ml_prediction.word2vec_regression_model_pred(embedding_lyric.reshape(1, -1), songs['Sentiment of lyrics'][idx], test_song)

    test_song = str(random.sample(songs['Lyrics_Processed'].to_list(), 1))
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    embedding_lyric = compute_average_embedding(test_song, w2v_model)
    wf_ml_prediction.word2vec_regression_model_pred(embedding_lyric.reshape(1, -1),songs['Sentiment of lyrics'][idx], test_song)


    # Preprocess all lyrics in the dataset
    songs['processed_lyrics'] = songs['lyrics'].apply(preprocess_lyrics)

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(songs['processed_lyrics']).toarray()
    y = songs['sadness']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=34)

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    wf_ml_training.trainRegression_sad(X_train_resampled, y_train_resampled)
    wf_ml_prediction.sad_pred(X_test, y_test)

    # songlyric = vectorizer.fit_transform(random.sample(songs['Lyrics_Processed'], 1)).toarray()
    test_song = random.sample(songs['Lyrics_Processed'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_sad_pred(vectorizer.transform(test_song).toarray(), songs['sadness'][idx], test_song)

    test_song = random.sample(songs['processed_lyrics'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_sad_pred(vectorizer.transform(test_song).toarray(), songs['sadness'][idx], test_song)

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(songs['processed_lyrics']).toarray()
    y = songs['happy']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=34)
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    wf_ml_training.trainRegression_happy(X_train_resampled, y_train_resampled)
    wf_ml_prediction.happy_pred(X_test, y_test)

    # songlyric = vectorizer.fit_transform(random.sample(songs['Lyrics_Processed'], 1)).toarray()
    test_song = random.sample(songs['processed_lyrics'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_happy_pred(vectorizer.transform(test_song).toarray(), songs['happy'][idx], test_song)

    test_song = random.sample(songs['processed_lyrics'].to_list(), 1)
    idx = songs.isin(['test_song']).any(axis=1).idxmax()
    wf_ml_prediction.regression_model_happy_pred(vectorizer.transform(test_song).toarray(), songs['happy'][idx], test_song)


    # Example usage of prediction function
    while True:
        title = input("Enter song title (or 'quit' to exit): ").strip()

        if title.lower() == 'quit':
            print("Thank you for using the song theme analyzer. Goodbye!")
            break

        artist = input("Enter artist name: ").strip()

        song = genius.search_song(title=title, artist=artist)
        if len(song.lyrics) == 0 or song.lyrics == None:
            print(f"Sorry, couldn't find the song '{title}' by {artist}. Please try again.")
            continue

        processed = preprocess_lyrics(song.lyrics)
        listprocessed = []
        listprocessed.append(processed)

        sadnessfact = wf_ml_prediction.regression_model_sad_pred_ret(vectorizer.transform(listprocessed).toarray())
        happinessfact = wf_ml_prediction.regression_model_happy_pred_ret(vectorizer.transform(listprocessed).toarray())
        print("Sad")
        print(sadnessfact)
        print("Happy")
        print(happinessfact)
        if(sadnessfact > happinessfact):
            print("Song is sad")
        else:
            print("Song is happy")

