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
    # Bootstrap'ten app ve userbot alıyoruz
    app, api, userbot, platforms = init_all()

    # String kontrol
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "String Session Not Filled. Please fill a Pyrogram session."
        )
        raise SystemExit(1)

    await sudo()

    # Banlı kullanıcıları yükle
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    # Bot başlat
    await app.start()

    # Pluginleri yükle
    for module in ALL_MODULES:
        importlib.import_module(f"TEAMZYRO.plugins.{module}")

    LOGGER("TEAMZYRO.plugins").info("All Features Loaded ✅")

    await userbot.start()

    # Voice Call sistemi başlat
    await ZYRO.start()

    try:
        await ZYRO.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except Exception:
        LOGGER("TEAMZYRO").error(
            "Voice chat aktif değil. Log grubunda voice chat başlat."
        )

    await ZYRO.decorators()

    LOGGER("TEAMZYRO").info("ZYRO Music Bot Started Successfully 🎵")

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("TEAMZYRO").info("Bot stopped.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
