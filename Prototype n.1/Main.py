import os
import sys
import time
import threading
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from tkinter import * #temporary, cause i dont know how to make something in pyqt5
import subprocess
import External as ext
import exceptset as excpt

slots = {
    "s1": None,
    "s2": None,
    "s3": None,
    "s4": None,
    "s5": None,
    "s6": None,
    "s7": None,
    "s8": None,
    "s9": None,
    "s10": None
}

root = Tk()

panel = 0
panpad = 10
l1 = 0

def log(message, err):
    print ("[LOG] | " + message + " | Exception | " + err)

def panel(func):
    if func == 1:
        menu = Button(root, text="Menu", command=lambda: panel(2))
        menu.grid(column=0, row=panel, padx=panpad, pady=panpad)
    elif func == 2:
        print("menu doesnt exist yet")
    elif func > 2:
        log("invalid panel function call", "404")

def desktop(func):
    if func == 1:
        # Default itens
        trsh = Button(root, text="Trash")
        ext.set("s1", "trash")
        trsh.grid(column=0, row=1, padx=15, pady=15)
    elif func == 2:
        print("desktop doesnt have any execution call")

def Main(func) :
    if func == 1:
        root.title("Phantom Pr.1, for testing purposes only")
        root.geometry("800x600")
    
        # Main Window


        root.mainloop()
    elif func == 2:
       print("Main window doesnt have any execution call")
    elif func == 3:
        pass

def start():
    Main(1)
    panel(1)
    desktop(1)

start()