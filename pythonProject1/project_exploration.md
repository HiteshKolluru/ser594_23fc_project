SER594: Exploratory Data Munging and Visualization
Title: Analyzing music lyrics and their sentiments 
Author: Hitesh Kolluru
Date: October, 22nd
## Basic Questions
Dataset Author: Hitesh Kolluru
Dataset Record Count: 100 songs 
Dataset Field Meanings: artist, Song name, song id for genius, song url genius, Songlyrics, processed lyrics, sentiment of lyrics
It has the name of the artist and the song id and the followed by the lyrics and after processing I add a few more attributes one for processed lyrics and then for sentiment of lyrics
**Dataset File Hash(es):** Created dataset so not needed 
## Interpretable Records
### Record 1

RAW Data

Chappell Roan,10090037,"Good Luck, Babe!",https://genius.com/Chappell-roan-good-luck-babe-lyrics,"101 ContributorsTranslationsBahasa IndonesiaPortuguêsDeutschEspañolFrançaisTürkçeHebrewItalianoDanskCatalàTiếng ViệtPolskiGood Luck, Babe! Lyrics
It's fine, it's cool
You can say that we are nothing, but you know the truth
And guess I'm the fool
With her arms out like an angel through the car sunroof

I don't wanna call it off
But you don't wanna call it love
You only wanna be the one that I call ""baby""

You can kiss a hundred boys in bars
Shoot another shot, try to stop the feeling
You can say it's just the way you are
Make a new excuse, another stupid reason
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling

I'm cliché, who cares?
It's a sexually explicit kind of love affair
And I cry, it's not fair
I just need a little lovin', I just need a little air
You might also like
Think I'm gonna call it off
Even if you call it love
I just wanna love someone who calls me ""baby""

You can kiss a hundred boys in bars
Shoot another shot, try to stop the feeling
You can say it's just the way you are
Make a new excuse, another stupid reason
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling

When you wake up next to him in the middle of the night
With your head in your hands, you're nothing more than his wife
And when you think about me all of those years ago
You're standing face to face with ""I told you so""
You know I hate to say it, I told you so
You know I hate to say, but I told you so

You can kiss a hundred boys in bars
Shoot another shot, try to stop the feeling (Well, I told you so)
You can say it's just the way you are
Make a new excuse, another stupid reason
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling
Good luck, babe (Well, good luck)
Well, good luck, babe (Well, good luck)
You'd have to stop the world just to stop the feeling
You'd have to stop the world just to stop the feeling
You'd have to stop the world just to stop the feeling
You'd have to stop the world just to stop the feeling12Embed"

Interpretation: 
It has the name of the artist and the song id, url and the followed by the lyrics and after processing I add a few more attributes one for processed lyrics and then for sentiment of lyrics


### Record 2
Raw Data: 

Rod Wave,10972409,25,https://genius.com/Rod-wave-25-lyrics,"21 Contributors25 Lyrics
Uh, uh-uh, uh, uh
Oh, do you do this often?
I know it sound wrong, like, everything I left in Maryland
I just don't wanna see myself anymore, I don't
They, like, they say they miss me and shit, shut up, for real, like, man
Look, 'kay

DJ, run it back, play my song in this bitch
Vibin' like I'm alone in this bitch, mm
Tit for tat, I got you back, was I wrong for that shit?
Tell me, is we too grown for that shit? Uh
I wanna lock it in, baby, no weighin' my options
Wanna travel, see the world, gettin' drunk on an island
Wanna settle, start a family, so tell me about it
And you so perfect, baby, don't give nobody that body (Okay)
Social anxiety, I fear
And I done been this way for some years
I don't really get along with my peers
Everything that they do to me is weird
So in a world full of weirdos, fools, and scrubs
Tell me, what is it you're willin' to do for love?
You know it's true that the datin' pool is fucked
Ain't nobody out here, baby, it just be us
And I know, and I know, and I know, and I know a broken heart when I see one
And I feel, and I feel, and I feel, and I feel like I love you more
Did you know? Do you know? Did you know? Do you know I'm a shoulder if you need one?
When I feel what I feel, keep it real, what’s the deal? I'm ready for
Oh, somewhere we could be alone, you and me alone
I remember bein' twenty-one when my life had just begun
Twenty-two, many things to see and do
Twenty-three, lookin' forward to twenty-four
Is it just me or it ain't no love no more?
Twenty-five, what a time to be alive
Am I getting old? Why do I feel tired?
All the same old things, the same old games
Same old pain, think it's time for a change 'cause
Certain shit ain't like me no more
Certain shit don't excite me no more
It don't excite no more, no
It ain't like me no more
No more, no more
No, no, no, no, no
Certain shit don't excite me no more
It ain't like me no more
This ain't like me no more, no
It don't excite me no more, uh
See Rod Wave LiveGet tickets as low as $80You might also like
UhEmbed"

Interpretation: 
It has the name of the artist and the song id, url and the followed by the lyrics and after processing I add a few more attributes one for processed lyrics and then for sentiment of lyrics

## Background Domain Knowledge




## Dataset Generality
I get the data from the current top 100 songs on the billboard charts and then use this data to fetch the song details from genius
it has the latest and the most popular songs of the current week and will change as per the chart's updates when ever the file for billboard is run to fetch the scrapped data.

## Data Transformations
I get raw lyrics from genius and the text has irrelevant text at the start and at the end of the lyrics and those need to be removed 
so I split the string and keep the necessary section and discard the rest, then I remove punctuations, stop words and clean the text further

### Transformation N
Description: removal of stop words, punctuations
Soundness Justification: I have only removed text data that won't be relevant like punctuation so we can focus on 
more meaningful words, reduce noise and improve accuracy when visualising this data.
Description: Added sentiment 
Soundness Justification: wanted to process sentiment of lyrics to get an understand on what the general sentiment of the lyrics was.

## Visualizations
created a visualization of the most common words by the 3 most popular artists and then also by the general data.
show the most used words by artist and their count in their lyrics.
created a sentiment analysis of the general words that are used. it shows an overwhelming majority for neutral words as expected and few positive and negative words
created a wordcloud to show the most popular words. it show how often a word is used and and give an understanding of the frequency.

### Visual N
Analysis:
Was 
