#program by Sam Traylor, written Jan 28 2019, function is to format an entered date into written form

origdate = input("Please enter date in MM/DD/YYYY format:")
newdate = ""
Months = ['January','February','March','April','May','June','July','August','September','October','November','December']
mon = 0
formatted = ""
if (origdate[1] == "/"): #if a zero needs to be inserted
    origdate = "0" + origdate
if (origdate[4] == "/"): #if 5th char is / instead of the 2nd digit in a 2-dig #
    origdate = origdate[0:3] + "0" + origdate[3:] #we need another 0, so we add it

newdate = origdate

if newdate[0] == "0":
    mon = int(newdate[1:2])
else:
    mon = int(newdate[0:2])
        
formatted = Months[mon - 1] + " " + newdate[3:5] + ", " + newdate[6:]


print(" Here is the formatted date:" + " " + formatted )
