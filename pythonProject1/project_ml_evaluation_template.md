#### SER594: Machine Learning Evaluation
#### Title: Lyric Insights: Analyzing Sentiment and Clustering Song Patterns Using Machine Learning
#### Author: Hitesh Kolluru
#### Date: November 25th, 2024

## Evaluation Metrics
I am showing results for happy and sad for a songs lyrics
and then classifying the song between 3 types
"Complex and Poetic",
"Simple and Catchy",
"Balanced and Moderate"

## Interpretation: Interpreting the output

the first 2 lines are to take input from the user for song title and artist name
the following lines are related to the sadness and happiness score for the song
finally it states if the song is a happy or sad song
then the final line describes the song based on its lyrical features like 
wordcount, unique wordcount, lyrical density, use of syllables, lines, 
syllable_density, line density.

### Metric 1
**Name:** Testing the song 'baby' by 'Justin Bieber'

**the songs lyrics:**
Oh-ooh-whoa-oh-oh-oh-oh
Oh-ooh-whoa-oh-oh-oh-oh
Oh-ooh-whoa-oh, oh-oh-oh-oh
You know you love me (yo), I know you care (uh-huh)
Just shout whenever (yo), and I'll be there (uh-huh)
You are my love (yo), you are my heart (uh-huh)
And we will never, ever, ever be apart (yo, uh-huh)
Are we an item? (Yo) girl, quit playin' (uh-huh)
"We're just friends" (yo), what are you sayin'? (Uh-huh)
Said, "There's another" (yo), and looked right in my eyes (uh-huh)
My first love broke my heart for the first time, and I was like (yo, uh-huh)
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine
Oh, for you, I would've done whatever (uh-huh)
And I just can't believe (yo) we ain't together (uh-huh)
And I wanna play it cool (yo), but I'm losin' you (uh-huh)
I'll buy you anything (yo), I'll buy you any ring (uh-huh)
And I'm in pieces (yo), baby, fix me (uh-huh)
And just shake me 'til you wake me from this bad dream (yo, uh-huh)
I'm goin' down (oh), down, down, down (uh-huh)
And I just can't believe, my first love won't be around, and I'm like
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine (Luda!)
When I was 13, I had my first love
There was nobody that compared to my baby
And nobody came between us, nor could ever come above
She had me goin' crazy, oh, I was starstruck
She woke me up daily, don't need no Starbucks (woo)
She made my heart pound
And skip a beat when I see her in the street and
At school on the playground
But I really wanna see her on the weekend
She knows she got me dazin'
'Cause she was so amazin'
And now, my heart is breakin'
But I just keep on sayin'
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine
"Baby, baby, baby, oh"
Like, "Baby, baby, baby, no"
Like, "Baby, baby, baby, oh"
I thought you'd always be mine, mine
I'm gone (yeah, yeah, yeah, yeah, yeah, yeah)
Now, I'm all gone (yeah, yeah, yeah, yeah, yeah, yeah)
Now, I'm all gone (yeah, yeah, yeah, yeah, yeah, yeah)
Now, I'm all gone (gone, gone, gone)
I'm gone


**Output Generated**
Enter song title: baby
Enter artist name: justin beiber
Sad
[0.52967101]
Happy
[1.34394999]
Song is happy
Model and scaler loaded!
New Song 1 is assigned to: Simple and Catchy

**Choice Justification:** 
The song "Baby" by Justin Bieber is classified as "Simple and Catchy" because of 
its repetitive lyrics and straightforward structure. Words like "baby" are repeated 
often, leading to a high total word count but a lower unique word density. 
The short lines and simple vocabulary result in a high line density and a simple, 
memorable style.

The emotional analysis shows a higher happiness score (1.34) than sadness (0.53), 
reflecting its upbeat tone and themes of young love despite hints of heartbreak. 
These traits align well with the characteristics of the "Simple and Catchy" cluster, 
which represents songs designed for mass appeal and memorability.

### Metric 2
**Name:** Testing the song 'perfume' by 'Mehro'

**the songs lyrics:**
The present is so unsatisfying
I wish I was materialistic
Excited for the future unfolding
Thank god I'm not realistic
Heels over head in the bedroom
You smell so good, don't need perfume
I'm a tulip, you're the spring bloom
I'd be a fool not to love you
Headed down, I see green lights
Block after block, nearly sunrise
Rolling my way through stop signs
Pinned down by jealous minds
Heels over head in the bedroom
You smell so good, don't need perfume
I'm a tulip, you're the spring bloom
I'd be a fool not to love you
Yeah, don't ever change
Stay the same, stay the same
That's the last thing I said
To you

**Output generated**
Enter song title: perfume
Enter artist name: mehro
Sad
[0.80449031]
Happy
[1.06087255]
Song is happy
Model and scaler loaded!
New Song 1 is assigned to: Balanced and Moderate

**Choice Justification:** 
The song is not strongly leaning towards either sad or happy, although I would classify
the song as sad, but it has elements of both sad and happy
"The present is so unsatisfying" and "Pinned down by jealous minds" indicates sadness
"I'm a tulip, you're the spring bloom" and "You smell so good, don't need perfume,"
are indicative of happiness or a positive notion.
The song falls into the "Balanced and Moderate" cluster, which is accurate as the
lyrics are not overly complicated yet the simple words and phrases used hold 
strong meanings, it is a very poetic song.
The emotional tone and structure are suggestive mix of both happiness and sadness 
with moderate complexity.



