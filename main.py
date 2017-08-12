#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Sim Dlamini: 
# AllanGray work Exercise:
# Description: A simple program to simulate the twitter feed of users, based on who they follow. This is a rudimentary example to illustrate a simple solution to
# the problem with the given example. It is also a bit inefficient since in the last part we check all tweets posted to extract those of only users being followed by a user.
# A better solution is to add an integer index to the tweet as a kind of timestamp to make this more efficient
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



f = open('tweet.txt','r') # opening the tweet file
g = open('user.txt','r')  # opening the user file

#-----------------------------------------------#
users = {} # store uses in dictionary
tweets = [] # store tweets in a list

#-----------------------------------------------#
for line in g:
  line = line.strip()               # line strip to remove the space at the beginning and end of the file.
  line = line.split(' follows ')    # spliting the file into users and followees
  
  user = line[0]                    # first column as user
  followees = line[1].split(', ')   # Spliting the second column as follwees 
  followees.append(user)            # assuming that users follow themselves (see example scenario)
  
  if user in users.keys():          # from the dictionary, retrieve the list of usernames, and check if new user is in there or not
    users[user].update(followees)   # update entry of user with new followees
  else:
    users[user] = set()             # add user to the dictionary as key with empty set of followees
    users[user].update(followees)   # add any followers to entry
    
  for followee in followees:        # check if we have missed any users in the system
    if followee not in users.keys():# check if followee is in the dictionary of users
      users[followee] = set()       # add followee as new user to the dictionary as key with empty set of followees
      
#----------------------------------------------#

for line in f:
  line = line.strip()
  line = line.split('> ')           # split into user and their tweet
  
  user = line[0]                    # get the user name of the user that posted the tweet
  tweet = line[1]                   # get the text of the tweet
  
  tweets.append( (user, tweet) )    # append this as a pair/tuple in the tweets list
  
sorted_users = sorted(users.keys()) # sort the list of users alphabetically

for user in sorted_users:           # for each user...
  following = users[user]           # get the list of users that this user follows
  print(user)                       # print the name of the user nad setup their feed
  
  # for this user's feed...
  for pair in tweets:
    person = pair[0]                # get the name of the user in the list of tweets who has posted as tweet
    if person in following:         # if the person who has posted the tweet is being followed by this user, post the tweet
      tweet = pair[1]               # get the tweet that was posted
      print('\t@%s: %s'%(person,tweet))  # print the person and tweet as requested
      
 #-------------------------------------------#     
  
  
  