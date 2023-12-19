#Github.com/devgaganin

from pyrogram import Client, filters
from pyrogram.types import Message

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging
import time
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120" #config("API_ID", default=None, cast=int)
API_HASH = "1fda88a5d1de46058a4791c78bce198e" #config("API_HASH", default=None)
BOT_TOKEN = "6468925244:AAGSX6vcSCegLPU0NaUOo7ghT0CNirmFQ5A" #config("BOT_TOKEN", default=None)
SESSION = "BAGN3_AAFo_meT02xKompypVDBUavS3m3mVdey235WQW8br1DcqSR_ncTQqCQIvwGQRYXHGeqJvBfRFkqq5ND99JfLRhsqFAdg_WJ76IkYYSTAFmXY0GKUgmAX5Fth28KIRBgHjj2uzBdC3JYpg5eDIm-5AoB2bgRIZHEZd9TH76Rqkz1zD9Ib4c06usdTzGAI5DJi14s_p0lbBI1bjm3LFm8OBor12wJgKuxepMk-oP_TX_u2_RitUAgq03Pea8HR0p87J0kyBgdLNCEaTh7yqu6uBvXKCh8o3AbTzRcNdlSSABtQbgyq8yd1j74qJL3lY0QcApTmetfK-LPnaMxPY4PVmYNwAAAAGEi3zNAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "6876018655" #config("AUTH", default=None)
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
