import pandas as pd
import snscrape.modules.twitter as tweets
import streamlit as st
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')  # To connect with local host
mydb = client['mydb']
mycol = mydb['data']


def scrapper(tags, end, start, p):  # tweets scrapping function
    tweet1 = []
    text = '{} since:{} until:{}'.format(tags, start, end)  # Join hashtag with date range
    for i, tweet in enumerate(tweets.TwitterSearchScraper(text).get_items()):  # To get tweets
        if i > p - 1:
            break
        tweet1.append(
            [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,
             tweet.lang, tweet.source, tweet.likeCount])  # To store data into list
    tweet_coll = pd.DataFrame(tweet1,
                              columns=['Date', 'id', 'url', 'content', 'user name', 'Reply count', 'Retweet count',
                                       'Lang', 'source', 'Like count'])  # To store all data into dataframe
    return tweet_coll


def json_data(ab):  # Function for downloading json file
    json_button = st.download_button(label='Download data as json file', data=ab.to_json(),
                                     file_name='Tweets_data.json',
                                     mime='application/json')


def csv_data(cd):  # Function for downloading csv file
    csv_button = st.download_button(label='Download data as csv file', data=cd.to_csv(), file_name='Tweets_data.csv',
                                    mime='text/csv')


def storage(fd, tag):  # Function for storing  data in MongoDB
    mylist = fd.to_dict('records')
    data = {tag: mylist}
    y = mycol.insert_one(data)  # Stores data into MongoDB
    return st.info('Data Stored successfully')


st.title('Twitter scrapping')
name = st.text_input("Enter hashtag: ")
hashtag = '#' + name

start_date = st.date_input("From: ")
end_date = st.date_input("To: ")

x = st.number_input(label="Enter max no of tweets:", step=1)
clicked = st.button(label='Submit')

if clicked == 1:
    df = scrapper(hashtag, end_date, start_date, x)
    st.dataframe(df)
    json_data(df)
    csv_data(df)

storing = st.button('Click here to store data')
if storing == 1:
    xy = scrapper(hashtag, end_date, start_date, x)
    storage(xy, hashtag)
