# https://github.com/alien-max
from tkinter import *
import pygame
from pygame import mixer
import os

root = Tk()
root.geometry("600x450")
root.resizable(0,0)
root.title("Music player")

status = StringVar()
status.set("Playing")

pygame.init()
mixer.init()

def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.insert('1.0', playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)
    status.set("Playing")

    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.config(state=DISABLED)
    status.set("Stoped")

    mixer.music.stop()

def pausesong():
    status.set("Paused")
    mixer.music.pause()

def unpausesong():
    status.set("Playing")
    mixer.music.unpause()


frametrack = LabelFrame(root, text="Song Track", font=("Arial", 12, "bold"), bg="#673ab7", fg="#fff",bd=5, relief=GROOVE)
frametrack.place(x=0, y=250, width=600, height=100)

songtrack = Text(frametrack, width=40, height=2, font=("Arial", 12), bg="#5205d8", fg="#fff", state=DISABLED)
songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstatus = Label(frametrack, textvariable=status, font=("Arial", 10), bg="#5205d8", fg="#fff")
trackstatus.grid(row=0, column=1, padx=10, pady=5)

buttonframe = LabelFrame(root, text="Control Panel", font=("Arial", 12, "bold"), bg="#673ab7", fg="#fff", bd=5, relief=GROOVE)
buttonframe.place(x=0, y=350, width=600, height=100)

playbtn = Button(buttonframe, text="Play", width=8, height=2, font=("Arial", 12), bg="#5205d8", fg="#fff", bd=3, command=playsong)
playbtn.grid(row=0, column=0, padx=10, pady=5)

pausebtn = Button(buttonframe, text="Pause", width=8, height=2, font=("Arial", 12), bg="#5205d8", fg="#fff", bd=3, command=pausesong)
pausebtn.grid(row=0, column=1, padx=10, pady=5)

unpausebtn = Button(buttonframe, text="Unpause", width=8, height=2, font=("Arial", 12), bg="#5205d8", fg="#fff", bd=3, command=unpausesong)
unpausebtn.grid(row=0, column=2, padx=10, pady=5)

stopbtn = Button(buttonframe, text="Stop", width=15, height=2, font=("Arial", 12), bg="#5205d8", fg="#fff", bd=3, command=stopsong)
stopbtn.grid(row=0, column=3, padx=10, pady=5)

songsframe = LabelFrame(root, text="Playlist", font=("Arial", 12, "bold"), bg="gray", fg="#fff", bd=5, relief=GROOVE)
songsframe.place(x=0, y=0, width=600, height=250)

scrol_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, selectbackground="#673ab7", selectmode=SINGLE, height=250, font=("Arial", 12), bg="silver" ,fg="#000", relief=GROOVE, yscrollcommand=scrol_y.set)
scrol_y.config(command=playlist.yview)
scrol_y.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)

user = os.getlogin()
os.chdir(r"C:\Users\\"+user+"\\Music")
songtracks = os.listdir()

for track in songtracks:
    if ".mp3" in track:
        playlist.insert(END, track)
    else:
        pass

root.mainloop()