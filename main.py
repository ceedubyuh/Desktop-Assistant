# Written by Carter Womack
# Designed as an all-in-one Desktop Assistant application
# TODO: 
#   Get basic functions to work with command-line or hardcoding:
#       -Open and close applications
#       -Search Google
#       -Time and Date
#       -Control the system (sleep, shut down, restart)
#   Add a GUI so it"s accessible like an app
#   Make it hideable in taskbar
#   Keep it small and clean

from AppOpener import run
import webbrowser, requests
from bs4 import BeautifulSoup
import pystray
from pystray import MenuItem as item
from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image

root = Tk()
root.title("Personal Assistant")
root.geometry("300x300")

# Window Functions
def quitWindow(icon, item):
    icon.stop()
    root.destroy()

def showWindow(icon, item):
    icon.stop()
    root.after(0,root.deiconify)

def withdrawWindow():
    root.withdraw()
    img = Image.open("logo.png")
    menu = (item('Quit', quitWindow), item('Show', showWindow))
    icon = pystray.Icon("name", img, "title", menu)
    icon.run()


root.protocol('WM_DELETE_WINDOW', withdrawWindow)
# Main FUNCTIONS

text=StringVar()
def search():
    data = requests.get('https://www.google.com/search?q=' + text.get())
    soup =  BeautifulSoup(data.content, 'html.parser')
    result =  soup.select('.kCrYT a')
    for link in result[:1]:
        searching = link.get('href')
        searching = searching[7:]
        searching = searching.split("&")
        webbrowser.open(searching[0])

label=Label(text="Enter here to search",font=("Times",15,"bold"))
label.pack()
enter=Entry(textvar=text,width=30)
enter.pack()
button=Button(text="Search",width=30,command=search)

#BIND ENTER TO SEARCH AS WELL AS THE BUTTON!!!!
root.bind('<Return>', search)
button.pack()

def openGoogle():
    google = "https://www.google.com"
    webbrowser.open(google)

def openSteam():
    run("steam")

def currTime():
    current = strftime("%H:%M:%S %p")
    clock.config(text=current)
    clock.after(1000,currTime)

clock = Label(root, font=("calibri", 20, "bold"),  
            foreground="black")
clock.pack()
currTime()

#Icons for Buttons
googleIcon = PhotoImage(file="google.png")
steamIcon = PhotoImage(file="steam.png")
#Buttons
googleButton = Button(root, image = googleIcon, command = openGoogle).pack(side = "left", anchor="e", expand=True)
steamButton = Button(root, image = steamIcon, command = openSteam).pack(side = "right", anchor="w", expand=True)
mainloop()


