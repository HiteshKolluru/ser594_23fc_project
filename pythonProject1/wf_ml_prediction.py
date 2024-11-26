import pathlib
import pickle
import re
import string

import joblib
import pandas as pd
from nltk import WordNetLemmatizer, RegexpTokenizer, word_tokenize
from nltk.corpus import cmudict, stopwords
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error

path = str(pathlib.Path().resolve())
pathToModelFolder = path + "/" + "models" + "/"

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
    lemmatizer = WordNetLemmatizer()
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    processed_words = ' '.join(word for word in processed_tokens)

    return processed_words, word_count, unique_words_count

d = cmudict.dict()
def syllable_count(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    except KeyError:
        # If word not in CMU dictionary, estimate based on vowels
        return len(re.findall(r'[aeiouy]+', word.lower()))


def calculate_density_metrics(lyrics):
    # Split lyrics into lines and words
    lines = lyrics.strip().split('\n')
    words = word_tokenize(lyrics)

    # Total words (rename to match training)
    word_count = len(words)

    # Unique words (rename to match training)
    word_count_unique = len(set(words))

    # Total syllables (simplified using vowels)
    syllables = sum(len(re.findall(r'[aeiouyAEIOUY]', word)) for word in words)

    # Number of lines
    num_lines = len(lines)

    # Calculate densities
    unique_word_density = word_count_unique / word_count if word_count > 0 else 0
    syllable_density = syllables / word_count if word_count > 0 else 0
    line_density = word_count / num_lines if num_lines > 0 else 0

    # Return metrics with matching names
    return {
        'word_count': word_count,
        'word_count_unique': word_count_unique,
        'unique_words': word_count_unique,
        'syllables': syllables,
        'lines': num_lines,
        'unique_word_density': unique_word_density,
        'syllable_density': syllable_density,
        'line_density': line_density
    }

def linear_model_pred(X_test, y_test):
    # loading basic linearRegression model
    with open(pathToModelFolder + 'linear_regression_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)
    y_pred = model_basic.predict(X_test)

    # Convert predictions to binary labels: happy (1), sad (0)
    threshold = 0.5  # You can adjust the threshold based on the dataset
    y_pred_labels = [1 if score >= threshold else 0 for score in y_pred]

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred_labels)
    precision = precision_score(y_test, y_pred_labels)
    recall = recall_score(y_test, y_pred_labels)
    f1 = f1_score(y_test, y_pred_labels)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")

def regression_model_pred(song_lyric, sentiment, lyric):
    with open(pathToModelFolder + 'linear_regression_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)

    pred = 1 if model_basic.predict(song_lyric) >= 0.5 else 0
    print("Predicted: " + str(pred))
    print("labeled: "+ str(sentiment))
    print(lyric)


def word2vec_pred(X_test, y_test):
    # loading Word2Vec linearRegression model
    with open(pathToModelFolder + 'linear_regression_Word2Vec_model.pkl', 'rb') as file:
        model_word2vec = pickle.load(file)

    y_pred = model_word2vec.predict(X_test)

    # Convert predictions to binary labels: happy (1), sad (0)
    threshold = 0.5  # You can adjust the threshold based on the dataset
    y_pred_labels = [1 if score >= threshold else 0 for score in y_pred]

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred_labels)
    precision = precision_score(y_test, y_pred_labels)
    recall = recall_score(y_test, y_pred_labels)
    f1 = f1_score(y_test, y_pred_labels)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")

def word2vec_regression_model_pred(song_lyric, sentiment, lyric):
    with open(pathToModelFolder + 'linear_regression_Word2Vec_model.pkl', 'rb') as file:
        model_word2vec = pickle.load(file)


    pred = 1 if model_word2vec.predict(song_lyric) >= 0.5 else 0
    print("Predicted: " + str(pred))
    print("labeled: "+ str(sentiment))
    print(lyric)

def sad_pred(X_test, y_test):
    # loading Word2Vec linearRegression model
    with open(pathToModelFolder + 'linear_regression_sad_model.pkl', 'rb') as file:
        model_word2vec = pickle.load(file)

    y_pred = model_word2vec.predict(X_test)

    # Convert predictions to binary labels: happy (1), sad (0)
    threshold = 0.5  # You can adjust the threshold based on the dataset
    y_pred_labels = [1 if score >= threshold else 0 for score in y_pred]

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred_labels)
    precision = precision_score(y_test, y_pred_labels)
    recall = recall_score(y_test, y_pred_labels)
    f1 = f1_score(y_test, y_pred_labels)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")

def regression_model_sad_pred(song_lyric, sad, lyric):
    with open(pathToModelFolder + 'linear_regression_sad_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)

    pred = 1 if model_basic.predict(song_lyric) >= 0.5 else 0
    print("Predicted: " + str(pred))
    print("labeled: "+ str(sad))
    print(lyric)

def regression_model_sad_pred_ret(song_lyric):
    with open(pathToModelFolder + 'linear_regression_sad_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)

    return  model_basic.predict(song_lyric)

def happy_pred(X_test, y_test):
    # loading Word2Vec linearRegression model
    with open(pathToModelFolder + 'linear_regression_happy_model.pkl', 'rb') as file:
        model_word2vec = pickle.load(file)

    y_pred = model_word2vec.predict(X_test)

    # Convert predictions to binary labels: happy (1), sad (0)
    threshold = 0.5  # You can adjust the threshold based on the dataset
    y_pred_labels = [1 if score >= threshold else 0 for score in y_pred]

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred_labels)
    precision = precision_score(y_test, y_pred_labels)
    recall = recall_score(y_test, y_pred_labels)
    f1 = f1_score(y_test, y_pred_labels)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")

def regression_model_happy_pred(song_lyric, happy, lyric):
    with open(pathToModelFolder + 'linear_regression_happy_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)

    pred = 1 if model_basic.predict(song_lyric) >= 0.5 else 0
    print("Predicted: " + str(pred))
    print("labeled: "+ str(happy))
    print(lyric)

def regression_model_happy_pred_ret(song_lyric):
    with open(pathToModelFolder + 'linear_regression_happy_model.pkl', 'rb') as file:
        model_basic = pickle.load(file)

    return  model_basic.predict(song_lyric)

def kmeans_clustering_experiment(song_lyric):
    cluster_names = {
        0: "Complex and Poetic",
        1: "Simple and Catchy",
        2: "Balanced and Moderate"
    }

    # will need both mode and scaler to get accurate results
    pathToModelFolder = path + "/" + "models" + "/"
    loaded_kmeans = joblib.load(pathToModelFolder+'kmeans_model.pkl')
    loaded_scaler = joblib.load(pathToModelFolder+'kmeans_scaler.pkl')
    print("Model and scaler loaded!")
    new_song_lyrics = []
    new_song_lyrics.append(song_lyric)
    # Extract features for new lyrics
    new_features = [calculate_density_metrics(lyric) for lyric in new_song_lyrics]
    new_features_df = pd.DataFrame(new_features)

    # Prepare features for clustering (with correct names)
    X_new = new_features_df[['word_count', 'word_count_unique','unique_words', 'syllables', 'lines',
                             'unique_word_density', 'syllable_density', 'line_density']]

    # Standardize using the same scaler
    X_new_scaled = loaded_scaler.transform(X_new)

    # Predict the cluster using the loaded model
    new_song_clusters = loaded_kmeans.predict(X_new_scaled)

    # Output the predicted cluster for each new song
    for i, cluster in enumerate(new_song_clusters):
        cluster_name = cluster_names.get(cluster, f"Cluster {cluster}")
        print(f"New Song {i + 1} is assigned to: {cluster_name}")
