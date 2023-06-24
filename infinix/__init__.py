from telethon import TelegramClient 
import logging
import time


api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"
bot_token ="6264683318:AAGKjpVhz00L6l46h-cQAWAXXDVxiw3W4tE"

bot = TelegramClient("infinix", api_id, api_hash).start(bot_token=bot_token)
