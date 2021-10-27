class MilClock:
    def __init__(self,h,m):
        self.hours = h
        self.minutes = m
    def __repr__(self):
        if int(self.minutes) >= 60:
            self.minutes = str(int(self.minutes) - 60)
            self.hours = str(int(self.hours) + 1)
        if int(self.hours) == 24:
            self.hours = '00'
            
        if str(self.minutes) == '0':
            self.minutes = '0' + str(self.minutes)
        if str(self.hours) == '0':
            self.hours = '0' + str(self.hours)
            
        if len(str(self.minutes)) < 2:
            self.minutes = '0' + str(self.minutes)
        if len(str(self.hours)) < 2:
            self.hours = '0' + str(self.hours)
        
        return str(self.hours) + ':' + str(self.minutes)
    def addOne(self):
        self.minutes = str(int(self.minutes) + 1)
       
