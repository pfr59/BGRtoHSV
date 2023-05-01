#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Sep 28, 2019 03:39:17 PM CDT  platform: Windows NT
#    Sep 30, 2019 09:12:24 AM CDT  platform: Windows NT
#    Sep 30, 2019 09:18:35 AM CDT  platform: Windows NT
#    Sep 30, 2019 11:15:30 AM CDT  platform: Windows NT
#    Oct 28, 2019 01:09:35 PM CDT  platform: Windows NT
#    Oct 28, 2019 01:20:35 PM CDT  platform: Windows NT

import sys
import re
from tkinter import filedialog
from tkinter import *
import os
import os.path
import pathlib
from os import path
from tkinter import messagebox
from pathlib import Path

from BGR2HSV import BGR2HSV

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class BGRList():

    def __init__(self, first_val, second_val, third_val):

        self.valid_BGR_values = True        

        try:
            self.BGR_list = [int(first_val), int(second_val), int(third_val)]
        except Exception as e:
            messagebox.showerror("BGR Entry Error", "BGR Entry Error: " +str(e))

        for val in self.BGR_list:
            if val < 0: 
                messagebox.showerror("BGR Value Error - LOW", "BGR ValueError: Entry less than 0! ONLY ENTER VALUES FROM 0 TO 255")
                self.valid_BGR_values = False
            elif val > 255 : 
                messagebox.showerror("BGR Value Value Error - HIGH", "BGR Value Error: Entry greater than 255! ONLY ENTER VALUES FROM 0 TO 255")
                self.valid_BGR_values = False
                
    def getBGRList(self):
        return self.BGR_list
    
    def getValidBGRValues(self):
        return self.valid_BGR_values
    
## Instantiate an instance of the SelectStains class.
BGR_conversion = BGR2HSV()

def set_Tk_var():
    global entry_blue
    entry_blue = tk.StringVar()
    global entry_green
    entry_green = tk.StringVar()
    global entry_red
    entry_red = tk.StringVar()

def btn_release(p1):
    print('BGR_to_HSV_support.btn_release')

    dirname = ''
    logfilename = ''
    
    dirname = filedialog.askdirectory(initialdir=os.getcwd(),title='Please select a directory')
    if dirname != '':
        logfilename = dirname+"/BGR_to_HSV.csv"
        output_dir_lbl =("Ouput to: {}".format(logfilename))
        w.LabelOutDir.configure(text=output_dir_lbl)
    else:
        ## Defaults output directory to folder containing this program.
        dirname = os.getcwd()
        print ("\nNo directory selected - initializing with {} \n" .format(os.getcwd()))
        logfilename = dirname+"/BGR_to_HSV.csv"
        output_dir_lbl =("Ouput to: {}".format(logfilename))
        w.LabelOutDir.configure(text=output_dir_lbl)

    BGR_conversion.setLogFileName(logfilename)
        
    sys.stdout.flush()

def btn_convert_RGB_to_HSV(p1):
    print('BGR_to_HSV_support.btn_convert_RGB_to_HSV')
    # RESET HSV Integer List used for computing Paint.Net
    # equivalent values.
    
    BGR_conversion.resetHSVInt()    
    
    # Get BGR values
    BGR_list = BGRList(entry_blue.get(), entry_green.get(), entry_red.get())

    print(BGR_list.getBGRList())

## Execute conversion ONLY for valid values!
    if(BGR_list.getValidBGRValues()):
        BGR_conversion.setColorBGR_In(BGR_list.getBGRList())
        BGR_conversion.convert_BGR2HSV()
        output_HSV_lbl = 'Results - Hue, Saturation, Value: ' + BGR_conversion.getStrHSV()
        w.LabelResults.configure(text=output_HSV_lbl)
        output_paint_net_lbl = 'Paint.Net Approx. Hue, Sat, Value: ' + BGR_conversion.getPaintNetHSV()
        w.LabelPaintNet.configure(text=output_paint_net_lbl)
    else:
        messagebox.showerror("BGR Value Error", "CORRECT VALUE ERROR. Try again.")
    
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def exit():
    print('BGR_to_HSV_support.exit')
    sys.stdout.flush()
    destroy_window()

def open_instruct():
    print('BGR_to_HSV_support.open_instruct')
    sys.stdout.flush()
    os.startfile("BGR to HSV Convertor Instructions.pdf")

if __name__ == '__main__':
    import BGR_to_HSV
    BGR_to_HSV.vp_start_gui()





