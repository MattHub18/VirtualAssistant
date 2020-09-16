import tkinter as tk
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk
from pygame import mixer


class Mixer(object):
    def __init__(self, master, filename):

        self.pauseStatus = False
        self.load = False
        self.mixer = mixer
        self.mixer.init()
        self.mixer.music.set_volume(0.7)
        self.title = ""

        self.master = master

        self.master.resizable(False, False)
        self.master.title("Mixer")
        self.filename = filename
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.configure(background='#c8c8c8')
        self.canvas.pack()

        play_button = tk.Button(self.canvas, text="Play", background='#ffffff',
                                command=self.play)
        pause_button = tk.Button(self.canvas, text="Pause", background='#ffffff',
                                 command=self.pause)
        stop_button = tk.Button(self.canvas, text="Stop", background='#ffffff',
                                command=self.stop)
        browse_button = tk.Button(self.canvas, text="Browse", background='#ffffff',
                                  command=self.browse)

        self.canvas.create_window(50, 250, window=play_button)
        self.canvas.create_window(150, 250, window=pause_button)
        self.canvas.create_window(250, 250, window=stop_button)
        self.canvas.create_window(150, 285, window=browse_button)

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(150, 120, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            if self.load:
                angle += 3
            else:
                angle += 0
            angle %= 360

    def play(self):
        if self.title != "":
            self.load = True
            self.mixer.music.play()

    def pause(self):
        if not self.pauseStatus:
            self.load = False
            self.mixer.music.pause()
            self.pauseStatus = True
        elif self.pauseStatus:
            self.load = True
            self.mixer.music.unpause()
            self.pauseStatus = False

    def stop(self):
        self.load = False
        self.mixer.music.stop()

    def exit(self):
        self.mixer.music.stop()
        self.mixer.stop()

    def browse(self):
        self.master.filename = filedialog.askopenfilename(initialdir="/Users/Public/Music/Sample Music",
                                                          title="Select file",
                                                          filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.title = self.master.filename
        self.mixer.music.load(self.master.filename)
