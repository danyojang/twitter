#!/usr/bin/python

# This program will print the prompt the user for a Twitter username and 
# print the number of followers and the number of followers of each follower

import tweepy

# will print up to MAX_FOLLOWERS followers and their followers count
MAX_FOLLOWERS = 50

# authentication info
consumer_key = 'gtTRVAy4u8969aIV8C4ZxwZfD'
consumer_secret = '6eEA8ZYb9VPTD35kN8YYf9OsqF1yvx3bL5YDKOpBh9ffxYSZDE'
access_token = '569880785-AGgDbbc5Pt3WneBhPXJOYLGyi21xTcNo1VME8AcI'
access_token_secret = 'cDLLw0203s8IgP1uJizAyjfuXBnOCvNxIoM1Saems0W27'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# for manual input user_id
# user_id = 'lokeshd'

# prompt for user_id in console
user_id = raw_input("Please enter a username: ")

# prints the description of the program
def printProgramDescription():
	print 'This program will print the given Twitter username and print the '\
			'number of followers and the number of followers of each follower'

# Prints the user's screen name and number of followers.
# In addition, for each follower (maximum of MAX FOLLOWERS), prints the 
# screen name and the number of followers.
def get_twitter_users(user_id):
	followers = []
	print_num_of_followers(user_id)
	for follower in tweepy.Cursor(api.followers, id = user_id).items(MAX_FOLLOWERS):
		followers.append(follower)
	
	# only works for 20 followers
	# followers = api.followers(id = user_id)

	print "Followers:"
	for user in followers:
		print_num_of_followers(user.id_str)

# Prints the user's screen name and followers count.
def print_num_of_followers(user_id):
	user = api.get_user(id = user_id)
	print "Username: \t\t", user.screen_name
	print "Number of followers: \t", user.followers_count, '\n' 

printProgramDescription();
get_twitter_users(user_id);
