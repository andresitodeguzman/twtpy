# TwtPy
#		
# Andresito de Guzman
#
import twitter
import auth
    
api = twitter.Api(
        consumer_key=auth.consumer_key,
        consumer_secret=auth.consumer_secret,
        access_token_key=auth.access_token_key,
        access_token_secret=auth.access_token_secret
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

## Search
def search(query):
    if(query == ""):
        print("Cannot search empty query")
    else:
            q = api.GetSearch(query)
            print("Here are the results for " + query + ":\n\n")
            for status in q:
                name = status.user.name
                username = status.user.screen_name
                text = status.text
                print(name + " (" + username + "): " + text + "\n")