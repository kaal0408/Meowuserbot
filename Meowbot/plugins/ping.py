import datetime

from . import *


@bot.on(mew_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(Meow):
    if Meow.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(Meow, "`⊰ քɨռɢ ⊱´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"•࿙𝖯ØᏁᎶ࿙•\n\n    🌺  `{ms}`\n    🌺  __**Oառҽʀ**__ **:**  {mew_mention}"
    )


CmdHelp("ping").add_command(
    "ping", None, "Checks the ping speed of your ℳêøաɮøƚ"
).add_warning("✅ Harmless Module").add()

# Meowbot
