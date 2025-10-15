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
import Main

def Main():
    excpt = Tk()
    excpt.title("Exception Tester")
    excpt.geometry("400x200")
    label = Label(excpt, text="Exception tester, for testing purposes only.")
    label.grid(column=0, row=0, padx=15, pady=15)

    excpt.mainloop()
