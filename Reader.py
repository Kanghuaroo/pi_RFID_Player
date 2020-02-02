import spotipy
import spoipy.util as util
from LCD_Screen import LCD_Screen
from PlayerWriter import PlayerWriter

class Reader:

    def __inti__(self):
        
        ID='bf8057981097462a95729337360b7f03'
        SECRET='264737bc4ad443429635d93babefc597'
        URI='https://localhost/'
        
        scope = 'user-read-playback-state'
        songToken = util.prompt_for_user_token(username='lyirk',
                scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)
        
        self.readerPlayer = spotipy.Spotify(auth=songToken)
        self.lcd = LCD_Screen()

        def upadte_LCD(self):
            lcd.writeSong(readerPlayer.current_playback()['item']['name'])

        def write_to_card(self, uri):
            self.PlayerWriter(readerPlayer.currnet_playback()['item']['uri'])
