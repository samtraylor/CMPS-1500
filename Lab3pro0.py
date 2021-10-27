#Sam Traylor, February 11. This program calculates average amount of heartbeats and yawns in a person's lifetime
minsinyear = 525600
heartbts = 0
yawnz = 0
days = 0

age = int(input("Enter your age in years: "))
def heartbeats(age):
    heartbts = minsinyear * age
    heartbts *= 72
    return heartbts
    
def yawns(age):
    days = age * 365
    yawnz = 5 * days
    return yawnz

print(heartbeats(age), "heartbeats and", yawns(age), "yawns so far")
