class MilClock:
    def __init__(self,h,m):
        self.hours = h
        self.minutes = m
    def __repr__(self):
        return str(self.hours) + ':' + str(self.minutes)
    def addOne(self):
        self.minutes = str(int(self.minutes) + 1)
        if int(self.minutes) == 60:
            if int(self.hours) == 23:
                self.hours = '00'
            else:
                self.hours = str(int(self.hours) + 1)
            self.minutes = '00'
            
        if int(self.minutes) > 0 and int(self.minutes) < 10:
            self.minutes = '0' + str(self.minutes)
        if int(self.hours) > 0 and int(self.minutes) < 10:
            self.hours = '0' + str(self.minutes)
    