### Metric 3
**Name:** Testing the song 'masterpeice' by 'Cloudy June'

**song lyrics**
You hide your eyes behind the shades
You stroke can make the climate change
Your art should see the light of day (you and me a masterpiece)
You never let your colors show
Lose your face when we get close
I've seen you paint, nobody knows (you and me a masterpiece)
You've got an artist inside you
Come drown in my navy blue
Tonight let the artist inside me be you
Baby paint me like a canvas - don't mind
Your dripping colors on the mattress - tonight
Dip your brush into the pallet - oh my
Make the shades of you and me a masterpiece
Put your body where my heart is - my love
I'm the muse and you're the artist don't stop
Gotta finish what you started - oh god
Make the shades of you and me a masterpiece
You make me Scream in Starry Nights
The golden kiss, mysterious smile
You never let the paint run dry (you and me a masterpiece)
I'm standing pose for your design
Your fingertips, they reach for mine
Let's make a mess and cross the line (you and me a masterpiece)
You got an artist inside you
Come drown in my navy blue
Tonight let the artist inside me be you
Baby paint me like a canvas - don't mind
Your dripping colors on the mattress - tonight
Dip your brush into the pallet - oh my
Make the shades of you and me a masterpiece
Put your body where my heart is - my love
I'm the muse and you're the artist don't stop
Gotta finish what you started - oh god
Make the shades of you and me a masterpiece
Make the shades of you and me a masterpiece
Baby paint me like a canvas
Your dripping colors on the mattress
Drip your brush into the pallet
And make the shades of you and me a masterpiece
Baby, paint me like a canvas - don't mind
Your dripping colors on the mattress - tonight
Dip your brush into the palette - oh my
Make the shades of you and me a masterpiece
Put your body where my heart is - my love
I'm the muse and you're the artist don't stop
Gotta finish what you started - oh god
Make the shades of you and me a masterpiece

**Output Generated**
Enter song title (or 'quit' to exit): masterpeice
Enter artist name: cloudy june
Sad
[0.67786278]
Happy
[0.63176546]
Song is sad
Model and scaler loaded!
New Song 1 is assigned to: Complex and Poetic

**Choice Justification:** 
The song is in my opinion correctly identified as a sad
song it aims to pull at the emotional stings of the heart it is intimate
and not a vibrantly joyful song, and so I think this evaluation is valid,
but it is important to understand the song is not strictly sad but lines like
"You never let your colors show" and "Lose your face when we get close" 
suggest are suggestive of holding back and so it tends more on being a sad song 
than a happy song.
the lyrics in the song are very creative and suggestive the artist cloudy june uses
a lot of different phrases to mean different thing and invoke a variety of emotions
from within the listner and so it being classify as a complex and poetic song makes 
a lot of sense.

## Alternative Models
### Alternative 1
[linear_regression_model.pkl](models/linear_regression_model.pkl)

**Construction:** 
used vectorized song lyrics and compounded sentiment to identify sentiment in songs

**Evaluation:** 
Accuracy: 0.73
Precision: 0.76
Recall: 0.86
F1 Score: 0.81
Mean Squared Error (MSE): 0.1777

### Alternative 2
[linear_regression_Word2Vec_model.pkl](models/linear_regression_Word2Vec_model.pkl)
**Construction:**
used vectorized song lyrics and compounded sentiment to identify sentiment in songs
applied smote to increase sample in data to manage underfitting.


**Evaluation:** 
Accuracy: 0.53
Precision: 0.64
Recall: 0.66
F1 Score: 0.65
Mean Squared Error (MSE): 37692.4330


### Alternative 3

[linear_regression_happy_model.pkl](models/linear_regression_happy_model.pkl)

**Construction:** 
Used happy words associaated within song lyrics to identify and tag songs as happy songs
used this to then compare with song lyrics and then predict if the song is a happy song


**Evaluation:** 
Accuracy: 0.80
Precision: 0.83
Recall: 0.91
F1 Score: 0.87
Mean Squared Error (MSE): 0.1663

### Alternative 4

[linear_regression_sad_model.pkl](models/linear_regression_sad_model.pkl)

**Construction:**
Used happy words associaated within song lyrics to identify and tag songs as sad songs
used this to then compare with song lyrics and then predict if the song is a sad song

**Evaluation:** 
Accuracy: 0.61
Precision: 0.61
Recall: 0.74
F1 Score: 0.67
Mean Squared Error (MSE): 0.2513

(duplicate above three times; remove this line when done)


## Visualization
### Visual N
**Analysis:** The Kmeans models the clusters it was able to identify.
![mykmeansplot.png](visuals/mykmeansplot.png)

the use of the elbow method to identify the most optimal K
![iterationtofindOptimalK.png](visuals/iterationtofindOptimalK.png)


## Best Model

**Model:**My Kmeans model [kmeans_model.pkl](models/kmeans_model.pkl)

My best model is the kmeans model that identifies how 
complex a song is based on the lyrical density of the song through various factor 
like wordcount, unique wordcount, lyrical density, use of syllables, lines, 
syllable_density, line density.

