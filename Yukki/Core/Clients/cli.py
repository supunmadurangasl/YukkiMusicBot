from config import API_HASH, API_ID, BOT_TOKEN, STRING
from pyrogram import Client
from pytgcalls import PyTgCalls

app = Client(
    "YukkiMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

bot = STRING(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

userbot = PyTgCalls(bot, overload_quiet_mode=True)
