from Infinitymusic.core.bot import Nand
from Infinitymusic.core.dir import dirr
from Infinitymusic.core.git import git
from Infinitymusic.core.userbot import Userbot
from Infinitymusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aditya()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


