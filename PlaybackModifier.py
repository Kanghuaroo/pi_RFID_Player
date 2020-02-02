import spotipy
from mfrc522 import SimpleMFRC522

class PlaybackModifier:

    def __init__(self, sp):
        self.modifyPlayer = sp

    def changeWithRFID(self, reader):
            print('Hold a Song Card Near...')
            text = reader.read()
            self.changeSong(text)

    def changeSong(self, text):
            #Song URI is in the text var
            text = str(text[1])
            text = text.strip(' ')
            
            print(text)
            #how to play text
            if text.find('track') != -1:
                self.modifyPlayer.start_playback(uris=[text])
                self.modifyPlayer.repeat('track')
            elif text.find('playlist') != -1:
                self.modifyPlayer.shuffle(state=True)
                self.modifyPlayer.start_playback(context_uri=text)
            elif text.find('artist') != -1:
                self.modifyPlayer.start_playback(context_uri=text)
                self.modifyPlayer.shuffle(state=True)
    
    def skip(self):
        self.modifyPlayer.next_track()
    
    def pause(self):
        self.modifyPlayer.pause_playback()

    def rewind(self):
        self.modifyPlayer.previous_track()
