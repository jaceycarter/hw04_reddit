import praw
import time

reddit = praw.Reddit('bot')

count = 0
for submission in reddit.subreddit("TheBachelorette").hot(limit=300):
    a = submission.title
    b = submission.url
    try:
        reddit.subreddit('BotTown2').submit(a, url=b)
    except praw.exceptions.RedditAPIException:
        pass
    count += 1
    print('Reposted comment count = ', count)
    time.sleep(1)


    
