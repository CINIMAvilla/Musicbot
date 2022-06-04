import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import GROUP_ID, ADMINS, START_MSG

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

@Client.on_message(filters.command(
"start") & filters.private)
async def start(bot, message):
  current_time = datetime.utcnow()
  uptime_sec = (current_time - START_TIME).total_seconds()
  uptime = _human_time_duration(int(uptime_sec))
    m=await message.reply_text("▰▱▱▱")
    n=await m.edit("▰▰▱▱")
    s=await n.edit("▰▰▰▱")
    o=await s.edit("▰▰▰▰")
    await o.edit(text=Config.START_MSG.format(message.from_user.mention),
         disable_web_page_preview=True,
         reply_markup = InlineKeyboardMarkup(
           [[
             InlineKeyboardButton("🎧 ᴍᴜsɪᴄ.ᴘᴀɴᴅᴀ", url="telegram.dog/musicspanda")
           ],[
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Gxneo"),
             InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
           ]]))
  
@Client.on_callback_query(filters.regex("close"))
async def close(bot, query):
  await query.message.delete()


def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

