#!/usr/bin/env python

import spotipy
import spotipy.util as util

def currentPlayback(sp):
    #print('Card to Write ')
    msg = (sp.current_playback())


    text = msg['item']['uri']

    #print(msg['item']['uri'])
    print('=================================================')

    for key in msg['item']:
        print(key)
        print(msg['item'][key])


        print("URI - " + msg['item']['uri'])
        print("Name - " + msg['item']['name'])
