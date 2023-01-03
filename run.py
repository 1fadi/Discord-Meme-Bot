import discord
from discord.errors import LoginFailure
from discord_bot import DiscordBot, RedditScraper
import sys
import os
from dotenv import load_dotenv


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    user_agent = RedditScraper(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )
    client = DiscordBot(
        intents=discord.Intents.all(),
        reddit=user_agent
    )
    try:
        client.run(os.environ.get('DISCORD_TOKEN', ''))
    except LoginFailure:
        sys.exit("Token not valid.")


if __name__ == "__main__":
    main()
