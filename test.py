from tkinter import *
from clampDeploymentSignal import *
import random

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.createWidgets();
        self.clamps = []
        
    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT the application', command=self.quit).grid(row=0,column=0)
        self.create = Button(self, text='create new CSG', command=self.createCSG).grid(row=1,column=0)
        self.stopOne = Button(self, text='Stop one', command=self.stopOne).grid(row=2,column=0)
        self.stopAll = Button(self, text='Stop all', command=self.stopAll).grid(row=3,column=0)
        self.startAll = Button(self, text='Start all', command=self.startAll).grid(row=4,column=0)
        self.closeOne = Button(self, text='close one', command=self.closeOne).grid(row=5,column=0)
        


    def createCSG(self):
        print("creatings csg")
        for id in range(10):
            self.clamps.append(ClampSignalGenerator(id))

        for clamp in self.clamps:
            print(clamp.id)

        for clamp in self.clamps:
            clamp.start();

    

    def stopOne(self):
        r = random.randint(0,9);
        self.clamps[r].switchState();
        print("shut down Generator {} succesfully".format(r));

    def stopAll(self):
        for clamp in self.clamps:
            clamp.switchState();
        
        print("shut down all generators succesfully");

    def startAll(self):
        for clamp in self.clamps:
            clamp.switchState();

    def closeOne(self):
        r = random.randint(0,9);
        self.clamps[r].switchState();
        self.clamps[r].sendClosedSignal();

    

root = Tk()
app = GUI(master=root)
app.mainloop()


root.destroy()
