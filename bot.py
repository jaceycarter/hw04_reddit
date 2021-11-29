import praw
import random
import time
import datetime
from praw.reddit import Subreddit

# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "John McCain was an [AMERICAN] politician, statesman and [UNITED STATES] Navy officer who served as a [SENATOR] for [ARIZONA]. He served [TWO] terms in the House of Representatives and was the [REPUBLICAN] [NOMINEE] for [PRESIDENT] of the United States in the 2008 [ELECTION].",
    
    "John McCain graduated from the United States Naval Academy in [1958] and received a commission in the United States Navy. He became a naval aviator and flew ground-attacks from [AIRCRAFT] carriers. During the Vietnam [WAR], he almost [DIED] in the 1967 USS Forrestal fire.",
    
    "While on a bombing [MISSION] during Operation Rolling Thunder over Hanoi in October 1967, McCain was shot down, [SERIOUSLY INJURED], and [CAPTURED] by the North Vietnamese. John McCain was a [PRISONER] of war until 1973. He experienced episodes of [TORTURE] and refused an out-of-sequence early release.",
   
    "In [1982], McCain was [ELECTED] to the United States House of Representatives, where he served [TWO] terms. He was elected to the U.S. Senate in 1986, [SUCCEEDING] the 1964 Republican presidential nominee and [CONSERVATIVE] icon Barry Goldwater upon his retirement. McCain easily won reelection [FIVE] times.",
   
    "While generally [ADHERING] to conservative principles, McCain also gained a [REPUTATION] as a [MAVERICK] for his willingness to break from his [PARTY] on certain issues, where his stances were more [MODERATE] than those of the party's base.", 
   
    "McCain [ENTERED] the race for the Republican nomination for president in [2000] but [LOST] a heated primary season contest to Governor George W. Bush of Texas. He [SECURED] the Republican presidential nomination in 2008, [BEATING] fellow candidates Mitt Romney and Mike Huckabee, though he lost the general election to Barack Obama."
    ]

replacements = {
    'AMERICAN' : ['American', 'Canadian', 'North Korean', 'British', 'Australian'],
    'UNITED STATES' : ['United States', 'Canada', 'North Korea', 'Great Britain', 'Australia'],
    'SENATOR' : ['Representative', 'Judge', 'Senator', 'Attorney General', 'Governor'],
    'ARIZONA' : ['Arizona', 'California', 'Texas', 'New York', 'Florida', 'Nevada'],
    'TWO' : ['two', 'three', 'four', 'five', 'one'],
    'REPUBLICAN' : ['Republican', 'Independent', 'Democrat', 'Libertarian', 'Green Party'],
    'NOMINEE' : ['applicant', 'appointee', 'candidate', 'nominee', 'selectee'],
    'PRESIDENT' : ['President', 'Head of State', 'Chief of State', 'Commander in Chief', 'leader'],
    'ELECTION' : ['election', 'selection', 'appointment', 'referendum', 'vote'],
    
    '1958' : ['1998', '2000', '2021', '1965', '1999'],
    'AIRCRAFT' : ['aircraft', 'airline', 'airship', 'helicopter', 'jet', 'chopper'],
    'WAR' : ['war', 'conflict', 'warfare', 'combat', 'battle'],
    'DIED' : ['died', 'drowned', 'got killed', 'passed away', 'lost consciousness'],

    'MISSION' : ['mission', 'attack', 'assignment', 'operation', 'charge'],
    'SERIOUSLY INJURED' : ['seriously injured', 'seriously hurt', 'very wounded', 'harmed', 'mistreated'],
    'CAPTURED' : ['captured', 'imprisoned', 'trapped', 'incarcerated', 'seized', 'caught'],
    'PRISONER' : ['prisoner', 'convict', 'inmate', 'jailbird', 'detainee'],
    'TORTURE' : ['torture', 'abuse', 'torment', 'punishment', 'maltreatment'],

    '1982' : ['1982', '2000', '2021', '2001', '2041'],
    'ELECTED' : ['elected', 'nominated', 'chosen', 'appointed', 'voted'],
    'SUCCEEDING' : ['succeeding', 'advancing', 'winning', 'triumphing', 'achieving'],
    'CONSERVATIVE' : ['conservative', 'traditionalist', 'right-wing', 'unprogressive', 'orthodox'],
    'FIVE' : ['five', 'three', 'ten', 'eleven', 'seven'],

    'ADHERING' : ['adhering', 'committing', 'sticking', 'clinging', 'attaching'],
    'REPUTATION' : ['reputation', 'public image', 'recognition', 'distinction', 'name'],
    'MAVERICK' : ['maverick', 'individualist', 'nonconformist', 'free spirit', 'rebel' ],
    'PARTY' : ['party', 'caucus', 'faction', 'organization', 'group'],
    'MODERATE' : ['moderate', 'medium', 'common', 'balanced', 'fair'],

    'ENTERED' : ['entered', 'started', 'participated in', 'engaged', 'attempted'],
    '2000' : ['1900', '1919', '2001', '2021', '2031'],
    'LOST' : ['lost', 'missed', 'did not win', 'was deprived of', 'suffered the loss of'],
    'SECURED' : ['secured', 'won', 'obtained', 'acquired', 'fortified'],
    'BEATING' : ['beating', 'conquesting', 'defeating', 'getting rid of', 'vanquishing']

    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    x = random.choice(madlibs)
    for key in replacements.keys():
        x = x.replace('['+ key + ']', random.choice(replacements[key]))
    return x

reddit = praw.Reddit('bot')

submission_url = 'https://www.reddit.com/r/BotTown2/comments/r2j3n8/mccain_submission/'
submission = reddit.submission(url=submission_url)

while True:

    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

#Task 0:

    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    print('len(all Comments=',len(all_comments))


#Task 1:
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'jcar_bot':
            not_my_comments.append(comment)

    print('Comments That Aren\'t Mine =',len(not_my_comments))

    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented = ', has_not_commented)

    
#Task 2:
    if has_not_commented:
        text = generate_comment()
        submission.reply(text)

#Task 3:
    else:
        comments_without_replies = []
        for comment in not_my_comments:
                for reply in comment.replies:
                    if str(reply.author) != 'jcar_bot':
                        comments_without_replies.append(comment)
                    else:   
                        continue
            
        print('Comments Without Replies =',len(comments_without_replies))


#Task 4:

    text = generate_comment()
    
    try:
        comment = random.choice(comments_without_replies)
        comment.reply(text)
    except IndexError:
        pass
    except praw.exceptions.APIException:
        print('Comment has been deleted and will not be replied to.')


#Task 5:
    hotsubmissions = []
    for entry in reddit.subreddit('BotTown2').hot(limit=5):
        hotsubmissions.append(entry)
    submission = random.choice(hotsubmissions)
    print('Next Submission Title =', submission.title)

    time.sleep(1)
