"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
from telethon import events
import os
import requests
import json


@borg.on(admin_cmd("dns (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await event.edit("i can't seem to find {} on the internet".format(input_str))


@borg.on(admin_cmd("shorten (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Your shortened URL:- {} ".format(response_api))
    else:
        await event.edit("something w3nt wrong. please try again later.")


@borg.on(admin_cmd("unshort (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await event.edit("Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"]))
    else:
        await event.edit("Input URL {} returned status_code {}".format(input_str, r.status_code))
