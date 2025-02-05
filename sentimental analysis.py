from textblob import TextBlob
import pandas as pd

#check to analyze the sentiment of a given sentence
def analyze_sentiment(sentence):
    word = sentence.strip().lower()
    sentiment = TextBlob(word).sentiment
    if sentiment.polarity > 0:
        return "positive"
    elif sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

#test cases of sentences for analysis
test_sentences = [
    "you are lame go make me breakfast!!",   #negative
    "happy bday!",  #postive
    "So hot today =_= don`t like it and i hate my new timetable, having such a bad week",  #negative
    "and within a short time of the last clue all of them",  #neutral
    "What did you get? My day is alright.. haven`t done anything yet. leaving soon to my stepsister tho...",  #neutral
]

#create a dataframe using pandas to store the test sentences and their sentiment
results = pd.DataFrame({"Text": test_sentences, "Sentiment": [analyze_sentiment(text) for text in test_sentences]})
print(results)