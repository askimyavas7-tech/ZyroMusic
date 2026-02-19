import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TEAMZYRO.logging import LOGGER
from TEAMZYRO.bootstrap import init_all

from TEAMZYRO.core.call import ZYRO
from TEAMZYRO.misc import sudo
from TEAMZYRO.plugins import ALL_MODULES
from TEAMZYRO.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # ✅ app ve userbot artık bootstrap'ten geliyor
    app, api, userbot, platforms = init_all()

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("String Session Not Filled. Please fill a Pyrogram session.")
        raise SystemExit(1)

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    # ✅ plugin import yolu düzeltildi
    for all_module in ALL_MODULES:
        importlib.import_module(f"TEAMZYRO.plugins.{all_module}")

    LOGGER("TEAMZYRO.plugins").info("All Features Loaded...")
    await userbot.start()

    await ZYRO.start()
    try:
        await ZYRO.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("TEAMZYRO").error("Please start your log group voice chat. Bot stopping...")
        raise SystemExit(1)
    except Exception:
        pass

    await ZYRO.decorators()

    LOGGER("TEAMZYRO").info("ZYRO Music Bot Started ✅")

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TEAMZYRO").info("Bot stopped.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
