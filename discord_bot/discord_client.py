import discord


class DiscordBot(discord.Client):

    def __init__(self, reddit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._reddit = reddit

    async def on_ready(self):
        print(f"Bot has logged in as {client.user}.")

    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        msg = str(message.content)
        print(f"<{message.channel.name}> {username}: {msg}")

        if message.author == client.user:  # ignore self-reply
            return
        
        if message.channel.name == "memes":
            if msg[0:2] == "!m":
                try:
                    subreddit = msg.split()[1]
                except IndexError:
                    await message.channel.send("please specify a subreddit.")
                    return
                await message.channel.send(
                    self._reddit.generate_meme(subreddit)
                )
                return
            elif msg == "!help":
                await message.channel.send("How to use:\n!m <subreddit-name>")

        if msg.lower() == "hello":
            await message.channel.send(f"Hello {username} :)\nwanna see a meme?")
            return
