# Introduction
Author: Hitesh Kolluru
Course: SER 594 Data Science

Notes about the project:

Created a web scraper for collecting this weeks top 100 billboard songs
Created a script to call the lyricsgenius API to give details regarding each of the songs and a few more.

Things to note for the lyricsgenius API:

I have added my personal key to run the project for the time being but ideally you should create your own token and then run the code

Use the following link and sign up then go to API management  and enter details it should show the option to generate	a token which can then be used.
The Link: https://docs.genius.com/#/getting-started-h1

Things to implement in the future maybe?
The collecting_date.py file runs for a good minute, if needed I might add some print statements to execute so it does not seem like it not doing anything.

The lyrics sometimes have other languages, so they need to be tagged for being either English or not. Also need to consider if in the future we need to skip songs that have other languages(ideally do not prefer)

Some of the lyrics are not songs so need to figure out how to either filter it out of the data generated or ensure it is not added to the data in the first place.






