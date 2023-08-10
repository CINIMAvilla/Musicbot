import os
from os import getenv

GROUP_ID = int(getenv("GROUP_ID", None))
ADMINS = [id for id in getenv("ADMINS").split(" ")]
SESSION_NAME = getenv("RiyaMusicBot", "session")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
START_MSG = getenv("START_MSG")
