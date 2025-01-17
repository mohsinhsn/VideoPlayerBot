

import os
import sys
import asyncio
from pyrogram import Client, idle
from config import Config
from bot.safone.nopm import User

Bot = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="bot.safone"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

Bot.start()
User.start()
print("\nVideo Player Bot Started, Join @StylishUser!")

idle()
Bot.stop()
User.stop()
print("\nVideo Player Bot Stopped, Join @StylishUser!")
