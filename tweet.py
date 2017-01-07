#		Twitter Python Connection
#
# Andresito de Guzman
#
import twitter

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""
    
api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
       )

person = api.VerifyCredentials()

## Tweet
def tweet(status):
	if(status == ""):
		print("Cannot tweet empty text")
	else:
		status = api.PostUpdate(status)
		print("You just tweeted: " + status.text)	

## Check your Name
def whoami():
	print("You are " + person.name)

## Check your Username/Screen Name
def username():
	print("Your username is @" + person.screen_name)