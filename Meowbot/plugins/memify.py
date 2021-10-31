import os
import shutil

import cv2

from . import *

path = "./mewmify/"
if not os.path.isdir(path):
    os.makedirs(path)


@bot.on(mew_cmd(pattern="mmf ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mmf ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(
            event,
            "You need to reply to an image with .mmf` 'text on top' ; 'text on bottom'",
        )
        return
    await eor(event, "🤪 **Memifying...**")
    reply = await event.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs)
    tal, semx = img.read()
    cv2.imwrite("mew.webp", semx)
    text = event.pattern_match.group(1)
    webp_file = await draw_meme_text("mew.webp", text)
    await event.client.send_file(
        event.chat_id, webp_file, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    shutil.rmtree(path)
    os.remove("mew.webp")
    os.remove(webp_file)


@bot.on(mew_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def sed(Meowmew):
    if Meowmew.fwd_from:
        return
    if not Meowmew.reply_to_msg_id:
        await eod(
            Meowmew,
            "You need to reply to an image with .mms` 'text on top' ; 'text on bottom'",
        )
        return
    await eor(Meowmew, "🤪 **Memifying...**")
    reply = await Meowmew.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs)
    tal, semx = img.read()
    cv2.imwrite("mew.webp", semx)
    text = Meowmew.pattern_match.group(1)
    photo = await draw_meme("mew.webp", text)
    await Meowmew.client.send_file(
        Meowmew.chat_id, photo, reply_to=Meowmew.reply_to_msg_id
    )
    await Meowmew.delete()
    shutil.rmtree(path)
    os.remove("mew.webp")
    os.remove(photo)


@bot.on(mew_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(mew):
    Meow = mew.pattern_match.group(1)
    if not Meow:
        if mew.is_reply:
            (await mew.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(mew, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(mew, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(Meow))}")
    if troll:
        await mew.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                mew.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
        await eod(mew, "Error 404:  Not Found")


@bot.on(mew_cmd(pattern="gg(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gg(?: |$)(.*)", allow_sudo=True))
async def nope(mew):
    Meow = mew.pattern_match.group(1)
    if not Meow:
        if mew.is_reply:
            (await mew.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(mew, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(mew, "Doge need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(Meow))}")
    if troll:
        await mew.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                mew.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
        await eod(mew, "Error 404:  Not Found")


CmdHelp("memify").add_command(
    "mmf",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in sticker format.",
    "mmf <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "mms",
    "<reply to a img/stcr/gif> <upper text> ; <lower text>",
    "Memifies the replied image/gif/sticker with your text and sends output in image format.",
    "mms <reply to a img/stcr/gif> hii ; hello",
).add_command(
    "doge", "<text>", "Makes A Sticker of Doge with given text."
).add_command(
    "gg", "<text>", "Makes google search sticker."
).add_info(
    "Make Memes on telegram 😉"
).add_warning(
    "✅ Harmless Module."
).add()
