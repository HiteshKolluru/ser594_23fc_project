import pathlib
import pickle

from sklearn.linear_model import LinearRegression

path = str(pathlib.Path().resolve())
pathToModelFolder = path + "/" + "models" + "/"

def trainLinearmodel(X_train, y_train):

    model = LinearRegression()
    model.fit(X_train, y_train)

    # save model
    with open(pathToModelFolder + 'linear_regression_model.pkl', 'wb') as file:
        pickle.dump(model, file)


def trainWord2vecRegressionModel(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)

    # save model
    with open(pathToModelFolder + 'linear_regression_Word2Vec_model.pkl', 'wb') as file:
        pickle.dump(model, file)


def trainRegression_happy(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)

    # save model
    with open(pathToModelFolder + 'linear_regression_happy_model.pkl', 'wb') as file:
        pickle.dump(model, file)

def trainRegression_sad(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)

    # save model
    with open(pathToModelFolder + 'linear_regression_sad_model.pkl', 'wb') as file:
        pickle.dump(model, file)