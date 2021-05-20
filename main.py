try:
    from SwSpotify import spotify
except:
    print("Install SwSpotify using: ", "pip install SwSpotify")
import time

from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused

while True:
    try:
        print(spotify.current())
        if(spotify.current()[0] == 'Advertisement'): 
            pass
        
        
        time.sleep(1)
    except SpotifyPaused:
        print("Spotify paused.")
    except SpotifyNotRunning or SpotifyClosed:
        print("Spotify closed.")