from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

# -------------------------------------------------------------------------------

mew_pic = Config.ALIVE_PIC or "https://telegra.ph/file/3c2932815330a143fa1a8.png"
alive_c = f"__**😺😺ʍɛօա ɨs օռʟɨռɛ😺😺**__\n\n"
alive_c += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
alive_c += f"╠⟪Øωηєя⟫╣  ⊱ 【 {mew_mention} 】\n\n"
alive_c += f"┏━━━━━━━━━━━━━━━━━━━\n"
alive_c += f"┣⧼• тεℓεтнση  ⊱  `[version](1.0)\n"
alive_c += f"┣⧼• мεσω        ⊱  __**{mew_ver}**__\n"
alive_c += f"┣⧼• sυ∂σ           ⊱ `{is_sudo}`\n"
alive_c += f"┣⧼• cнαηηεℓ     ⊱  {mew_channel}\n"
alive_c += f"┣⧼• ℓιcεηsε     ⊱ (Meow)[GitHub.com/TeamMew]\n"
alive_c += f"┣⧼• υρтιмε      ⊱ `{uptime}`\n"
alive_c += f"┗━━━━━━━━━━━━━━━━━━━\n"
# -------------------------------------------------------------------------------


@bot.on(mew_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(Meow):
    if Meow.fwd_from:
        return
    await Meow.get_chat()
    await Meow.delete()
    await bot.send_file(Meow.chat_id, mew_pic, caption=alive_c)
    await Meow.delete()


msg = f"""
**✨ ʍɛօա ιѕ σиℓιиє ✨**
{Config.ALIVE_MSG}
**🌹 Meow 𝚂𝚝𝚊𝚝𝚞𝚜 🌹**
**тєℓєтнσи:**  `{version}`
**ℳêøա    :**  **{mew_ver}**
**υρтιмє    :**  `{uptime}`
**αвυѕє     :**  **{abuse_m}**
**ѕυ∂σ        :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME


@bot.on(mew_cmd(pattern="meow$"))
@bot.on(sudo_cmd(pattern="meow$", allow_sudo=True))
async def mew_a(event):
    try:
        Meow = await bot.inline_query(botname, "alive")
        await Meow[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
    "alive", None, "Shows the Default Alive Message"
).add_command("Meow", None, "Shows Inline Alive Menu with more details.").add_warning(
    "✅ Harmless Module"
).add()
