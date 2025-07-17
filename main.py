from re import search
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime, timezone
import requests
import pytz
from funcs import *


# ===== App Functions =====
def getWeather():
    city = searchField.get()
    geoLocator = Nominatim(user_agent="geoapiExercices")
    location = geoLocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    name.config(text="Current Weather")
    clock.config(text=current_time)



# ===== App Main Frame =====
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


# ===== Search Box =====
searchImage = PhotoImage(file="images/search.png")
mainSearch = Label(root, image=searchImage)
mainSearch.place(x=20, y=20)

searchField = tk.Entry(root, width=18, font=("poppins", 25, "bold"), justify="center", bg="#404040", border=0, fg="white")
searchField.place(x=50, y=40)
searchField.focus()

searchIcon = PhotoImage(file="images/search_icon.png")
searchTool = Button(root, image=searchIcon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
searchTool.place(x=400, y=34)


# ===== Logo =====
logoImage = PhotoImage(file="images/logo.png")
Logo = Label(root, image=logoImage)
Logo.place(x=150, y=100)


# ===== Bottom Box =====
frameImage = PhotoImage(file="images/box.png")
mainFrame = Label(root, image=frameImage)
mainFrame.pack(padx=5, pady=5, side=BOTTOM)


# ===== Time =====
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("helvetica", 20))
clock.place(x=30, y=130)


# ===== Weather Info =====
time = Label(root, font=("arial", 70, "bold"), text="Time", fg="#ee666d")
time.place(x=400, y=150)
cls = Label(root, font=("arial", 15, "bold"), text="cls")
cls.place(x=400, y=250)


# ===== Weather Details =====
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white")
label4.place(x=650, y=400)

w = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)



root.mainloop()


