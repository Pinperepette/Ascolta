#! /usr/bin/env python
#  -*- coding: utf-8 -*-

import sys, time

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ascolta_support
import speech_recognition as sr
recognizer_instance = sr.Recognizer()


def vp_start_gui():

    global val, w, root
    root = Tk()
    top = Ascolta (root)
    ascolta_support.init(root, top)
    root.mainloop()

w = None
def create_Ascolta(root, *args, **kwargs):

    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Ascolta (w)
    ascolta_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Ascolta():
    global w
    w.destroy()
    w = None


class Ascolta:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("563x291+415+119")
        top.title("Ascolta")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Buttonmp3 = Button(top)
        self.Buttonmp3.place(relx=0.71, rely=0.03, height=44, width=142)
        self.Buttonmp3.configure(activebackground="#d9d9d9")
        self.Buttonmp3.configure(activeforeground="#000000")
        self.Buttonmp3.configure(background="#d9d9d9")
        self.Buttonmp3.configure(disabledforeground="#a3a3a3")
        self.Buttonmp3.configure(foreground="#000000")
        self.Buttonmp3.configure(highlightbackground="#d9d9d9")
        self.Buttonmp3.configure(highlightcolor="black")
        self.Buttonmp3.configure(pady="0")
        self.Buttonmp3.configure(text='''Ascolta''')
        self.Buttonmp3.configure(width=142)
        self.Buttonmp3.configure(command=self.Voce)

        self.Text1 = Text(top)
        self.Text1.place(relx=0.02, rely=0.24, relheight=0.7, relwidth=0.97)
        self.Text1.configure(background="#ffff40")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#000000")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=544)
        self.Text1.configure(wrap=WORD)
    def Voce(self):
        with sr.Microphone() as source:
            recognizer_instance.adjust_for_ambient_noise(source)
            audio = recognizer_instance.listen(source)
        try:
            text = recognizer_instance.recognize_google(audio,language="it-IT")
            msg1 = (text)
            self.Text1.delete('1.0',END)
            self.Text1.insert("end", msg1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    vp_start_gui()
