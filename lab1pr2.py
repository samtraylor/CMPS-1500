#program by Sam Traylor, written Jan 28 2019, function is to format an entered date into mm/dd/yyyy

origdate = input("Please enter date in MM/DD/YYYY format:")
newdate = ""

if (origdate[1] == "/"): #if a zero needs to be inserted
    origdate = "0" + origdate
if (origdate[4] == "/"): #if 5th char is / instead of the 2nd digit in a 2-dig #
    origdate = origdate[0:3] + "0" + origdate[3:] #we need another 0, so we add it

origdate = origdate[3:6] + origdate[0:3] + origdate[6:] #switch month and day sections

newdate = origdate 
newdate = newdate[0:2] + "." + newdate[3:5] + "." + newdate[6:]

print(" Here is the formatted date:" + " " + newdate )
