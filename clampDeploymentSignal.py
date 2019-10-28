import time
import threading
import requests 

class ClampSignalGenerator(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.running = True;
        self.id = id;
        self.URL = "http://localhost:3000/api/clamps/test" # api endpoint
            


    def run(self):
        print("running...");
        while self.running == True:
            self.sendAliveSignal();
            time.sleep(5);
            


    def switchState(self):
        if(self.running == False):
            self.running = True;
            print("state is now True!");
        else:
            self.running = False;
            print("state is now False!");
        
    def sendAliveSignal(self):
        #send alive signal
        print("alive from {}".format(self.id))
        try:
            r = requests.get(url = self.URL, data={id: self.id})
        except:
            print("An exception occurred")

    def sendClosedSignal(self):
        #send closed signal
        print("closed signal sent");
        try:
            r = requests.get(url = self.URL, data={id: self.id, status: "closed"})
        except:
            print("An exception occurred")
