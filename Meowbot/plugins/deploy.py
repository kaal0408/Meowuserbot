
from telethon import events

import asyncio


from Meowbot import CMD_HELP

@borg.on(admin_cmd(pattern=r"deploy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Deploying...")

    animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (kaal0408/Meowbot)**",
            "**Build started by user** **{DEFAULTUSER}**",
            "**Deploy** `535a74f0` **by user** **{MY BOSS}**",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:Meowbot:Logged in as 557667062__",
            "__INFO:Meowbot:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
            
            
            
CMD_HELP.update(
    {
        "deploy": ".deploy"
        "\nUsage show fake animation of deploy "
    }
)
