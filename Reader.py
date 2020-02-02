import spotipy
import spotipy.util as util
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

class Reader:

    def __init__(self):
        self.lcd = LCD_Screen()
        
        ID='1138b697263c4280bf7c63bbb3d9e698'
        SECRET='447c1235c85c4f76ad7b676e7300cf70'
        URI='https://localhost/'
        
        scope = 'user-read-playback-state'
        songToken = util.prompt_for_user_token(username='lyirk',
                scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
        
        self.readerPlayer = spotipy.Spotify(auth=songToken)

    def update_LCD(self):
        self.lcd.writeSong(self.readerPlayer.current_playback()['item']['name'])

    def write_to_card(self, uri):
        self.PlayerWriter(self.readerPlayer.currnet_playback()['item']['uri'])
