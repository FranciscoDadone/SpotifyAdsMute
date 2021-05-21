try:
    from SwSpotify import spotify
except:
    print("Install SwSpotify using: ", "pip install SwSpotify")
import time

from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused

def mute(mute):
    try:
        os.mkdir("tmp")
    except: pass
    os.system("pacmd list-sink-inputs > tmp/list-sink-inputs")
    process_id = 0
    with open("tmp/list-sink-inputs", "r") as file:
        for line in file:
            wasFound = False
            stripped_line = line.strip()
            if(stripped_line[:7] == "index: "):
                process_id = stripped_line[7:]
            if(stripped_line == 'media.name = "Spotify"' or stripped_line == 'application.name = "Spotify"'): 
                wasFound = True
                break
    if wasFound:
        os.system(f"pacmd set-sink-input-mute {process_id} {mute}")

def main():
    muted = False
    while True:
        try:
            print(spotify.current())
            if spotify.current()[0] == 'Advertisement': 
                mute("true")
                muted = True
            elif muted and spotify.current()[0] != 'Advertisement':
                mute("false")
                muted = False
            
            
            time.sleep(1)
        except SpotifyPaused:
            print("Spotify paused.")
        except SpotifyNotRunning or SpotifyClosed:
            print("Spotify closed.")

if __name__ == "__main__":
    main()