#Written by Sam Traylor on Feb 6, 2019. Program is designed to hide entered passwords

password = []
asterisks = []
passw = ""

while True:
    passw = (input('Please enter a password (press [enter] to finish): '))
    
    if passw == "":
        for i in password:
            asterisks.append('*' * len(i))
        print(password)
        print(asterisks)
        break

    else:
        password.append(passw)
        
