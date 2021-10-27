#Sam Traylor and Matt Hogan, Jan 24 2019. Program converts seconds into minutes and hours

sec = 0
hours = 0
minut = 0
minute = ""
hour = ""
second = ""

inp = int(input("Please enter the number of seconds:"))
if inp < 60:
    if inp != 1:
        print(str(inp) + " seconds")
    if inp == 1:
        print(str(inp) + " second")
    
if inp > 59 and inp < 3600:
    minut = (inp // 60)
    sec = (inp % 60)
    if minut == 1:
        minute = " minute"
        if sec != 0:
            minute = minute + " "
    if minut > 1:
        minute = " minutes"
        if sec != 0:
            minute = minute + " "
    if sec != 0 and sec != 1:
        second = " seconds"
    if sec !=0 and sec == 1:
        second = " second"
    if sec ==  0:
        sec = ""
    
    print(str(minut) + minute + str(sec) + second)
          
if inp > 3599:
    hours = (inp // 3600)
    minut = (inp % 3600) // 60
    sec = (inp % 3600) % 60
    if hours == 1:
        hour = " hour"
        if (minut != 0) or (sec != 0):
            hour = hour + " "
    if hours > 1:
        hour = " hours"
        if (minut != 0) or (sec != 0):
            hour = hour + " "
    if minut == 1:
        minute = " minute"
        if (sec != 0):       #if something else comes after, put space
            hour = hour + " "
    if minut > 1:
        minute = " minutes"
        if (sec != 0):       #if something else comes after, put space
            hour = hour + " "
    if minut == 0:
        minut = ""
    if sec == 1:
        second = " second"
    if sec > 1:
        second = " seconds"
    if sec == 0:
        sec = ""
    print(str(hours) + hour + str(minut) + minute + str(sec) + second)
    

          
