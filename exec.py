import os

from MyBot.base import app
from MyBot.conversations import *
from MyBot.messages.conversations import *
from MyBot.enchant.conversations import *
from MyBot.cats.conversations import *

from dotenv import load_dotenv
load_dotenv()

def exec():
    TOKEN = os.getenv("TOKEN","")
    print("Run! Discord Server!")
    app.run(TOKEN)
    
if __name__=="__main__":
    exec()