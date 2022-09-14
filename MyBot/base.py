import os
import discord

from consts import COMMAND_PREFIX
from .mybot import MyBot
from dotenv import load_dotenv

load_dotenv()

COMMAND_PREFIX = os.getenv('PREFIX','!')

app = MyBot(command_prefix=COMMAND_PREFIX,intents=discord.Intents.all())

@app.event
async def on_ready():
    print('Done')
    if not app.increase_hungry.is_running():
        app.increase_hungry.start()
    if not app.announce_hungry.is_running():
        app.announce_hungry.start()
    await app.change_presence(status=discord.Status.online, activity=None)
