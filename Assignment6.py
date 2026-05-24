#Extracting data from OPEN WEATHER API

import requests
def weather_data(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a7a6eba4b65f3fb30eda10c74221c92"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        print(data['main'])
        
    except requests.exceptions.RequestException as e:
        print(e)
        
city=input("enter city name")
weather_data(city)

# ROCK PAPER SCISSOR GAME

l=["rock","paper","scissor"]
import random

for i in range(6):
    print("Users Turn")
    us=0
    print("Choose no from 1,2,3 when 1=Rock 2=Paper 3=Scissor")
    n=int(input("enter a no"))
    
    if(n==1):
        print("rock")
    elif(n==2):
        print("paper")
    elif(n==3):
        print("scissor")
    else:
        print("Please enter a valid no.")        #*
        
        
        
    print("Computer's Turn")
    cs=0
    x=random.choice(l)
    print(x)
    
    if(n==1 and x=="rock"):
        print("Game Draw")
        
    elif(n==2 and x=="paper"):
        print("Game Draw")
        
    elif(n==3 and x=="scissor"):
        print("Game Draw")
        
    elif(n==1 and x=="scissor"):
        us=us+1
        print("user score",us)
        
    elif(n==2 and x=="rock"):
        us=us+1
        print("user score",us)
        
    elif(n==3 and x=="paper"):
        us=us+1
        print("user score",us)
        
    elif(n==1 and x=="paper"):
        cs=cs+1
        print("computer score",cs)
    
    elif(n==2 and x=="scissor"):
        cs=cs+1
        print("computer score",cs)
        
    elif(n==3 and x=="rock"):
        cs=cs+1
        print("computer score",cs)
        
if(us>cs):                                               #*
    print("User Wins with score",us)
    
elif(cs>us):
    print("computer wins with score",cs)
    
else:
    print("Match Draw")
    
        
        
#SOME MORE APIS

# Program to fetch joke data using free API

import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

data = response.json()

print("Joke:")
print(data["setup"])
print(data["punchline"])