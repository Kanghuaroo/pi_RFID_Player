import spotipy
import spotipy.util as util
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

class Reader:

    def __init__(self):
        
        ID='1138b697263c'
        SECRET='264737bc4ad443429635d93babefc597'
        URI='https://localhost/'
        
        scope = 'user-read-playback-state'
        songToken = util.prompt_for_user_token(username='lyirk',
                scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
        
        self.readerPlayer = spotipy.Spotify(auth=songToken)
        self.lcd = LCD_Screen()

    def update_LCD(self):
        self.lcd.writeSong(self.readerPlayer.current_playback()['item']['name'])

    def write_to_card(self, uri):
        self.PlayerWriter(self.readerPlayer.currnet_playback()['item']['uri'])
