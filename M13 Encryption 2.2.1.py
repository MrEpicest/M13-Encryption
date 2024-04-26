"""
m13 version 2.2.1
UPDATES:
    -added lines 19-33, 60-65, 96-99, 158-161, and 225-228
    -added to line 52: action != "?"
    -Entering '?' will display input options.
"""

import random
from tkinter import filedialog
import os
import atexit

alphabet = [" ", ",", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", "!", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "\n"]
location = os.path.dirname(__file__)
path = open(location + "\\path.txt", "a+")
path.seek(0)

q = {
    "encrypt": "choose a file for encryption.",
    "decrypt": "choose a file to decrypt",
    "revert": "choose an already-decrypted file to revert back to it's former state prior to decryption using the key that was used to decrypt it.",
    "end:": "ends the program."
}

createq = {
    "add": "create an encryption key file.",
    "exit": "exit to action"
}

selectq = {
    "add": "select an encryption key file.",
    "exit": "exit to action"
}


        

end = False
while not end:
    exit = False
    while not exit: 
        text = ""

####get action

        action = input("action>")
        if action == "exit":
                exit = True
        elif action == "end":
                exit = True
                end = True
        while (action != "?" and action != "revert" and action != "encrypt" and action != "decrypt" and not exit and not end):
            action = input("This is not a valid input. Please try again. \naction>")
            if action == "exit":
                exit = True
            elif action == "end":
                exit = True
                end = True

#####?

        if action == "?":
            for x, y in q.items():
                print("\n" + x + ": " + y)
            print("\n")



#####Encrypt 
           
        if action == "encrypt":
            print("action>encrypt>")
            try:
                file = filedialog.askopenfile(mode='a+', filetypes=[('Text Document', '*.txt')], title='Open')
            except:
                print("Error: no file selected")
            else:
                if file == None:
                    print("Error: no file was selected.")
                else:
                    file.seek(0)
                    text = str(file.read())
                    file.seek(0)
                    if text[:5] != "!m13!":
                        text = "!m13!0" + text

                    leave = False
                    while not exit:
                        while not leave and not exit:
                            keyAction = input("action>encrypt>key>")
                            if keyAction == "exit":
                                exit = True
                            elif keyAction == "end":
                                exit = True
                                end = True
                            elif keyAction == "?":
                                for x, y in createq.items():
                                    print("\n" + x + ": " + y)
                                print("\n")
                            elif keyAction != "add":
                                print("This is not a valid input.")
                            else:
                                try:
                                    keyFile = filedialog.asksaveasfile(filetypes=[('Privacy Enhanced Mail', '*.pem')], mode='w', defaultextension=[('Privacy Enhanced Mail', '*.pem')], title='Save As', initialfile='*.pem')
                                except:
                                    print("Error: no file was created.")
                                else:
                                    leave = True
                        leave = False
                        if not exit:
                            if keyFile == None:
                                print("Error: no file was created.")
                            else:
                                key = ""
                                b=6
                                while b<len(text):
                                    ran = random.randint(0, len(alphabet)-1) #the amount subtracted
                                    num = alphabet.index(text[b]) #index in alphabet of original letter in text
                                    newNum = num-ran #index in alphabet of substitute character
                                    newCharacter = alphabet[newNum] #substitute character
                                    text = text[:b] + newCharacter + text[b+1:]
                                    key = key + str(alphabet[ran]) #keep track of the amount subtracted
                                    b+=1
                                text = text[:5] + str(int(text[5]) + 1) + text[6:]
                                file.truncate(0)
                                file.write(text)
                                file.seek(0)
                                keyFile.write(key)
                                keyFile.close()
                                print("file successfully encrypted.")
                    file.close()

#####Decrypt

        if action == "decrypt":
            print("action>decrypt>")
            try:
                file = filedialog.askopenfile(mode='a+', filetypes=[('Text Document', '*.txt')], title='Open')
            except:
                print("Error: no file selected")
            else:
                if file == None:
                    print("Error: no file was selected.")
                else:
                    file.seek(0)
                    text = str(file.read())
                    file.seek(0)
                    if text[:5] != "!m13!":
                        print("Error: chosen file was not encrypted using m13.")
                    else:
                        while not exit and text[:5] == "!m13!":
                            keyAction = input("action>decrypt>key>")
                            if keyAction == "exit":
                                exit = True
                            elif keyAction == "end":
                                exit = True
                                end = True
                            elif keyAction == "?":
                                for x, y in selectq.items():
                                    print("\n" + x + ": " + y)
                                print("\n")
                            elif keyAction != "add":
                                print("This is not a valid input.")
                            else:
                                try:
                                    keyFile = filedialog.askopenfile(mode='a+', filetypes=[('Privacy Enhanced Mail', '*.pem')], title='Open')
                                except:
                                    print("Error: no file was selected.")
                                else:
                                    if keyFile == None:
                                        print("Error: no file was selected.")
                                    else:
                                        keyFile.seek(0)
                                        key = keyFile.read()
                                        keyFile.seek(0)
                                        print("Decrypting...")
                                        vnum = int(text[5])
                                        text = text[6:]
                                        print(text[6:])
                                        b=0
                                        while b<len(text):
                                            num = alphabet.index(text[b])
                                            add = alphabet.index(key[b]) #amount to be added
                                            newNum = num + add
                                            if newNum > len(alphabet)-1:
                                                newNum = newNum - (len(alphabet))
                                            newCharacter = alphabet[newNum]
                                            text = text[:b] + newCharacter + text[b+1:]
                                            b+=1
                                        if vnum > 1:
                                            text = "!m13!" + str(vnum-1) + text
                                        file.truncate(0)
                                        file.write(text)
                                        file.seek(0)
                                        print("file successly decrypted.")
                        file.close()

######revert

        if action == "revert":
            print("action>revert>")
            try:
                file = filedialog.askopenfile(mode='a+', filetypes=[('Text Document', '*.txt')], title='Open')
            except:
                print("Error: no file selected")
            else:
                if file == None:
                    print("Error: no file was selected.")
                else:
                    file.seek(0)
                    text = str(file.read())
                    file.seek(0)
                    if text[:5] == "!m13!":
                        vmnum = text[5]
                        text = text[6:]
                    else:
                        vnum = 0
                    while not exit and text[:5] != "!m13!":
                        keyAction = input("action>revert>key>")
                        if keyAction == "exit":
                            exit = True
                        elif keyAction == "end":
                            exit = True
                            end = True
                        elif keyAction == "?":
                                for x, y in selectq.items():
                                    print("\n" + x + ": " + y)
                                print("\n")
                        elif keyAction != "add":
                            print("This is not a valid input.")
                        else:
                            try:
                                keyFile = filedialog.askopenfile(mode='a+', filetypes=[('Privacy Enhanced Mail', '*.pem')], title='Open')
                            except:
                                print("Error: no file was selected.")
                            else:
                                if keyFile == None:
                                    print("Error: no file was selected.")
                                else:
                                    keyFile.seek(0)
                                    key = keyFile.read()
                                    keyFile.seek(0)
                                    print("Decrypting...")
                                    b=0
                                    while b<len(text):
                                        num = alphabet.index(text[b])
                                        sub = alphabet.index(key[b]) #amount to be subtracted
                                        newNum = num - sub
                                        newCharacter = alphabet[newNum]
                                        text = text[:b] + newCharacter + text[b+1:]
                                        b+=1
                                    text = "!m13!" + str(vnum+1) + text
                                    file.truncate(0)
                                    file.write(text)
                                    file.seek(0)
                                    print("file successly decrypted.")
                        file.close()
        #########

def close():
    try:
        file.close()
    except:
        x=0
    try: 
        keyFile.close()
    except:
        x=0

atexit.register(close)