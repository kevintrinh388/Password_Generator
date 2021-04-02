import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
specialChar = ["!","#","$","%","&","*","+","-","^","@","_","~"]

# Generates a number 0-9
def generate_num():
     return str(random.randint(0,9))
print("Welcome to Kevin T's password generator!")
print("Note: If few characters are chosen, there is a chance that one or more options will not be included in the password")

# Generates a letter a-z
def generate_letter():
    return alphabet[random.randint(0,25)]

# Generates a capital letter A-Z
def generate_cap_letter():
    return alphabet[random.randint(0,25)].upper()

# Generates a special character
def generate_special_character():
    return specialChar[random.randint(0,11)]

# Generates the password
def generate_password(characters):
    password = ""
    
    while len(password)<characters:
        randomGen = random.randint(0,3)
        if randomGen == 0:
            if numChoice:
                password += generate_num()
            elif numChoice == False:
                pass
        elif randomGen == 1:
            if letterChoice:
                password += generate_letter()
            elif letterChoice == False:
                pass
        elif randomGen == 2:
            if capChoice:
                password += generate_cap_letter()
            elif capChoice == False:
                pass
        elif randomGen == 3:
            if specialCharChoice:
                password += generate_special_character()
            elif letterChoice == False:
                pass     


    return str(password)



# Length check
lengthError = True
while lengthError:
    length = input("How many characters would you like your password to be? Please enter a number: ")
    if length.isdigit == False:
        print("Error: Input was not a number")
        lengthError = True
    else:
        lengthError = False

# Letters check
letterError = True
while letterError:
    letterChoice = input("Would you like your password to have letters? Type Y or N: ")
    if letterChoice == 'Y':
        letterChoice = True
        letterError = False
    elif letterChoice == 'N':
        letterChoice = False
        letterError = False
    else:
        print("Error: Input was not Y or N")
        letterError = True

# Capital check
capChoice = False
capError = True
if letterChoice == True:
    while capError:
        capChoice = input("Would you like your password to have capital letters? Type Y or N: ")
        if capChoice == 'Y':
            capChoice = True
            capError = False
        elif capChoice == 'N':
            capChoice = False
            capError = False
        else:
            print("Error: Input was not Y or N")
            capError = True

# Numbers check
numError = True
while numError:
    numChoice = input("Would you like your password to have numbers? Type Y or N: ")
    if numChoice == 'Y':
        numChoice = True
        numError = False
    elif numChoice == 'N':
        numChoice = False
        numError = False
    else:
        print("Error: Input was not Y or N")
        numError = True

# Special characters check
specialCharError = True
while specialCharError:
    specialCharChoice = input("Would you like your password to have special characters? Type Y or N: ")
    if specialCharChoice == 'Y':
        specialCharChoice = True
        specialCharError = False
    elif specialCharChoice == 'N':
        specialCharChoice = False
        specialCharError = False
    else:
        print("Error: Input was not Y or N ")
        specialCharError = True

print("Generating password....")
print("Password is: " + generate_password(int(length)))
input("Press ENTER to exit. Thanks for using Kevin T's Password Generator!")
