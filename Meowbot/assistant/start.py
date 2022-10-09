from telethon ipmort events
from telethon import Button

@tgbot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await tgbot.send_message(event.chat_id, "Welcome to Meow Tg UserBot...\nHow can i help you Choose", buttons=[
    [Button.url("My Github", url="https://github.com/kaal0408/Meowuserbot"), 
     Button.url("My Owner", url="https://github.com/kaal0408")
    ],
    ])
