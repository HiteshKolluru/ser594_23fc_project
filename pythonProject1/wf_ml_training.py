import pathlib
import pickle
import joblib
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import StandardScaler

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

def trainKmean(songs):

    X = songs[['word_count', 'word_count_unique', 'unique_words', 'syllables', 'lines',
               'unique_word_density', 'syllable_density', 'line_density']]
    y = songs['lyrical_density']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using the Elbow Method
    inertia = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    # # Plot the Elbow Curve
    # plt.figure(figsize=(8, 5))
    # plt.plot(k_range, inertia, marker='o')
    # plt.title("Elbow Method for Optimal K")
    # plt.xlabel("Number of Clusters (k)")
    # plt.ylabel("Inertia")
    # plt.show()

    # Choose k (e.g., 3) based on the Elbow Curve
    kmeans = KMeans(n_clusters=3, random_state=42)
    songs['cluster'] = kmeans.fit_predict(X_scaled)

    # Visualize clusters (2D projection using PCA for simplicity)
    from sklearn.decomposition import PCA

    silhouette_avg = silhouette_score(X, songs['cluster'])
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Inertia: {kmeans.inertia_}")

    davies_bouldin = davies_bouldin_score(X, songs['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin}")

    # PCA1 -> Overall Complexity related to unique_word_density, syllable_density, and total_words
    # PCA2 -> Structural Simplicity related to line_density and lines
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    songs['pca1'] = X_pca[:, 0]
    songs['pca2'] = X_pca[:, 1]

    # plt.figure(figsize=(10, 7))
    # sns.scatterplot(x='pca1', y='pca2', hue='cluster', data=songs, palette='Set2', s=100)
    # plt.title("Clusters of Songs Based on Lyrical Features")
    # plt.xlabel("Overall Complexity")
    # plt.ylabel("Structural Simplicity")
    # plt.legend(title="Cluster")
    # plt.show()

    # Display the clustered DataFrame
    print(songs)

    # will need both else would lead to inaccurate results
    pathToModelFolder = path + "/" + "models" + "/"
    joblib.dump(kmeans, pathToModelFolder + 'kmeans_model.pkl')
    joblib.dump(scaler, pathToModelFolder + 'kmeans_scaler.pkl')
    print("Model and scaler saved!")

def changedKmeans(songs):
    X = songs[[ 'syllables', 'lines',
               'unique_word_density', 'syllable_density', 'line_density']]
    y = songs['lyrical_density']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using the Elbow Method
    inertia = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    # # Plot the Elbow Curve
    # plt.figure(figsize=(8, 5))
    # plt.plot(k_range, inertia, marker='o')
    # plt.title("Elbow Method for Optimal K")
    # plt.xlabel("Number of Clusters (k)")
    # plt.ylabel("Inertia")
    # plt.show()

    # Choose k (e.g., 3) based on the Elbow Curve
    kmeans = KMeans(n_clusters=3, random_state=42)
    songs['cluster'] = kmeans.fit_predict(X_scaled)

    # Visualize clusters (2D projection using PCA for simplicity)
    from sklearn.decomposition import PCA

    silhouette_avg = silhouette_score(X, songs['cluster'])
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Inertia: {kmeans.inertia_}")

    davies_bouldin = davies_bouldin_score(X, songs['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin}")

    # PCA1 -> Overall Complexity related to unique_word_density, syllable_density, and total_words
    # PCA2 -> Structural Simplicity related to line_density and lines
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    songs['pca1'] = X_pca[:, 0]
    songs['pca2'] = X_pca[:, 1]

    # plt.figure(figsize=(10, 7))
    # sns.scatterplot(x='pca1', y='pca2', hue='cluster', data=songs, palette='Set2', s=100)
    # plt.title("Clusters of Songs Based on Lyrical Features")
    # plt.xlabel("Overall Complexity")
    # plt.ylabel("Structural Simplicity")
    # plt.legend(title="Cluster")
    # plt.show()

    # Display the clustered DataFrame
    print(songs)

    # will need both else would lead to inaccurate results
    pathToModelFolder = path + "/" + "models" + "/"
    joblib.dump(kmeans, pathToModelFolder + 'kmeans_model2.pkl')
    joblib.dump(scaler, pathToModelFolder + 'kmeans_scaler2.pkl')
    print("Model and scaler saved!")


def changedKmeans2(songs):
    X = songs[[ 'word_count', 'word_count_unique', 'unique_words', 'syllable_density', 'line_density']]
    y = songs['lyrical_density']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using the Elbow Method
    inertia = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    # # Plot the Elbow Curve
    # plt.figure(figsize=(8, 5))
    # plt.plot(k_range, inertia, marker='o')
    # plt.title("Elbow Method for Optimal K")
    # plt.xlabel("Number of Clusters (k)")
    # plt.ylabel("Inertia")
    # plt.show()

    # Choose k (e.g., 3) based on the Elbow Curve
    kmeans = KMeans(n_clusters=3, random_state=42)
    songs['cluster'] = kmeans.fit_predict(X_scaled)

    # Visualize clusters (2D projection using PCA for simplicity)
    from sklearn.decomposition import PCA

    silhouette_avg = silhouette_score(X, songs['cluster'])
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Inertia: {kmeans.inertia_}")

    davies_bouldin = davies_bouldin_score(X, songs['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin}")

    # PCA1 -> Overall Complexity related to unique_word_density, syllable_density, and total_words
    # PCA2 -> Structural Simplicity related to line_density and lines
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    songs['pca1'] = X_pca[:, 0]
    songs['pca2'] = X_pca[:, 1]

    # plt.figure(figsize=(10, 7))
    # sns.scatterplot(x='pca1', y='pca2', hue='cluster', data=songs, palette='Set2', s=100)
    # plt.title("Clusters of Songs Based on Lyrical Features")
    # plt.xlabel("Overall Complexity")
    # plt.ylabel("Structural Simplicity")
    # plt.legend(title="Cluster")
    # plt.show()

    # Display the clustered DataFrame
    print(songs)

    # will need both else would lead to inaccurate results
    pathToModelFolder = path + "/" + "models" + "/"
    joblib.dump(kmeans, pathToModelFolder + 'kmeans_model3.pkl')
    joblib.dump(scaler, pathToModelFolder + 'kmeans_scaler3.pkl')
    print("Model and scaler saved!")

def changedKmeans3(songs):
    X = songs[[ 'syllable_density', 'line_density']]
    y = songs['lyrical_density']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using the Elbow Method
    inertia = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    # # Plot the Elbow Curve
    # plt.figure(figsize=(8, 5))
    # plt.plot(k_range, inertia, marker='o')
    # plt.title("Elbow Method for Optimal K")
    # plt.xlabel("Number of Clusters (k)")
    # plt.ylabel("Inertia")
    # plt.show()

    # Choose k (e.g., 3) based on the Elbow Curve
    kmeans = KMeans(n_clusters=3, random_state=42)
    songs['cluster'] = kmeans.fit_predict(X_scaled)

    # Visualize clusters (2D projection using PCA for simplicity)
    from sklearn.decomposition import PCA

    silhouette_avg = silhouette_score(X, songs['cluster'])
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Inertia: {kmeans.inertia_}")

    davies_bouldin = davies_bouldin_score(X, songs['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin}")

    # PCA1 -> Overall Complexity related to unique_word_density, syllable_density, and total_words
    # PCA2 -> Structural Simplicity related to line_density and lines
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    songs['pca1'] = X_pca[:, 0]
    songs['pca2'] = X_pca[:, 1]

    # plt.figure(figsize=(10, 7))
    # sns.scatterplot(x='pca1', y='pca2', hue='cluster', data=songs, palette='Set2', s=100)
    # plt.title("Clusters of Songs Based on Lyrical Features")
    # plt.xlabel("Overall Complexity")
    # plt.ylabel("Structural Simplicity")
    # plt.legend(title="Cluster")
    # plt.show()

    # Display the clustered DataFrame
    print(songs)

    # will need both else would lead to inaccurate results
    pathToModelFolder = path + "/" + "models" + "/"
    joblib.dump(kmeans, pathToModelFolder + 'kmeans_model4.pkl')
    joblib.dump(scaler, pathToModelFolder + 'kmeans_scaler4.pkl')
    print("Model and scaler saved!")

def changedKmeans4(songs):
    X = songs[[  'syllables', 'lines', 'unique_word_density', 'word_count',
                 'word_count_unique', 'unique_words', 'syllable_density', 'line_density']]
    y = songs['lyrical_density']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Determine optimal number of clusters using the Elbow Method
    inertia = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    # # Plot the Elbow Curve
    # plt.figure(figsize=(8, 5))
    # plt.plot(k_range, inertia, marker='o')
    # plt.title("Elbow Method for Optimal K")
    # plt.xlabel("Number of Clusters (k)")
    # plt.ylabel("Inertia")
    # plt.show()

    # Choose k (e.g., 3) based on the Elbow Curve
    kmeans = KMeans(n_clusters=3, random_state=42)
    songs['cluster'] = kmeans.fit_predict(X_scaled)

    # Visualize clusters (2D projection using PCA for simplicity)
    from sklearn.decomposition import PCA

    silhouette_avg = silhouette_score(X, songs['cluster'])
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Inertia: {kmeans.inertia_}")

    davies_bouldin = davies_bouldin_score(X, songs['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin}")

    # PCA1 -> Overall Complexity related to unique_word_density, syllable_density, and total_words
    # PCA2 -> Structural Simplicity related to line_density and lines
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    songs['pca1'] = X_pca[:, 0]
    songs['pca2'] = X_pca[:, 1]

    # plt.figure(figsize=(10, 7))
    # sns.scatterplot(x='pca1', y='pca2', hue='cluster', data=songs, palette='Set2', s=100)
    # plt.title("Clusters of Songs Based on Lyrical Features")
    # plt.xlabel("Overall Complexity")
    # plt.ylabel("Structural Simplicity")
    # plt.legend(title="Cluster")
    # plt.show()

    # Display the clustered DataFrame
    print(songs)

    # will need both else would lead to inaccurate results
    pathToModelFolder = path + "/" + "models" + "/"
    joblib.dump(kmeans, pathToModelFolder + 'kmeans_model5.pkl')
    joblib.dump(scaler, pathToModelFolder + 'kmeans_scaler5.pkl')
    print("Model and scaler saved!")