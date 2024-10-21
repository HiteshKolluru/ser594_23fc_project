import pandas as pd
import requests
from bs4 import BeautifulSoup
import pathlib

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#please change this path as required as your path will be different from mine
# filename = "billboard_hot_100.csv"
# pathToFolder = "/Users/twisted_fate/Desktop/594 Data Science/ser594_23fc_project/pythonProject1/data_original/billboard_hot_100.csv"

# this should work fine if it does not replace
# every thing before the name of the csv file with absolute path to foldername => data_original
folder_name = "data_original"
billboardFile = "billboard_current_week_100.csv"
pathToFolder= str(pathlib.Path().resolve()) +"/"+ folder_name + "/" + billboardFile


print("Starting the Web Scraper to scrape " + url + " for the current weeks top 100 songs \n")

# Dictionary to store data
list_song_100 = {
    "Song": [],
    "Artist": [],
}

#Scraping for each of the 100 songs
for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
    song = container.find("h3", {"class": "c-title"}).text.strip()
    artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

    # Printing data being scraped
    print("Song: " + song)
    print("Artist: " + artist)
    print("\n")

    #storing data scraped in dictionary
    list_song_100['Song'].append(song)
    list_song_100['Artist'].append(artist)

# saving dictionary in filename
df = pd.DataFrame(list_song_100)
df.to_csv(pathToFolder,index=False)