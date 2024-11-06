from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import Image, ImageTk
from data import AudioPlayer
import pygame
import os

class AudioPlayerUI:
    def __init__(self, root):
        self.player = AudioPlayer()
        self.root = root
        self.root.configure(bg='lightblue')
        self.root.title("Odtwarzacz muzyki")
        self.root.geometry("500x300") 

        self.song_box = Listbox(root, bg='black', fg='green', selectbackground='green', selectforeground='black', width=60, font=font.Font(size=10), selectmode=SINGLE)
        self.song_box.pack(pady=20)
        self.song_box.bind("<<ListboxSelect>>", self._on_select)

        self.control_frame = Frame(root)
        self.control_frame.configure(bg="lightblue")
        self.control_frame.pack()

        # Załaduj obrazy do przycisków
        self.back_button_image = ImageTk.PhotoImage(Image.open('png/back.png'))
        self.forward_button_image = ImageTk.PhotoImage(file="png/next.png")
        self.play_button_image = ImageTk.PhotoImage(file="png/play.png")
        self.pause_button_image = ImageTk.PhotoImage(file="png/pause.png")
        self.stop_button_image = ImageTk.PhotoImage(file="png/stop.png")
        self.shuffle_button_image = ImageTk.PhotoImage(file="png/shuffle.png")

        # Przyciski sterujące
        self.back_button = Button(self.control_frame, bg="lightblue", activebackground="lightgrey", image=self.back_button_image, borderwidth=0, command=self.player.previous_song)
        self.forward_button = Button(self.control_frame, bg="lightblue", image=self.forward_button_image, borderwidth=0, command=self.player.next_song)
        self.play_button = Button(self.control_frame, bg="lightblue", image=self.play_button_image, borderwidth=0, command=self.player.play)
        self.pause_button = Button(self.control_frame, bg="lightblue", image=self.pause_button_image, borderwidth=0, command=self.player.pause)
        self.stop_button = Button(self.control_frame, bg="lightblue", image=self.stop_button_image, borderwidth=0, command=self.player.stop)
        self.shuffle_button = Button(self.control_frame, bg="lightblue", image=self.shuffle_button_image, borderwidth=0, command=self.toggle_shuffle)

        self.back_button.grid(row=0, column=0, padx=15)
        self.forward_button.grid(row=0, column=1, padx=15)
        self.play_button.grid(row=0, column=2, padx=15)
        self.pause_button.grid(row=0, column=3, padx=15)
        self.stop_button.grid(row=0, column=4, padx=15)
        self.shuffle_button.grid(row=0, column=5, padx=15)

        self.my_menu = Menu(root)
        self.root.config(menu=self.my_menu)

        self.add_song_menu = Menu(self.my_menu, background='lightblue')
        self.my_menu.add_command(label='Dodaj muzykę', command=self._add_song)

    def _add_song(self):
        """Dodaje utwory do playlisty."""
        songs = list(filedialog.askopenfilenames(initialdir='audio/', title='Wybierz muzykę', filetypes=(("mp3 Files", "*.mp3"), )))
        for song in songs:
            song_name = os.path.basename(song)
            print(f"Dodano: {song_name}")
            self.player.add_to_playlist(song) 
        self._refresh_song_box()

    def _refresh_song_box(self):
        """Odświeża Listbox z utworami."""
        self.song_box.delete(0, END)
        for song in self.player.playlist:
            self.song_box.insert(END, song)    

    def _on_select(self, event):
        """Obsługuje wybór utworu w Listboxie."""
        selected_title = self.song_box.curselection()
        if selected_title:
            selected_song = self.song_box.get(selected_title)
            self.player.set_chosen_song(selected_song)
            print(f"Wybrano utwór: {selected_song}")

    def toggle_shuffle(self):
        """Włącza/wyłącza tryb shuffle."""
        self.player.toggle_shuffle()
        print(f"Tryb shuffle: {'Włączony' if self.player.shuffle else 'Wyłączony'}")

# Uruchomienie aplikacji
root = Tk()
app = AudioPlayerUI(root)
root.mainloop()
