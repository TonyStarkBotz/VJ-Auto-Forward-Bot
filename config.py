from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
      API_ID = int(getenv("API_ID", "20389440"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7373996407:AAHqyhXEGhVILwmIA8oFQtXpQ8CQJaPzGZY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002189912442:-1002126324229").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
