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

## update
## Tweet Silently (uses return instead of print [best for python programs])
## Param: String status
## Return: String
def update(status):
    if status:
        s = api.PostUpdate(str(status))
        return s
    else:
        return "Error sending tweet"

## tweet
## Tweets a status update
## Param: String status
## Return: Void
def tweet(status):
	if(status == ""):
		print("Cannot tweet empty text")
	else:
		status = api.PostUpdate(status)
		print("You just tweeted: " + status.text)	

## unfollow
## Unfollow Someone using their username
## Param: String username
## Return: Void
def unfollow(username):
    if username:
        api.DestroyFriendship(screen_name=username)
        print("Unfollowed " + str(username))
    else:
        print("Username cannot be empty")

## follow
## Follow someone using their username
## Param: String username
## Return: Void
def follow(username):
    if username:
        api.CreateFriendship(screen_name=username)
        print("Followed " + str(username))
    else:
        print("Username cannot be empty")

## whoami
## Check your Name
## Param: none
## Return: String
def whoami():
	print("You are " + person.name)
    return str(person.name)

## username
## Check your Username/Screen Name
## Param: none
## Return: Void
def username():
        print("Your username is @" + person.screen_name)

## sendDM
## Send a DM
## Param: String to - Username of User
##        String message - Message to be sent
## Return: Void
def sendDM(to, message):
   if(to == ""):
      return "You cannot send a message to an empty recepient"
   else:
      if(message == ""):
         return "Message cannot be empty"
      else:
         api.PostDirectMessage(screen_name=to, text=message)
         print("DM Sent to " + to)

## getDM
## Retrieve DMs
## Param: none
## Return: Void
def getDM():
   dms = api.GetDirectMessages()
   if dms:
      for dm in dms:
         sender = dm.sender.name
         sender_screen = dm.sender.screen_name
         text = dm.text
         date = dm.created_at
         print(sender + " (@" + sender_screen + "):")
         print("   " + text)
         print("[" + date + "]\n\n")
   else:
      return "No DMs or Error Getting them"

## followers
## Display Followers
## Param: none
## Return: Void
def followers():
    f = api.GetFollowers()
    print("Your Followers:\n\n")
    for follower in f:
        print(follower.name + " (@" + follower.screen_name + ")\n")

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


if __name__ == "__main__":
    print("You must import this to interactive Python")