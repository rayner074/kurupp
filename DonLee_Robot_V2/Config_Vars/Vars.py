# (c) [Muhammed] @PR0FESS0R-99
# (s) @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import os
import time
from DonLee_Robot_V2 import Text

class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN") 
    USER_SESSION = os.environ.get("SESSION_FILE")


    # store 
    DATABASE = os.environ.get("DATABASE_URI")   
    # from forces subscriber );
    FORCE_SUB_TEXT = os.environ.get("FORCE_TEXT", Text.FORCE_SUB_TEXT)
    FORCE_CHANNEL = os.environ.get("FORCE_CHANNEL", "all_links8")
    # seplling mode
    SPELLING_MODE = os.environ.get("SPELLING_MODE_TEXT", Text.SPELLING_TEXT)
    # from Bot Deploying User
    DEV_ID = set(int(x) for x in os.environ.get("DEV_ID1", "2028425293").split())
    DEV_NAME = os.environ.get("DEV_NAME", "rayner74")
    OW_ID = int(os.environ.get("DEV_ID2", "2028425293"))
    DEV_USERNAME = os.environ.get("DEV_USERNAME", "rayner74")
    # from file caption
    CAPTION_BOLD_OR_MONO = os.environ.get("FILE_CAPTION", "mono")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", Text.FILECAPTION)

    # from start, help, about, settings (random pics)
    PHOTO = os.environ.get("PHOTOS", "https://telegra.ph/file/33e070a63186b01afb488.jpg").split()

    # bot or user
    USE_AS_BOT = True

    # download media
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY","./DOWNLOADS/")

    # User
    MAX_USER = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/") 
    MAX_SELECT_LEN = 100
    TG_MAX_SELECT_LEN = int(MAX_SELECT_LEN)
    SUDO_USERS = list(MAX_USER)
    SUDO_USERS.append(OW_ID)
    SUDO_USERS = list(set(SUDO_USERS))

    # from welcome
    name_button_welcome = "📣 All Links 📣"
    WELCOME_BUTTON_NAME = os.environ.get("WELCOME_BUTTON_NAME", name_button_welcome)
    welcome_text = "𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖡𝗋𝗈𝗍𝗁𝖾𝗋"
    CUSTOM_WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
    CUSTOM_WELCOME = os.environ.get("WELCOME_ENABLE_OR_DISABLE", "on").lower()

    # from bot ):
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Donlee_Robot")
    BOT_NAME = os.environ.get("DONLEE_ROBOT_V2", "FLES")

    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
    BUTTON_MODE = os.environ.get("FILE_BUTTONS", "single").lower()
    
    # network time (Indian)
    Up_Time = time.time()
