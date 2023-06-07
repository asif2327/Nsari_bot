from telethon import TelegramClient 
import logging
import time
openai_key ="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"

api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"
bot_token ="6264683318:AAGKjpVhz00L6l46h-cQAWAXXDVxiw3W4tE"

bot = TelegramClient("ansari_123_bot", api_id, api_hash).start(bot_token=bot_token)