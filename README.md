reddit-cli
==========

A CLI interface to Reddit

### Functionality

* View the top 10 submissions to a subreddit, along with their upvote/downvote breakdown
* Select one of those ten submissions and open up their link in terminal with `w3m`. (You can specify another client if you'd like)

### Proposed Functionality

* Saving favorite subreddits and showing their top N posts on startup
* Logging in and getting notifications about new or unread messages, link or comment karma
* Searching posts from certain subreddits for certain keywords
* Sending messages to other users
* Viewing comments on a post

### Dependencies

* All interaction with Reddit's API is done through PRAW (Python Reddit Api Wrapper)
* This is written in Python3
* This requires a terminal browser to view links. I currently have `w3m` hardcoded in, but if you'd like to change it to `Lynx` or something else, be my guest.

### Disclaimer

I realize that this could be much prettier, but I currently know absolutely nothing about ncurses. I'm going to focus on features that deal with the API first, and then maybe visit UI.
