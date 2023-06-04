import time
import xdrlib
from xml.etree.ElementTree import tostring
import requests
import pytwitter
import sys
import random

api = pytwitter.Api(
    access_secret="", # access secret here 
    access_token="", # access token here
    consumer_key="", # consumer key here
    consumer_secret="" # consumer secret here (you can get this & everything else @ https://developer.twitter.com/en/docs/twitter-api)
)

# detail = User.data['detail']
# print(str(detail))

char = "0123456789abcdefghijklmnopqrstuvwxyz_"
charList = list(char)

def userRandomizer():
    randomList = random.choices(charList,k=5)
    string = ""

    return (string.join(randomList))

usernameInput = userRandomizer()
accountStatus = ""

def GetUser(): # function that sends a request to receive the user's data
    available = "Could not find user" # the variable "available" has a string of code thats found in accounts w unclaimed users etc..
    suspended = "User has been suspended" # ^^^^
    sys.tracebacklimit=0 # disables that big ass error msg whenever u get an available/susp account
    try:
        User = api.get_user(username=usernameInput)
    except Exception as error:
        errorMessage = str(error)
        print(errorMessage)
        if available in errorMessage:
            print("that account is available: " + usernameInput) 
        elif suspended in errorMessage:
            userRandomizer()
            return (suspended)
    else: 
        return(str(User.data))
while True:
    if GetUser() == "User has been suspended":
        print("user has been suspended")
        userRandomizer()
        usernameInput = userRandomizer()
    elif GetUser() == "Could not find user":
        userRandomizer()
        usernameInput = userRandomizer()
    else:
        userRandomizer()
        usernameInput = userRandomizer()




