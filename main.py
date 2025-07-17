from re import search
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# ===== Search Box =====
searchImage = PhotoImage(file="images/search.png")
mainImage = Label(root, image=searchImage)
mainImage.place(x=20, y=20)

searchField = tk.Entry(root, width=18, font=("poppins", 25, "bold"), justify="center", bg="#404040", border=0, fg="white")
searchField.place(x=50, y=40)
searchField.focus()

searchIcon = PhotoImage(file="images/search_icon.png")
searchTool = Button(root, image=searchIcon, borderwidth=0, cursor="hand2", bg="#404040")
searchTool.place(x=400, y=34)



root.mainloop()


