import os
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Turn Off WiFi ?")
root.geometry("240x150")
root.resizable(width = False, height = False)
root.eval('tk::PlaceWindow . center')

init = 10

def countdownLabel(label):
    def count():
        global init
        init -=1
        label.config(text= "WiFi will turn off after " + str(init) + " sec.")
        label.after(1000, count)
        if init == 0 :
            wifiOff()
    count()

def wifiOff():
    #Raspberry version :
    os.system("sudo ifconfig wlan0 off")
    #OSX version :
    #os.system("networksetup -setairportpower en1 off")
    root.destroy()
    exit()

def stop():
    exit()
    root.destroy()


label = tk.Label(root)
Off = ttk.Button(root, text="Turn off WiFi", command=lambda:wifiOff())
NotNow = ttk.Button(root, text="Not Now !", command=lambda:stop())

label.pack(pady=20)
Off.pack(padx=1, pady=1, expand=True, side=tk.LEFT)
NotNow.pack(padx=1, pady=1, expand=True, side=tk.RIGHT)

countdownLabel(label)


root.mainloop()
