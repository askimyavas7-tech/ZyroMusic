import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# -------------------- helpers (railway safe) --------------------
def _getenv(key: str, default: str = "") -> str:
    return (getenv(key, default) or "").strip()

def _to_int(val: str, default: int = 0) -> int:
    try:
        return int(str(val).strip())
    except Exception:
        return default

def _to_bool(val: str, default: bool = False) -> bool:
    if val is None:
        return default
    return str(val).strip().lower() in ("1", "true", "yes", "y", "on")

def _to_int_list(val: str) -> list[int]:
    # "123 456" / "123,456" / "123|456" hepsini kabul et
    if not val:
        return []
    parts = re.split(r"[,\s|]+", str(val).strip())
    out = []
    for p in parts:
        p = p.strip()
        if p.isdigit():
            out.append(int(p))
    return out

# -------------------- Telegram API --------------------
API_ID = _to_int(_getenv("API_ID"), 0)
API_HASH = _getenv("API_HASH")
BOT_TOKEN = _getenv("BOT_TOKEN")
BOT_USERNAME = _getenv("BOT_USERNAME")

# Eval / sudo tarzı kullanıcı id listesi
EVAL = _to_int_list(_getenv("EVAL", "0000000 0000000"))

# -------------------- Database --------------------
MONGO_DB_URI = _getenv("MONGO_DB_URI")
DB_NAME = _getenv("DB_NAME", "Trendyol")

# -------------------- Limits --------------------
DURATION_LIMIT_MIN = _to_int(_getenv("DURATION_LIMIT", "17000"), 17000)

# Logger / Owner (boşsa bot crash etmesin)
LOGGER_ID = _to_int(_getenv("LOGGER_ID", "0"), 0)
OWNER_ID = _to_int(_getenv("OWNER_ID", "0"), 0)

# -------------------- Heroku vars (Railway’de boş kalabilir) --------------------
HEROKU_APP_NAME = _getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = _getenv("HEROKU_API_KEY")

UPSTREAM_REPO = _getenv("UPSTREAM_REPO", "https://github.com/MrZyro/ZyroMusic")
UPSTREAM_BRANCH = _getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# -------------------- Support links (istedigin gibi) --------------------
SUPPORT_CHANNEL = _getenv("SUPPORT_CHANNEL", "https://t.me/MUHABBET_SOFASI_TR")
SUPPORT_CHAT = _getenv("SUPPORT_CHAT", "https://t.me/MUHABBET_SOFASI_TR")

# -------------------- Assistant auto leave --------------------
AUTO_LEAVING_ASSISTANT = _to_bool(_getenv("AUTO_LEAVING_ASSISTANT", "True"), True)
AUTO_LEAVE_ASSISTANT_TIME = _to_int(_getenv("ASSISTANT_LEAVE_TIME", "9000"), 9000)

SONG_DOWNLOAD_DURATION = _to_int(_getenv("SONG_DOWNLOAD_DURATION", "9999999"), 9999999)
SONG_DOWNLOAD_DURATION_LIMIT = _to_int(_getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"), 9999999)

# -------------------- Spotify --------------------
SPOTIFY_CLIENT_ID = _getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = _getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# -------------------- Playlist / filesize --------------------
PLAYLIST_FETCH_LIMIT = _to_int(_getenv("PLAYLIST_FETCH_LIMIT", "25"), 25)

TG_AUDIO_FILESIZE_LIMIT = _to_int(_getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"), 5242880000)
TG_VIDEO_FILESIZE_LIMIT = _to_int(_getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"), 5242880000)

# -------------------- String sessions --------------------
STRING1 = _getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# -------------------- Runtime vars --------------------
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# -------------------- Images --------------------
START_IMG_URL = _getenv("START_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
PING_IMG_URL = _getenv("PING_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
PLAYLIST_IMG_URL = _getenv("PLAYLIST_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
STATS_IMG_URL = _getenv("STATS_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
TELEGRAM_AUDIO_URL = _getenv("TELEGRAM_AUDIO_URL", "https://files.catbox.moe/ghaqbv.jpg")
TELEGRAM_VIDEO_URL = _getenv("TELEGRAM_VIDEO_URL", "https://files.catbox.moe/ghaqbv.jpg")
STREAM_IMG_URL = _getenv("STREAM_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
SOUNCLOUD_IMG_URL = _getenv("SOUNCLOUD_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
YOUTUBE_IMG_URL = _getenv("YOUTUBE_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
SPOTIFY_ARTIST_IMG_URL = _getenv("SPOTIFY_ARTIST_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
SPOTIFY_ALBUM_IMG_URL = _getenv("SPOTIFY_ALBUM_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
SPOTIFY_PLAYLIST_IMG_URL = _getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://files.catbox.moe/ghaqbv.jpg")
