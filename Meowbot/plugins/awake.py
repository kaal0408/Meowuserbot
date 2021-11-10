
"""Check if Meowbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


mew_pic = Config.ALIVE_PIC or "https://telegra.ph/file/3c2932815330a143fa1a8.png"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = "Meow is online"
   ALIVE_MESSAGE = "**🔱Meow Meowbot IS Awake🔱 \n\n\n**"
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"`Telethon: TELETHON-1.19.0 \n\n`"
   ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
   ALIVE_MESSAGE += f"`Support Channel` : @Murat_30_God \n\n"
   ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
