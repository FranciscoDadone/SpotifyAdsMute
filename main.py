try:
    from SwSpotify import spotify
except:
    print("Install SwSpotify using: ", "pip install SwSpotify")
import time, os

from SwSpotify import SpotifyClosed, SpotifyNotRunning, SpotifyPaused

def mute(mute):
    try:
        os.mkdir("tmp")
    except: pass
    os.system("pacmd list-sink-inputs > tmp/list-sink-inputs")
    process_id = []
    # Count the number of inputs
    with open("tmp/list-sink-inputs", "r") as file:
        sink_input_lines = file.readlines()
        
        for i in range(len(sink_input_lines)):
            line = sink_input_lines[i].strip()            
            if line[:7] == "index: ":
                for j in range(i, len(sink_input_lines)):
                    if sink_input_lines[j][:7] == "index: ": break
                    if sink_input_lines[j].strip() == 'media.name = "spotify"' or sink_input_lines[j].strip() == 'media.name = "Spotify"' or sink_input_lines[j].strip() == 'application.name = "Spotify"' or sink_input_lines[j].strip() == 'application.name = "spotify"': 
                        process_id.append(line[7:])

    for process in process_id:
        os.system(f"pacmd set-sink-input-mute {process} {mute}")

def main():
    mute("false")
    muted = False
    old_song = ""
    while True:
        try:
            song_name_lower = spotify.current()[0].lower()
            song_name = spotify.current()[0]
            artist_name = spotify.current()[1]

            # Displays to the terminal the current song name and artist.
            if old_song != song_name:
                print("Now listening to: ", song_name, " - ", artist_name)
                old_song = song_name
            # Handles the mute process when there's an Ad.
            if 'advertisement' in song_name_lower or 'spotify' in song_name_lower:  
                mute("true")
                muted = True
            # Handles the unmute when the ad finishes and spotify is muted.
            elif muted and ('advertisement' not in song_name_lower or 'spotify' not in song_name_lower):
                mute("false")
                muted = False
            time.sleep(1) # sleeps one second.
            #print(muted)
        except SpotifyPaused:
            if old_song != "":
                print("Spotify paused.")
                old_song = ""
        except SpotifyNotRunning or SpotifyClosed:
            if old_song != "":
                print("Spotify closed.")
                old_song = ""

if __name__ == "__main__":
    main()
