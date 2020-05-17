import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os, time, sys, glob, re, pandas as pd, numpy as np
from shutil import copyfile

window = tk.Tk()
window.withdraw()
file_path = filedialog.askdirectory(title='Select folder where new reports are located')