import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os, time, sys, glob, re, pandas as pd, numpy as np
from shutil import copyfile

window = tk.Tk()
window.withdraw()
# file_path = filedialog.askdirectory(title='Select folder where new reports are located')
webship_file_path = filedialog.askopenfilename(title="Select WebShip csv file")
ws_data = pd.read_csv(webship_file_path,encoding = "ISO-8859-1")
# data = pd.read_excel()
print(ws_data)