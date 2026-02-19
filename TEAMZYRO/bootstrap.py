from TEAMZYRO.core.bot import ZYRO
from TEAMZYRO.core.dir import dirr
from TEAMZYRO.core.git import git
from TEAMZYRO.core.userbot import Userbot
from TEAMZYRO.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from TEAMZYRO.logging import LOGGER


def init_all():
    dirr()

    # Git upstream zorunlu değilse çökmesin
    try:
        git()
    except Exception as e:
        LOGGER.warning(f"git() skipped: {e}")

    dbb()

    # Railway'de heroku yoksa çökmesin
    try:
        heroku()
    except Exception as e:
        LOGGER.warning(f"heroku() skipped: {e}")

    app = ZYRO()
    api = SafoneAPI()
    userbot = Userbot()

    # Platformları al
    from TEAMZYRO.platforms import (
        AppleAPI, CarbonAPI, RessoAPI, SoundAPI, SpotifyAPI, TeleAPI, YouTubeAPI
    )

    platforms = {
        "Apple": AppleAPI(),
        "Carbon": CarbonAPI(),
        "SoundCloud": SoundAPI(),
        "Spotify": SpotifyAPI(),
        "Resso": RessoAPI(),
        "Telegram": TeleAPI(),
        "YouTube": YouTubeAPI(),
    }

    return app, api, userbot, platforms
