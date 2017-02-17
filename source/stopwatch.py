
import datetime

class Stopwatch:
    def __init__(self, startTimer=False):
        self.stored = datetime.timedelta()
        self.running = False
        if startTimer:
            self.start()

    def start(self):
        self.stored = datetime.timedelta()
        self.startTime = datetime.datetime.now()
        self.running = True

    def pause(self):
        self.stored += datetime.datetime.now() - self.startTime
        self.running = False
    
    def unpause(self):
        self.startTime = datetime.datetime.now() - self.stored
        self.stored = datetime.timedelta()
        self.running = True

    def check(self):
        if self.running:
            return datetime.datetime.now() - self.startTime
        else:
            return self.stored
            
        
