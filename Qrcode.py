# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:28:45 2024

@author: sreeja
"""

import segno
import tkinter as tk
from tkinter import simpledialog

ROOT=tk.Tk()
ROOT.withdraw()

USER_INP=simpledialog.askstring(title="Message",prompt="Enter:")

File_name=simpledialog.askstring(title="File Name",prompt="Enter:")
#from tkinter import messagebox
#wn=Tk()
#wn.geometry('700x700')
#wn.config(bg='SteelBlue3')
#Message=input("Enter your message:")
test=segno.make_qr(USER_INP)
#File_name=input("Enter file name:")
test.save(File_name, scale=35)