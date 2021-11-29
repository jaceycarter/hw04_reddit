# HW 04:Reddit Bot

I used Python and the PRAW API to create a Reddit bot named jcar_bot. I programmed my bot to post comments supporting John McCain as a maverick politician. 

## My Favorite Thread

My favorite [thread](https://www.reddit.com/r/BotTown2/comments/r4l546/its_always_the_motivational_speakers_with_the_red/) was an interaction with another bot regarding The Bachelorette.

<img width="869" alt="Screen Shot 2021-11-28 at 8.54.23 PM.png" src="https://github.com/jaceycarter/hw04_reddit/blob/main/Screen%20Shot%202021-11-28%20at%208.54.23%20PM.png">

The intial comment is referring to a contestant on The Bachelorette who's a motivational speaker and raises many red flags to some viewers. This bot replies with a comment seeming motivational, which raises a red flag!!!

## My Output

Below is the output from running `bot_counter.py` for my bot, _jcar_bot_:
```
Jaceys-MacBook-Air:CS_bot jaceycarter$ python3 bot_counter.py --username=jcar_bot
Version 7.4.0 of praw is outdated. Version 7.5.0 was released Sunday November 14, 2021.
len(comments)= 668
len(top_level_comments)= 135
len(replies)= 533
len(valid_top_level_comments)= 107
len(not_self_replies)= 527
len(valid_replies)= 408
========================================
valid_comments= 515
========================================
```


**Extra Credit #4 :** Below is the output of running `extracredit4.py`. This bot created new submission posts from _r/The Bachelorette_ and posted them into the class subreddit, _r/BotTown2_. By the final iteration, the bot had generated over 200 submissions, including self-posts and URL posts.

**Extra Credit #7 :** Below is the output from running `extracredit7.py` program to upvote any comment or submission that mentioned Biden and downvote any comment or submission that mentioned Trump. I also used the TextBlob sentiment analysis library to determine the sentiment of all the posts. If the comment/submission had positive sentiment, then I upvoted it; if the comment/submission had a negative sentiment, then I downvoted it.

## Grading

**Required Tasks**

* *Task 1 :* Completed `bot.py` file | +18 Points |
* *Task 2 :* Completed GitHub repository | +2 Points |

**Optional Tasks**

* *Task 1 :* Getting at least 100 valid comments posted | +2 Points |
* *Task 2 :* Getting at least 500 valid comments posted | +2 Points |
* *Task 3 :* Getting at least 1000 valid comments posted | +0 Points |
* *Task 4 :* Making your bot create 200+ new submissions | +2 Points |
* *Task 5 :* Create an "army" of 5 bots that post 500+ valid comments each | +0 Points |
* *Task 6 :* Make your bot reply to the most highly upvoted comment | +0 Points |
* *Task 7 :* Have your bot upvote any comment or submission that mentions your favorite candidate. | +2 Points |
    * *Additional:* Use the _TextBlob_ sentiment analysis library | +2 Points |
* *Task 8 :* Use a more sophisticated algorithm for generating the text of your comments | +0 Points |

**Total Points :** I believe I should receive a 30/30 on this assignment
