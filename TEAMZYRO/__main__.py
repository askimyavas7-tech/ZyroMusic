import asyncio
import importlib

from pyrogram import idle

import config
from TEAMZYRO.logging import LOGGER
from TEAMZYRO.bootstrap import init_all

from TEAMZYRO.core.call import ZYRO
from TEAMZYRO.misc import sudo
from TEAMZYRO.plugins import ALL_MODULES
from TEAMZYRO.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    app, api, userbot = init_all()

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER.error("String Session Not Filled.")
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

    for module in ALL_MODULES:
        importlib.import_module(f"TEAMZYRO.plugins.{module}")

    LOGGER.info("All Plugins Loaded ✅")

    await userbot.start()

    await ZYRO.start()

    try:
        await ZYRO.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except Exception:
        LOGGER.warning("Voice chat not active.")

    await ZYRO.decorators()

    LOGGER.info("ZYRO Bot Started Successfully 🎵")

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER.info("Bot Stopped.")


if __name__ == "__main__":
    asyncio.run(init())
