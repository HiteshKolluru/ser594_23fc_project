import pathlib
import pickle

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error

path = str(pathlib.Path().resolve())
pathToModelFolder = path + "/" + "models" + "/"

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