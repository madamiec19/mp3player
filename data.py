import pygame
from pygame import mixer
import os
import random

class AudioPlayer:
    def __init__(self):
        mixer.init()
        self.playlist = {}  # {song_name: song_path}
        self.is_paused = False
        self.current_song = ''
        self.shuffle = False  # Dodajemy tryb shuffle

    def add_to_playlist(self, song_path):
        """Dodaje utwór do playlisty."""
        song_name = os.path.basename(song_path)  # Pobierz nazwę pliku
        self.playlist[song_name] = song_path

    def set_chosen_song(self, title):
        """Ustawia aktualnie wybrany utwór."""
        self.current_song = title

    def play(self):
        """Odtwarza wybrany utwór."""
        if self.playlist and self.current_song:
            if self.is_paused:
                mixer.music.unpause()
                self.is_paused = False
            else:
                mixer.music.load(self.playlist[self.current_song])
                mixer.music.play()
                mixer.music.set_endevent(pygame.USEREVENT)
            self.is_paused = False

    def pause(self):
        """Wstrzymuje odtwarzanie."""
        mixer.music.pause()
        self.is_paused = True

    def stop(self):
        """Zatrzymuje odtwarzanie."""
        mixer.music.stop()
        self.is_paused = False

    def next_song(self):
        """Przechodzi do następnego utworu w playliście."""
        if self.playlist:
            if self.shuffle:
                # Losowe wybranie następnego utworu
                next_song_name = random.choice(list(self.playlist.keys()))
                self.current_song = next_song_name
            else:
                # Kolejność utworów w playlisty
                keys = list(self.playlist.keys())
                current_song_number = keys.index(self.current_song)
                next_song_name = keys[(current_song_number + 1) % len(self.playlist)]
                self.current_song = next_song_name
            self.play()

    def previous_song(self):
        """Przechodzi do poprzedniego utworu w playliście."""
        if self.playlist:
            keys = list(self.playlist.keys())
            current_song_number = keys.index(self.current_song)
            previous_song_name = keys[(current_song_number - 1) % len(self.playlist)]
            self.current_song = previous_song_name
            self.play()

    def toggle_shuffle(self):
        """Przełącza tryb shuffle."""
        self.shuffle = not self.shuffle
