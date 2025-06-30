import random

songs = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3']  # Replace with your songs
random.shuffle(songs)
with open('playlist.m3u', 'w') as f:
    f.write('\n'.join(songs))
print("Playlist saved as playlist.m3u")