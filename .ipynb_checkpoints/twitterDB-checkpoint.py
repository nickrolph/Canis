import os
import requests
import json
import time
from pprint import pprint
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

consumer_key = "XPxx7q10newFt0aBAmUbgz23S"  # Add your API key here
consumer_secret = "GUljnxIUhuE2svMrbzfV7uQBsBRv2r6VVU0GPZ53zJloqFyn8k"  # Add your API secret key here

stream_url = "https://api.twitter.com/labs/1/tweets/stream/filter"
rules_url = "https://api.twitter.com/labs/1/tweets/stream/filter/rules"

sample_rules = [
  { 'value': 'dog has:images', 'tag': 'dog pictures' },
  { 'value': 'cat has:images -grumpy', 'tag': 'cat pictures' },
]

# Gets a bearer token
class BearerTokenAuth(AuthBase):
  def __init__(self, consumer_key, consumer_secret):
    self.bearer_token_url = "https://api.twitter.com/oauth2/token"
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.bearer_token = self.get_bearer_token()

  def get_bearer_token(self):
    response = requests.post(
      self.bearer_token_url,
      auth=(self.consumer_key, self.consumer_secret),
      data={'grant_type': 'client_credentials'},
      headers={'User-Agent': 'TwitterDevFilteredStreamQuickStartPython'})

    if response.status_code is not 200:
      raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" % (response.status_code, response.text))

    body = response.json()
    return body['access_token']

  def __call__(self, r):
    r.headers['Authorization'] = f"Bearer %s" % self.bearer_token
    r.headers['User-Agent'] = 'TwitterDevFilteredStreamQuickStartPython'
    return r


def get_all_rules(auth):
  response = requests.get(rules_url, auth=auth)

  if response.status_code is not 200:
    raise Exception(f"Cannot get rules (HTTP %d): %s" % (response.status_code, response.text))

  return response.json()


def delete_all_rules(rules, auth):
  if rules is None or 'data' not in rules:
    return None

  ids = list(map(lambda rule: rule['id'], rules['data']))

  payload = {
    'delete': {
      'ids': ids
    }
  }

  response = requests.post(rules_url, auth=auth, json=payload)

  if response.status_code is not 200:
    raise Exception(f"Cannot delete rules (HTTP %d): %s" % (response.status_code, response.text))

def set_rules(rules, auth):
  if rules is None:
    return

  payload = {
    'add': rules
  }

  response = requests.post(rules_url, auth=auth, json=payload)

  if response.status_code is not 201:
    raise Exception(f"Cannot create rules (HTTP %d): %s" % (response.status_code, response.text))

def stream_connect(auth):
  response = requests.get(stream_url, auth=auth, stream=True)
  for response_line in response.iter_lines():
    if response_line:
      pprint(json.loads(response_line))

bearer_token = BearerTokenAuth(consumer_key, consumer_secret)

def setup_rules(auth):
  current_rules = get_all_rules(auth)
  delete_all_rules(current_rules, auth)
  set_rules(sample_rules, auth)


# Comment this line if you already setup rules and want to keep them
setup_rules(bearer_token)

# Listen to the stream.
# This reconnection logic will attempt to reconnect when a disconnection is detected.
# To avoid rate limites, this logic implements exponential backoff, so the wait time
# will increase if the client cannot reconnect to the stream.
timeout = 0
while True:
  stream_connect(bearer_token)
  sleep(2 ** timeout)
  timeout += 1













# #https://towardsdatascience.com/streaming-twitter-data-into-a-mysql-database-d62a02b050d6
#
# import mysql.connector
# from mysql.connector import Error
# import tweepy
# import json
# from dateutil import parser
# import time
# import os
# import subprocess
#
# #importing file which sets env variable
# subprocess.call("./settings.sh", shell = True)
#
#
# consumer_key = os.environ['CONSUMER_KEY']
# consumer_secret = os.environ['CONSUMER_SECRET']
# access_token = os.environ['ACCESS_TOKEN']
# access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
# password = os.environ['PASSWORD']
#
#
# def connect(username, created_at, tweet, place , location):
# 	"""
# 	connect to MySQL database and insert twitter data
# 	"""
# 	try:
# 		con = mysql.connector.connect(host = 'localhost',
# 		database='twitterDB', user='nickrolph', password = password, charset = 'utf8')
#
#
# 		if con.is_connected():
# 			"""
# 			Insert twitter data
# 			"""
# 			cursor = con.cursor()
# 			# twitter, golf
# 			query = "INSERT INTO TweetData (username, created_at, tweet, place, location) VALUES (%s, %s, %s, %s, %s, %s)"
# 			cursor.execute(query, (username, created_at, tweet, place, location))
# 			con.commit()
#
#
# 	except Error as e:
# 		print(e)
#
# 	cursor.close()
# 	con.close()
#
# 	return
#
#
# # Tweepy class to access Twitter API
# class Streamlistener(tweepy.StreamListener):
#
#
# 	def on_connect(self):
# 		print("You are connected to the Twitter API")
#
#
# 	def on_error(self):
# 		if status_code != 200:
# 			print("error found")
# 			# returning false disconnects the stream
# 			return False
#
# 	"""
# 	This method reads in tweet data as Json
# 	and extracts the data we want.
# 	"""
# 	def on_data(self,data):
#
# 		try:
# 			raw_data = json.loads(data)
#
# 			if 'text' in raw_data:
#
# 				username = raw_data['user']['screen_name']
# 				created_at = parser.parse(raw_data['created_at'])
# 				tweet = raw_data['text']
#
# 				if raw_data['place'] is not None:
# 					place = raw_data['place']['country']
# 					print(place)
# 				else:
# 					place = None
#
#
# 				location = raw_data['user']['location']
#
# 				#insert data just collected into MySQL database
# 				connect(username, created_at, tweet, place, location)
# 				print("Tweet colleted at: {} ".format(str(created_at)))
# 		except Error as e:
# 			print(e)
#
#
# if __name__== '__main__':
#
# 	# # #Allow user input
# 	# track = []
# 	# while True:
#
# 	# 	input1  = input("what do you want to collect tweets on?: ")
# 	# 	track.append(input1)
#
# 	# 	input2 = input("Do you wish to enter another word? y/n ")
# 	# 	if input2 == 'n' or input2 == 'N':
# 	# 		break
#
# 	# print("You want to search for {}".format(track))
# 	# print("Initialising Connection to Twitter API....")
# 	# time.sleep(2)
#
# 	# authentification so we can access twitter
# 	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_token_secret)
# 	api =tweepy.API(auth, wait_on_rate_limit=True)
#
# 	# create instance of Streamlistener
# 	listener = Streamlistener(api = api)
# 	stream = tweepy.Stream(auth, listener = listener)
#
# 	track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
# 	#track = ['nba', 'cavs', 'celtics', 'basketball']
# 	# choose what we want to filter by
# 	stream.filter(track = track, languages = ['en'])
