import praw
import prawcore
import random

# read-only instance
user_agent = praw.Reddit(client_id="XXXXXX", 
                        client_secret="XXXXXX", 
                        user_agent="XXXXXX")


def generate_meme(subreddit):

    valid_meme_subs = ["memes", "meme", "dankmemes", "funny", "wholesomememes", "196"]
    if subreddit not in valid_meme_subs:
        return "please specify a valid memes subreddit such as 'memes' or 'dankmemes' etc.."

    try:
        subreddit = user_agent.subreddit(subreddit)
        posts = list(subreddit.hot())
    except prawcore.exceptions.Redirect:
        return "subreddit not found."
    except prawcore.exceptions.ResponseException:
        exit("invalid reddit client_id or client_secret.")
    except prawcore.exceptions.RequestException:
        exit("reddit user_agent cannot be empty.")
        
    else:
        try:
            while 1:
                post = random.choice(posts)
                if post.score >= 1000:  # get a meme with 1k upvotes or more
                    break
        except IndexError:
            return "subreddit has no posts."
        return f"{post.title}\n{post.url}"


if __name__ == "__main__":  # test
    print(generate_meme("memes"))