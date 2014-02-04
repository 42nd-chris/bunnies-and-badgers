import pygame
import sys

class Audio:
    _sounds = {}

    def __init__(self):
        try:
            pygame.mixer.init()
        except:
            sys.stderr.write("Can't open audio device.\n")

    def add_sound(self, sound_name, sound_path, volume = 0.05):
        """Add sounds to the classes dictionary of sounds.
           Later played back with Audio.play_sound()."""
        
        if pygame.mixer.get_init() == None:
            return

        self._sounds[sound_name] = pygame.mixer.Sound(sound_path)
        self._sounds[sound_name].set_volume(volume)

    def play_sound(self, sound_name):
        """Play a sound."""

        if pygame.mixer.get_init() == None \
        or not sound_name in self._sounds.keys():
            return

        self._sounds[sound_name].play()


    def add_music(self, track_path, volume = 0.25):
        """Add a music track, can be played with Audio.play_music()."""

        if pygame.mixer.get_init() == None:
            return
        pygame.mixer.music.load(track_path)

    def play_music(self, loops = -1, start = 0.0):
        """Start the music playing."""

        if pygame.mixer.get_init() == None:
            return

        pygame.mixer.music.play(loops, start)
