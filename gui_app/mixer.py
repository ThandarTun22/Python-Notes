
from pygame import mixer

# starting the mixer
mixer.init()

# loading the song
mixer.music.load("super_mario.mp3")

# setting the volume
mixer.music.set_volume(0.7)

# start playing the song
mixer.music.play()

# infinite loop
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':
        # pausing the music
        mixer.music.pause()
    elif query == 'r':
        # resuming the music
        mixer.music.unpause()
    elif query == 'e':
        # stop the mixer
        mixer.music.stop()
        break


