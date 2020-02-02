#!/usr/bin/env python

import spotipy
import spotipy.util as util

ID='bf8057981097462a95729337360b7f03'
SECRET='264737bc4ad443429635d93babefc597'
URI='https://localhost/'

scope = 'user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(username='lyirk',
        scope=scope,client_id=ID,client_secret=SECRET, redirect_uri=URI)

#init of player and classes
sp = spotipy.Spotify(auth=token)

def currentPlayback(sp):
    #print('Card to Write ')
    msg = (sp.current_playback())


    text = msg['item']['uri']

    #print(msg['item']['uri'])
    print('=================================================')

    #for key in msg['item']:
    #    print(key)
    #    print(msg['item'][key])


    print("Name - " + msg['item']['name'])
    print("URI - " + msg['item']['uri'])
    print('Artist URI - ' + msg['item']['artists'][0]['uri'])
    print('Playlist/ Album - ' + msg['item']['album']['uri'])
    
    for item in msg['context']['uri']:
        print(item)
        print()

currentPlayback(sp)
