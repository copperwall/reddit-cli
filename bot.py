#!/usr/bin/env python

import sys
import praw
import subprocess

# Create Reddit object
reddit = praw.Reddit(user_agent='Oppertest')

print('''Welcome to Reddit CLI!
Please enter a subreddit to be shown the current top 10 posts\n\n''')

input_subreddit = input("Reddit CLI> ")

# Grab top 10 submissions from subreddit
submissions = reddit.get_subreddit(input_subreddit).get_hot(limit=10)
urls = []
submission_index = 1

# Print information from top 10 submissions 
print("\n=== Top 10 posts from r/" + input_subreddit + " ===\n")
print("# :: Upvote/Downvotes :: Title")
print("______________________________")

for submission in submissions:
   print(str(submission_index) + " :: " + str(submission))
   urls.append(submission.url)
   submission_index += 1

print("\n")

# Prompt user to select submission to view
while True:
   print("Enter submission number to read, or press enter to exit... ")
   post_number = input("Reddit CLI> ")

   if post_number.isdigit():
      subprocess.call(['w3m', urls[int(post_number) - 1]])
   else:
      break

sys.exit()
