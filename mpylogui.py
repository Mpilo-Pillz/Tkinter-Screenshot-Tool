from tkinter import *
from time import localtime, strftime

import pyautogui


class mpygui:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quitButton = Button(frame, text="Stop", command=frame.quit)
        self.quitButton.pack(side=LEFT)

        self.printButton = Button(frame, text="Take Screen Shot", command=self.startScreenShotTool)
        self.printButton.pack(side=LEFT)

    print('Please click on the \"Take ScreenShot Button\"!')
    def startScreenShotTool(self):
        todaysdate = str(strftime(" - %d %b %Y - %H %M %S"))

        # Save the screenshot in a folder and save the image using current date, time (hh:mm:ss)
        img = pyautogui.screenshot('/home/mpilopillz/Documents/testscreen/%s.png' % (todaysdate))



root = Tk()
b = mpygui(root)
root.title("Screen Shot Taker")
root.mainloop()