import time
import ctypes
from tkinter import *
import threading #import Thread,Event
from pynput.keyboard import Controller

win = Tk()
keyboard = Controller()
delay = StringVar() 

global w 

class Worker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)        
        self.stopThread = threading.Event() 
        self.name = name        
        
    def run(self):        
        delayInt = int(delay.get())   
        while not self.stopThread.isSet():
            keyboard.press('c')
            keyboard.release('c')
            time.sleep(delayInt)               
    
    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
                
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
            
    def stop(self):        
        self.stopThread.set()
       

     
def startPressing():
    w = Worker('KeyPress Thread')
    w.start()
    delayEntry.configure(state='disabled')
    submitButton.destroy()
    stopButton.place(x=25, y=55)
    win.update()
    

def stopPressing():
    #w.stop()
    w.raise_exception()
    w.join()
    delayEntry.configure(state='normal')    
    stopButton.destroy()
    submitButton = Button(text="Submit", command=startPressing)
    submitButton.place(x=25, y=55)
    win.update()
    
   

delayLabel = Label(win, text="Enter Delay (in sec):")

delayEntry = Entry(win, textvariable=delay, width=20)

submitButton = Button(text="Submit", command=startPressing)
stopButton = Button(win, text="Stop", command=stopPressing)

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




