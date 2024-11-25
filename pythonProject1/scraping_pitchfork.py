import pathlib
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

folder_name = "data_original"
billboardFile = "pitchfork.csv"
pathToFolder= str(pathlib.Path().resolve()) +"/"+ folder_name + "/" + billboardFile

list_song_100 = {
    "Song": [],
    "Artist": [],
    "Year": [],
}

# URL of the Pitchfork page
urls = ["https://pitchfork.com/features/lists-and-guides/best-songs-2023/",
       "https://pitchfork.com/features/lists-and-guides/best-songs-2022/",
       "https://pitchfork.com/features/lists-and-guides/best-songs-2021/",
       "https://pitchfork.com/features/lists-and-guides/best-songs-2020/",
       "https://pitchfork.com/features/lists-and-guides/best-songs-2019/",]


# Send a GET request to fetch the page content
for url in urls:
    print(url +"  "+ re.search(r'\d{4}', url).group())
    response = requests.get(url)
    match = re.search(r'best-songs-(\d{4})', url)
    year = match.group(1)
    print(f"Year: {year}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.find_all('h2')
        for h2 in soup.find_all('h2'):
            text = h2.text.strip()
            if ":" in text:
                artist, song = text.split(":", 1)
                artist = artist.strip()
                song = song.strip(' “”')
                print(f"Artist: {artist}, Song: {song}")
                list_song_100['Song'].append(song)
                list_song_100['Artist'].append(artist)
                list_song_100['Year'].append(year)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# saving dictionary in filename
df = pd.DataFrame(list_song_100)
df.to_csv(pathToFolder,index=False, header=False)