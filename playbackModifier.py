import spotipy
import spotipy.util as util
from mfrc522 import SimpleMFRC522

class PlaybackModifier:

    def __init__(self):

        ID='bf8057981097462a95729337360b7f03'
        SECRET='264737bc4ad443429635d93babefc597'
        URI='https://localhost/'

        scope = 'user-modify-playback-state'
        modifyToken = util.prompt_for_user_token(username='lyirk',
                scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)

        self.modifyPlayer = spotipy.Spotify(auth=modifyToken)

    def changeSong(self, reader):
        try:
            print('Hold a Song Card Near...')
            #Song URI is in the text var
            text = reader.read()
            text = str(text[1])
            text = text.strip(' ')

            #how to play text
            if text.find('text') != 1:
                modifyPlayer.start_playback(uris=[text])
            elif text.find('playlist') != -1:
                modifyPlayer.shuffle(state=True)
                modifyPlayer.start_playback(context_uri=text)
            elif text.find('artist') != -1:
                modifyPlayer.shuffle(state=True)
                modifyPlayer.start_playback(context_uri=text)
        except KeyboardInterrupt:
            GPIO.cleanup()
        finally:
            GPIO.cleanup()

