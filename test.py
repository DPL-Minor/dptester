from tkinter import *
from clampDeploymentSignal import *

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.createWidgets();
        self.clamps = []
        
    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT', command=self.quit).grid(row=0,column=0)

        self.start = Button(self)
        self.start["text"] = "create new CSG",
        self.start["command"] = self.createCSG;
        self.start.grid(row=1,column=0)


    def createCSG(self):
        print("creatings csg")
        for id in range(100):
            self.clamps.append(ClampSignalGenerator(id))

        for clamp in self.clamps:
            print(clamp.id)

        for clamp in self.clamps:
            clamp.start();

    def test(self):
        print("test succesfull")

    def stop(self):
        print("stop succesfull")

    

root = Tk()
app = GUI(master=root)
app.mainloop()


root.destroy()
