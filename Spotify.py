from array import *

## Create a MongoClient to the running mongod local instance
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

database = client["admin"]
collection = database["topSpotify2018"]
print("---------------------------------------")

def get_all_songs_by_an_artist(artist_name):
    myCursor = collection.find({'artists': {'$regex':artist_name, '$options':'i'}})
    if(myCursor.count() != 0):
        for values in myCursor:
            print(values['name'])
    else:
        print("I'm sorry, we could not find songs by the artist: "+artist_name)



def find_words_in_the_song(text_to_search):
    myCursor = collection.find({'name': {'$regex':text_to_search}})
    print "Count is: ",myCursor.count()
    for values in myCursor:
        print(values['name'])

def 

##Find all the songs composed by an artist
artist_name=raw_input("Which artist's songs are you interested in? >>  ")
get_all_songs_by_an_artist(artist_name)
print("---------------------------------------")

##How many artists have been featured in a song
print("How many artists have been featured in a song? >> ")
find_words_in_the_song("feat")
print("---------------------------------------")


##List all the songs that could be played in a discotheque
## Logic used: danceability>0.7 && energy>0.5
print("List all the songs that could be played in a discotheque")
