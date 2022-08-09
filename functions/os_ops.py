import os 
import subprocess as sp

paths = {
    'steam': r"D:\Steam\steam.exe",
    'Discord': r"C:\Users\Isiac\OneDrive\Desktop\Discord.lnk",
    'Spotify': r"C:\Users\Isiac\AppData\Local\Microsoft\WindowsApps\Spotify.exe",
    'Valorant': r"C:\Users\Public\Desktop\VALORANT.lnk",
    'Code': r"C:\Users\Isiac\OneDrive\Desktop\Visual Studio Code.lnk",
    'Fallout 4': r"C:\Users\Isiac\OneDrive\Desktop\Fallout 4.url",
    'Opera': r"C:\Users\Isiac\OneDrive\Desktop\Opera Browser.lnk",
    'Chrome': r"C:\Users\Public\Desktop\Google Chrome.lnk"
}

def open_steam():
    os.startfile(paths['steam'])

def open_Discord():
    os.startfile(paths['Discord'])

def open_Spotify():
    os.startfile(paths['Spotify'])

def open_Valorant():
    os.startfile(paths['Valorant'])

def open_Code():
    os.startfile(paths['Code'])

def open_Fallout4():
    os.startfile(paths['Fallout 4'])

def open_Opera():
    os.startfile(paths['Opera'])

def open_Chrome():
    os.startfile(paths['Chrome'])