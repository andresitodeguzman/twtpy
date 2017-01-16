# TwtPy
Super lightweight twitter client for Python used for personal projects. No need for long Twitter APIs. Use Twitter in Python.

## Needed Module(s)
- Twitter-Python

## Setup
Download the repo. Install python-twitter through pip. Generate keys and tokens. Once you have the necessary keys and tokens, open auth.py and insert them.

## How to use
Start Python
```
$ python
```
Import TwtPy via tweet
```python
>>> import tweet
```
Start Using it

## Basic Usage
Check your Name
```python
>>> tweet.whoami()
```
Check your username/screen name
```python
>>> tweet.username()
```
Tweet Something
```python
>>> status = "Hello World"
>>> tweet.tweet(status)
```
Tweet Something (without explicit response)
```python
>>> status = "Hello World"
>>> tweet.update(status)
```
Search for Tweets
```python
>>> query = "Your Query Here"
>>> tweet.tweet(query)
```
See your Followers
```python
>>> tweet.followers()
```
Follow Someone
```python
>>> username = "username_here"
>>> tweet.follow(username)
```
Unfollow Someone
```python
>>> username = "username_here"
>>> tweet.unfollow(username)
```
Send a DM
```python
>>> to = "username"
>>> message = "Hi!"
>>> tweet.sendDM(to, message)
```

Get DMs (last 20 DMs Recieved)
```python
>>> tweet.getDM()
```

## Note
- Please do not rename tweet.py as twitter.py
- Get token and keys from https://dev.twitter.com and replace the values in the file.
- This will not work without token and keys.
- This is made for personal projects. Use with caution.

## Development
This is a personal project and was intended for personal use. You may fork and improve this. Report bugs if you find one.