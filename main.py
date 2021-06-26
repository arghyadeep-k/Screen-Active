import time
import ctypes
from tkinter import *
import threading #import Thread,Event
from pynput.keyboard import Controller

win = Tk()
keyboard = Controller()
delay = StringVar() 

i = 0
w = None

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)        
        self.stopThread = threading.Event() 
        
    def run(self):        
        delayInt = int(delay.get())   
        while not self.stopThread.isSet():
            keyboard.press('c')
            keyboard.release('c')
            self.stopThread.wait(delayInt)
            
    def stop(self):         
        self.stopThread.set()
       

     
def startKeyPress(): 
    global w
    global submitButton
    global stopButton
    w = Worker()
    w.start()
    delayEntry.configure(state='disabled')
    submitButton.destroy()
    stopButton = Button(text="Stop", command=stopKeyPress)
    stopButton.place(x=55, y=55)
    win.update()
    

def stopKeyPress():
    global w
    global submitButton
    global stopButton
    w.stop()
    delayEntry.configure(state='normal')        
    stopButton.destroy()
    submitButton = Button(text="Submit", command=startKeyPress)
    submitButton.place(x=25, y=55)
    win.update()
    
   

delayLabel = Label(win, text="Enter Delay (in sec):")

delayEntry = Entry(win, textvariable=delay, width=20)

submitButton = Button(text="Submit", command=startKeyPress)
stopButton = Button(text="Stop", command=stopKeyPress)

delayLabel.place(x=25, y=25)
delayEntry.place(x=140, y=25)
submitButton.place(x=25, y=55)

# Set Title
win.title("Mouse Active")
# Set the geometry of tkinter frame
win.geometry("300x250")
# Disallow resizing
win.resizable(0, 0)
win.mainloop()




