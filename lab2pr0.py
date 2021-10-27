#Written by Sam Traylor and Will Bush, Jan 31 2019
# wbush@tulane.edu
usr_inpt = input("Please enter a phrase: ")
finalstr = ""
listform = []
i = 0
j = 0

while i < len(usr_inpt):
    if i == 0:
        finalstr += usr_inpt[i]
        i += 1
        continue
    
    if usr_inpt[i] == "," or usr_inpt[i] == "!" or usr_inpt[i] == ":" or usr_inpt[i] == "?" or usr_inpt[i] == "." or usr_inpt[i] == ";":
        finalstr += usr_inpt[i] #add the punctuation to final
        if (i+2) < len(usr_inpt): #if first letter of next word isn't out of range
            finalstr += usr_inpt[i + 2] #add first letter of next word to final
            i += 2
            
    if usr_inpt[i] == " " and len(usr_inpt) > i+1 :    #if index is at a space
            finalstr += usr_inpt[i + 1] #add first letter of next word
            
    i += 1
    
while j < len(finalstr):
    if finalstr[j] == "o" or finalstr[j] == "O":  #if o, add 0 
        listform.append('0')
    elif finalstr[j] == "a": #if a, add @
        listform.append("@")
    elif finalstr[j] == "l": #if i, add 1
        listform.append("1")
    else:
        listform.append(finalstr[j])
    j += 1
    
finalstr = ""    #clear variable
for x in listform:
    finalstr += x #adds everything to the list
    
print(finalstr)
