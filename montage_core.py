# Core system with all of the functions the algorithme will need
# And with all of the imports needed

import os
import datetime
import time
import sys
from array import *
import json
import random
import threading
from threading import Thread
import shutil

from os import listdir
from os.path import isfile, join

import tkinter as tk

import subprocess
from mutagen.mp3 import MP3

import urllib.request
from bs4 import BeautifulSoup

import textwrap

def getBeautifulSoup(title):
    textToSearch = title
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Return informations about a youtube video searched from a given parsed html variable
# @Parameters:
# soup : Parsed html from BeautifulSoup module using getBeautifulSoup() function
# info : Informations returned
# - name_video
# - link_video
# - name_author
# - link_author
def getInfoFromYoutube(soup, info):
    for channel in soup.findAll(attrs={'class':'yt-uix-sessionlink spf-link'}):
        if(channel['href'][0:8] == "/channel"):
            if(info == "name_author"):
                return channel.findAll(text=True)[0]
            if(info == "link_author"):
                return 'https://www.youtube.com' + channel['href']
            break

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        if(vid['href'][0:6] != "https:"):
            if(info == "name_video"):
                return vid.findAll(text=True)[0]
            if(info == "link_video"):
                return 'https://www.youtube.com' + vid['href']
            break
    return "error"


# Returns if video in path contains audio
def containAudio(path):
    container = os.popen("ffprobe -i "+path+" -show_streams -select_streams a -loglevel error").read()
    if(container == ""):
        return False
    else:
        return True

# Get the list of files in a given path
def getListFile(path):
    if(folderExists(path)):
        toreturn = [f for f in listdir(path) if isfile(join(path, f))]
        return sorted(toreturn)
    else:
        return []

def appendTemp(filename, content):
    path = "temp/" + filename + ".txt"
    file = open(path, "a")
    file.write(content + "\n")
    file.close()

# Clear all of the temps files in the temp folder
def clearTemp():
    clearFolder("temp/")
    clearFolder("temp/skins")
    clearFolder("temp/audio_from_video")
    doPrint("Temp folder cleared")

# Clear all the files in a given folder
def clearFolder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

# Waiting animation in the console
def spin_cursor():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1) # adjust this to change the speed
            sys.stdout.write('\b')
            if done:
                sys.stdout.flush()
                sys.stdout.write('done')
                sys.stdout.write('\n')
                return

# Function to check if the input is an int or not
# @Parameters :
# s String/Float/Int/...
# @Return Boolean
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
# Function that returns the length of an audio file in seconds
# @Parameters :
# filename  String
# @Return int
def getLengthOfAudio(filename):
    audio = MP3(filename)
    return audio.info.length

# Function that returns the length of a video file in seconds
# @Parameters :
# filename  String
# @Return int
def getLengthOfVideo(filename):
    result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for x in result.stdout.readlines():
        if b"Duration" in x:
            duration = str(x).replace(" ", "").replace("b'", "").replace("'", "").split(",")
            duration = duration[0].split(":")
            seconds = duration[3]
            duration = int(duration[1])*60*60+int(duration[2])*60+float(seconds)
            return duration
        
