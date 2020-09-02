import tkinter as tk
from tkinter import PhotoImage

import voice


def get_question(entry1):
    x1 = entry1.get()
    voice.speak(x1)


def gui():
    root = tk.Tk()
    root.title("S.A.V.A")

    root.resizable(False, False)

    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.configure(background='#c8c8c8')
    canvas1.pack()

    entry1 = tk.Entry(root)
    canvas1.create_window(150, 140, window=entry1)

    photo = PhotoImage(file=r"res\AI.png")
    photoimage = photo.subsample(7, 7)
    button1 = tk.Button(image=photoimage, background='#ffffff', command=lambda: get_question(entry1))
    canvas1.create_window(150, 180, window=button1)

    root.mainloop()
