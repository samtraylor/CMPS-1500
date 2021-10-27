#Written by Sam Traylor, January 28. A program to convert SSN # into user friendly notation

inpt = input("Please enter SSN: ")

realssn = False
new_ssn = ""

if len(inpt) == 9:
    realssn = True
else:
    print("Incorrect SSN length.")
    
if realssn == True:
    new_ssn = inpt[0:3] + "-" + inpt[3:5] + "-" + inpt[5:]
    print(new_ssn)
    
