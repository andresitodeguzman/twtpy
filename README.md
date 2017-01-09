# TwtPy
Super lightweight twitter client for Python used for personal projects.

## Needed Module(s)
- Twitter-Python

## Setup
Once you have the necessary keys and tokens, open auth.py and insert them.

## How to use
Start Python
```python
python
```
Import TwtPy via tweet
```python
import tweet
```
Start Using it

## Basic Usage
Check your Name
```python
tweet.whoamI()
```
Check your username/screen name
```python
tweet.username()
```
Tweet Something
```python
status = "Hello World"
tweet.tweet(status)
```

## Note
- Please do not rename tweet.py as twitter.py
- Get token and keys from https://dev.twitter.com and replace the values in the file.
- This will not work without token and keys.
- This is made for personal projects. Use with caution.

## Development
This is a personal project and was intended for personal use. You may fork and improve this. Report bugs if you find one.