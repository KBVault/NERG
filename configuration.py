import re 
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def get_env_var(var_name, default=None, required=False):
    value = getenv(var_name, default)
    if required and value is None:
        raise ValueError(f"Environment variable {var_name} is required but not set.")
    return value
    
API_ID = 

API_HASH = ""

BOT_TOKEN = ""

BOT_ID = 7404841712

BOT_USERNAME = "soul_musixbot"

MONGO_DB_URI = ""

DURATION_LIMIT_MIN = int(get_env_var("DURATION_LIMIT", 500000))

LOGGER_ID = int(get_env_var("LOGGER_ID", -1002070231017))

LOG_CHANNEL_ID = -1002303365261

OWNER_ID = 6806897901

SPECIAL_USER_ID = 7472465398

HEROKU_APP_NAME = "developer4"

HEROKU_API_KEY = None

UPSTREAM_REPO = None

UPSTREAM_BRANCH = None

GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/soul_x_network"

SUPPORT_CHAT = "https://t.me/soul_x_society"

AUTO_LEAVING_ASSISTANT = bool(get_env_var("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = get_env_var("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")

SPOTIFY_CLIENT_SECRET = get_env_var("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

PLAYLIST_FETCH_LIMIT = int(get_env_var("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(get_env_var("TG_AUDIO_FILESIZE_LIMIT", 2147483648))
TG_VIDEO_FILESIZE_LIMIT = int(get_env_var("TG_VIDEO_FILESIZE_LIMIT", 2147483648))


STRING1 = ""
STRING2 = get_env_var("STRING_SESSION2", None)
STRING3 = get_env_var("STRING_SESSION3", None)
STRING4 = get_env_var("STRING_SESSION4", None)
STRING5 = get_env_var("STRING_SESSION5", None)


filter_users = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = get_env_var("START_IMG_URL", "https://telegra.ph//file/0049278b7c30b40319f7f.jpg")
PING_IMG_URL = get_env_var("PING_IMG_URL", "https://telegra.ph//file/01beefac0ce981a8bc5c8.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph//file/591fcfcedd423855767f4.jpg"
STATS_IMG_URL = "https://telegra.ph//file/86d5e07516147d669f3ba.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/a2168e8f272b5066164da.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/a5d7ceadb32e7d509ce81.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/4a1671590148cd4cd57b6.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/591fcfcedd423855767f4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/f508e9177873c30885606.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/5711afce367e3c68e97a8.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/aaab0e22901fa86fa537e.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
