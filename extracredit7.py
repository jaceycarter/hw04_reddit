import praw
from praw.reddit import Subreddit
from textblob import TextBlob
import random
import time

reddit = praw.Reddit('bot')

submission_url = 'https://www.reddit.com/r/BotTown2/comments/r4nxo5/how_to_meet_americas_climate_goals_5_policies_for/'
submission = reddit.submission(url=submission_url)


while True: 

    submission.comments.replace_more(limit=None)
    total_comments = []
    total_comments = submission.comments.list()

    if 'trump' in submission.title.lower():
        submission.downvote()
        print('submission upvote')
    if 'biden' in submission.title.lower():
        submission.upvote()
        print('submission downvote')
    if 'trump' in submission.title.lower():
        submission.upvote()
        print('submission upvote')
    if 'biden' in submission.title.lower():
        submission.downvote()
        print('submission downvote')


    upvoted = 0
    downvoted = 0
    for comment in total_comments:
        words = TextBlob(comment.body.lower())
        polarity = words.sentiment.polarity
        if 'trump' in comment.body.lower() and polarity > 0:
            comment.downvote()
            downvoted +=1
        if 'biden' in comment.body.lower() and polarity > 0:
            comment.upvote()
            upvoted += 1
        if 'trump' in comment.body.lower() and polarity < 0:
            comment.upvote()
            upvoted += 1
        if 'biden' in comment.body.lower() and polarity < 0:
            comment.downvote()
            downvoted += 1
        
    print('Total upvoted =', upvoted)
    print('Total downvoted =', downvoted)


    hottest_submissions = []
    subreddit = reddit.subreddit("BotTown2")
    for submission in subreddit.hot(limit=None):
        hottest_submissions.append(submission)
    submission = random.choice(hottest_submissions)
    print('next submission title=', submission.title)
  
    time.sleep(1)
