import importlib
import logging
import os
import sys
from pathlib import Path

from Meowbot import *
from Meowbot.config import *
from Meowbot.helpers import *
from Meowbot.utils import *

# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from Meowbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import Meowbot.utils

        path = Path(f"Meowbot/plugins/{shortname}.py")
        name = "Meowbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("MeowBot - Successfully imported " + shortname)
    else:
        import Meowbot.utils

        path = Path(f"Meowbot/plugins/{shortname}.py")
        name = "Meowbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = Meowbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.Meowbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_mew = delete_mew
        mod.eod = delete_mew
        mod.Var = Config
        mod.admin_cmd = mew_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = Meowbot.utils
        sys.modules["userbot"] = Meowbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = Meowbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["Meowbot.plugins." + shortname] = mod
        LOGS.info("⚡ ℳêøաɮøƚ ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"Meowbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


# Meowbot
