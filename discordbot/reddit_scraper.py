from praw import Reddit
from prawcore.exceptions import Redirect as RedirectException
import os
import random


class RedditScraper(Reddit):

    def generate_meme(self, subreddit):
        subreddit = self._check_subreddit(subreddit)
        if not subreddit:
            return "Subreddit not found. 404"
        if not self._sfw_subrreddit(subreddit):
            return "Whoops! I don't touch NSFW subreddits!"
        posts = self._sort_posts(subreddit)
        try:
            while True:
                post = random.choice(posts)
                if post.score >= os.environ.get(
                    'REDDIT_POST_MIN_UPVOTES', 1000
                ):
                    break
        except IndexError:
            return "subreddit doesn't have any post."
        return f"{post.title}\n{post.url}"

    def _check_subreddit(self, subreddit):
        subreddit = self.subreddit(subreddit)
        try:
            subreddit.title  # test to see if subreddit exists
        except RedirectException:
            return False
        else:
            return subreddit

    def _sort_posts(self, subreddit):
        return list(subreddit.hot())

    def _sfw_subrreddit(self, subreddit):
        return subreddit.over18 is False


if __name__ == "__main__":  # test
    user_agent = RedditScraper(
        client_id=os.environ.get('REDDIT_CLIENT_ID', ''),
        client_secret=os.environ.get('REDDIT_CLIENT_SECRET', ''),
        user_agent=os.environ.get('REDDIT_USER_AGENT', '')
    )
    print(user_agent.generate_meme("memes"))
