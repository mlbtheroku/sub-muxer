
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5941906344:AAFpx76Y1aIthLCQMTteqcQbntQ6-NEvwnA')
    APP_ID = os.environ.get('APP_ID', 15830858)
    API_HASH = os.environ.get('API_HASH', '2c015c994c57b312708fecc8a2a0f1a6')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1349301822').split(',')]

    DOWNLOAD_DIR = 'downloads'
