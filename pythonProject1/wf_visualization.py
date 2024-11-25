import pathlib
import pandas as pd
from matplotlib import pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
from collections import Counter


def get_sentiment(text, analyzer):
    scores = analyzer.polarity_scores(text)

    if scores['neu'] == 1.0:
        return 0
    elif scores['pos'] == 1.0:
        return 1
    elif scores['neg'] == 1.0:
        return -1
    else:
        return scores['compound']


def mainViz():

    analyzer = SentimentIntensityAnalyzer()
    # this should work fine if it does not replace
    # every thing before the name of the csv file with absolute path to foldername => data_original
    folder_name = "data_original"
    savefolder = '/visuals/'
    path = str(pathlib.Path().resolve())
    pathToFolder = path + "/" + folder_name + "/"
    csvProcessed = 'ArtistwithLyricsProcessed.csv'
    songs = pd.read_csv(pathToFolder + csvProcessed)
    songs_dict = songs.to_dict('list')

    cleaned_text = ""
    coun = Counter()
    listWords = []
    for song in songs_dict['Lyrics_Processed']:
        tempstr = song.split(" ")
        cleaned_text = cleaned_text + " " + song
        coun.update(tempstr)
        for word in tempstr:
            listWords.append(word)

    word = []
    count = []
    for con in coun.most_common(10):
        word.append(con[0])
        count.append(con[1])

    plt.barh(word, count, color='lightblue')
    plt.ylabel("Words")
    plt.xlabel("Count")
    plt.title("Top 10 most common words")
    plt.savefig(path + savefolder + "top10_words.png", bbox_inches='tight')
    plt.show()
    plt.close()

    wordcloud = WordCloud(background_color='darkgrey', width=2000, height=1000, collocations=False,
                          random_state=100).generate(cleaned_text)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")

    plt.savefig(path + savefolder + "WordCloud.png", bbox_inches='tight')
    plt.show()
    plt.close()

    # trying to see if I can plot words wrt their sentiment.
    pWords = []
    nWords = []
    neutralWords = []
    sentofWords = []

    for word in listWords:
        sent = get_sentiment(word, analyzer)
        sentofWords.append(sent)
        if sent > 0:
            pWords.append(word)
        elif sent < 0:
            nWords.append(word)
        else:
            neutralWords.append(word)

    plt.bar(['positive', 'neutral', 'negative'], [len(pWords), len(neutralWords), len(nWords)],
            color=['green', 'lightblue', 'red'], width=0.5)
    plt.xlabel("tendancy")
    plt.ylabel('count of positive neutral and negative words')
    plt.title("sentiment of words")

    plt.savefig(path + savefolder + "Wordsentiment.png", bbox_inches='tight')
    plt.show()
    plt.close()

    # individual Artists most used words in their popular songs of this week
    song = songs_dict['Lyrics_Processed']
    artist = songs_dict['artist']

    # billie = []
    # bCount = Counter()
    # sabrina = []
    # sCount = Counter()
    # chapple = []
    # cCount = Counter()
    # for i in range(len(song)):
    #     if (artist[i] == 'Billie Eilish'):
    #         tempstr = song[i].split(" ")
    #         bCount.update(tempstr)
    #         billie.append(song[i])
    #
    #     if (artist[i] == "Sabrina Carpenter"):
    #         tempstr = song[i].split(" ")
    #         sCount.update(tempstr)
    #         sabrina.append(song[i])
    #
    #     if (artist[i] == "Chappell Roan"):
    #         tempstr = song[i].split(" ")
    #         cCount.update(tempstr)
    #         chapple.append(song[i])

    # print(billie)
    # print(sabrina)
    # print(chapple)

    # word_list = []
    # counts_list = []
    # for con in bCount.most_common(30):
    #     word_list.append(con[0])
    #     counts_list.append(con[1])
    #
    # plt.bar(word_list, counts_list, color='green', width=0.5)
    # plt.xlabel("Words")
    # plt.ylabel("Count")
    # plt.title("Top 30 most common words Billie Eilish")
    # plt.xticks(rotation=45, ha='right')
    #
    # # plt.savefig("your_file_name"+".png", bbox_inches='tight')
    # plt.savefig(path + savefolder + "Top30BillieEilish.png", bbox_inches='tight')
    # plt.show()
    # plt.close()
    #
    # # Sabrina Carpenter
    # word_list = []
    # counts_list = []
    # for con in sCount.most_common(30):
    #     word_list.append(con[0])
    #     counts_list.append(con[1])
    #
    # plt.bar(word_list, counts_list, color='blue', width=0.5)
    # plt.xlabel("Words")
    # plt.ylabel("Count")
    # plt.title("Top 30 most common words Sabrina Carpenter")
    # plt.xticks(rotation=45, ha='right')
    #
    # # plt.savefig("your_file_name"+".png", bbox_inches='tight')
    # plt.savefig(path + savefolder + "Top30SabrinaCarpenter.png", bbox_inches='tight')
    # plt.show()
    # plt.close()
    #
    # # Chapple Roan
    # word_list = []
    # counts_list = []
    # for con in cCount.most_common(30):
    #     word_list.append(con[0])
    #     counts_list.append(con[1])
    #
    # plt.bar(word_list, counts_list, color='red', width=0.5)
    # plt.xlabel("Words")
    # plt.ylabel("Count")
    # plt.title("Top 30 most common words Chappell Roan")
    # plt.xticks(rotation=45, ha='right')
    #
    # # plt.savefig("your_file_name"+".png", bbox_inches='tight')
    # plt.savefig(path + savefolder + "Top30ChappelRoan.png", bbox_inches='tight')
    # plt.show()
    # plt.close()

    # # Create the bar chart
    # plt.figure(figsize=(100, 30))
    #
    # # Plot the bars
    # plt.bar(word_list, counts_list)
    # plt.xticks(rotation=35, ha='right')
    # plt.xlabel("Words")
    # plt.ylabel("Frequency")
    # plt.title("Word Frequency Distribution Chappell Roan")
    #
    # # Display the chart
    # plt.tight_layout()
    # plt.show()
    # not saving for now

if __name__ == "__main__":
    mainViz()


