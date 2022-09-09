#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VIVI import LOGGER, app, userbot
from VIVI.core.call import VIV
from VIVI.plugins import ALL_MODULES
from VIVI.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VIVI").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VIVI").warning(
            "Spotify Client Id & Secret not added, padh le bc abhi bhi time h ya fir gamd dede @SIXTH_H0KAGE ladki ho tabhi dena mai gay nhi ."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VIVI.plugins" + all_module)
    LOGGER("VIVI.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await VIV.start()
    try:
        await VIV.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("VIVI").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await VIV.decorators()
    LOGGER("VIVI").info("Music Bot Started Successfully, ENJOY PEEPS")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VIVI").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