def getMaxVolume(filename):
    result = subprocess.Popen(['ffmpeg', '-i', filename, '-af', 'volumedetect', '-vn', '-sn', '-dn', '-f', 'null', 'NULL'],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for x in result.stdout.readlines():
        if b"max_volume" in x:
            maxVolume = str(x).split(' ')[4]
            return float(maxVolume)

# Function to print text ands logs on the console with time and type information
# @Parameters :
#  toPrint  String
# @Return void
def doPrint(toPrint):
    type = "INFO"
    print("["+type+"]["+time.strftime("%H:%M:%S", time.localtime())+"] "+toPrint)


def doFFMPEG(toPrint):
    type = "INFO"
    print("["+type+"]["+time.strftime("%H:%M:%S", time.localtime())+"] "+toPrint, end="")
    #done = False
    #spin_thread = threading.Thread(target=spin_cursor)
    #spin_thread.start()
    #os.system(command)
    #done = True
    #spin_thread.join()

# Function to get an input from the user with a text with the format of the doPrint function
# @Parameters :
# toPrint   String
# @Return String
def doInput(toPrint):
    type = "INFO"
    if(toPrint != ""):
        doPrint(toPrint)
    # end = '' -> Make so that the print will not return to the line.
    # so that the input() instruction will run just after the print statement.
    print("["+type+"]["+time.strftime("%H:%M:%S", time.localtime())+"] >> ", end = '')
    return input()


# Function to display a list of choice from the given array in parameters
# and ask the user an option numer from 1 to the number of elements in the
# given array in parameters.
# @Parameters :
# choice    Array of String
# @Return int
def getChoiceList(choices):
    if(len(choices) < 1):
        return "err"
    i = 0
    # Display all of the choices availables with their option number.
    for choice in choices:
        i = i+1
        doPrint("["+str(i)+"] - " + choice)
    confirm_input = False

    # This part will ask the user until :
    # 1 - The user input is an int
    # 2 - The user input is between 1 and the number of options available
    while(confirm_input == False):
        user_input = doInput("")
        if(isInt(user_input)):
            user_input = int(user_input)
            if(user_input < 1 or user_input > i):
                doPrint("Incorrect option provided. Must be between 1 and " + str(i) + ".")
            else:
                confirm_input = True
                return user_input
        else:
            doPrint("Incorrect option provided." + " '"+str(user_input)+"' is not an int.")


# Function that exit the algorithm with an exit code of 0.
# Only purpose : Simplify the exit instruction.
def terminate():
    sys.exit(0)

# Function that check if a given path of a folder exists.
# @Parameters :
# path  String
# @Return Boolean
def folderExists(path):
    if(os.path.isdir(path)):
        if(os.path.exists(path)):
            return True
    return False

def fileExists(path):
    if(os.path.isfile(path)):
        if(os.path.exists(path)):
            return True
    return False

import ctypes  # An included library with Python install.
def msgbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def screenAnimation(base, font, from_point):
    from_point = from_point - 1.5
    from_end_animation_screen = from_point - 1.5
    to_end_animation_screen = from_point + 3
    base = movingEffectText("screenred", base, ".", font, "20", "0-w", "0", "h/2", "h/2", from_end_animation_screen, to_end_animation_screen, 3)
    base = movingEffectText("screenwhite", base, ".", font, "20", "0-w", "0", "h/2", "h/2", from_end_animation_screen + 0.5, to_end_animation_screen, 2.5)
    base = movingEffectText("screenred", base, ".", font, "20", "0-w", "0", "h/2", "h/2", from_end_animation_screen + 1, to_end_animation_screen, 2)
    base = movingEffectText("screenwhite", base, ".", font, "20", "0-w", "0", "h/2", "h/2", from_end_animation_screen + 1.5, to_end_animation_screen, 1.5)
    base = movingEffectText("screenred", base, ".", font, "20", "0-w", "0", "h/2", "h/2", from_end_animation_screen + 2, to_end_animation_screen, 1)

    base = movingEffectText("screenwhite", base, ".", font, "20", "w", "w*2", "h/2", "h/2", to_end_animation_screen, to_end_animation_screen + 1, 1)
    base = movingEffectText("screenred", base, ".", font, "20", "w", "w*2", "h/2", "h/2", to_end_animation_screen, to_end_animation_screen + 0.75, 0.75)
    base = movingEffectText("screenwhite", base, ".", font, "20", "w", "w*2", "h/2", "h/2", to_end_animation_screen, to_end_animation_screen + 0.5, 0.5)
    base = movingEffectText("screenred", base, ".", font, "20", "w", "w*2", "h/2", "h/2", to_end_animation_screen, to_end_animation_screen + 0.25, 0.25)
    return base

def movingEffectText(mode, base, content, font, fontsize, x1, x2, y1, y2, from_point, to_point, animationDuration):
    x1 = "(" + x1 + ")"
    x2 = "(" + x2 + ")"
    y1 = "(" + y1 + ")"
    y2 = "(" + y2 + ")"

    coor_animated = "x='x1+(x2-x1)*(t-t1)/(t2-t1)':y='y1+(y2-y1)*(t-t1)/(t2-t1)'"
    coor_animated = coor_animated.replace("x1", x1).replace("x2", x2)
    coor_animated = coor_animated.replace("y1", y1).replace("y2", y2)
    coor_animated = coor_animated.replace("t1", str(from_point)).replace("t2", str(from_point+animationDuration))
    shadow = "shadowcolor=black: shadowx=2: shadowy=2: "
    boxborder = ""
    color = "white"

    if mode != "":
        shadow = ""

    if mode == "title":
        boxborder = "box=1 :boxborderw=20: boxcolor=#00aeef :"
        
    if mode == "subtitle":
        boxborder = "box=1: boxborderw=15: boxcolor=white :"
        color = "black"

    if mode == "screenred":
        boxborder = "box=1 :boxborderw=1920: boxcolor=#00aeef :"
        shadow = "shadowcolor=#00aeef: shadowx=2: shadowy=2: "
        color = "red"
        
    if mode == "screenwhite":
        boxborder = "box=1 :boxborderw=1920: boxcolor=white :"
        shadow = "shadowcolor=white: shadowx=2: shadowy=2: "
        color = "white"

    if mode == "rankred":
        boxborder = "box=1 :boxborderw=5: boxcolor=#00aeef :"
        
    if mode == "rankwhite":
        boxborder = "box=1: boxborderw=10: boxcolor=white :"
        color = "black"

    base.append("drawtext=fontfile="+font+": text='"+content+"': fontcolor="+color+": fontsize="+fontsize+": "+shadow+boxborder+"enable='between(t,"+str(from_point)+","+str(from_point+animationDuration)+")': "+coor_animated)
    base.append("drawtext=fontfile="+font+": text='"+content+"': fontcolor="+color+": fontsize="+fontsize+": "+shadow+boxborder+"enable='between(t,"+str(from_point+animationDuration)+","+str(to_point)+")': x="+x2+": y="+y2)
    return base


def typingEffectTitle(base, text, begin, end, font, coor, fontsize, add):
    if(add == True):
        base.append("drawtext=fontfile="+font+": text='"+text+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(begin)+","+str(end)+")': "+coor)
        return base

    myend = end-3
    timespan = myend-begin
    if(timespan < 1):
        base.append("drawtext=fontfile="+font+": text='"+text+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(begin)+","+str(end)+")': "+coor)
        return base
    
    nb_cuts = int(timespan / 0.5)
    if(nb_cuts < 1):
        base.append("drawtext=fontfile="+font+": text='"+text+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(begin)+","+str(end)+")': "+coor)
        return base
    
    letter_per_part = int(len(text) / nb_cuts)
    if(letter_per_part < 1): letter_per_part = 1
    text_parts = textwrap.wrap(text.replace(' ', '_'), letter_per_part)
    
    if(len(text_parts) * 0.5 > timespan + 1):
        base.append("drawtext=fontfile="+font+": text='"+text+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(begin)+","+str(end)+")': "+coor)
        return base
    
    part_begin = begin
    part_end = part_begin
    to_display = ""
    for text_part in text_parts:
        part_begin = part_end + 0.0001
        part_end = part_begin + 0.5
        to_display = to_display + text_part.replace('_', ' ')
        base.append("drawtext=fontfile="+font+": text='"+to_display+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(part_begin)+","+str(part_end)+")': "+coor)
    
    base.append("drawtext=fontfile="+font+": text='"+text+"': fontcolor=white: fontsize="+str(fontsize)+": shadowcolor=black: shadowx=2: shadowy=2: enable='between(t,"+str(part_end)+","+str(part_end+3)+")': "+coor)
    #doPrint("Effect typing applied to " + text)    
    return base