# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "10299822"))
API_HASH = os.environ.get("API_HASH", "bce95faccfe6248103f572732ea64e27")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5931484630:AAFDph-1OJ6z4wba9Fa7WFkIpFEY22LKkg0")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6010227382")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://amrobots:amrobots@cluster0.e3hn16i.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6010227382")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001527701055")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "amrobots_bots") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/03691465baa774e46506d.mp4') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
