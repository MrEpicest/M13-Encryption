import random
end = False
while not end:
    exit = False
    while not exit:
        alphabet = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

        action = input("Would you like to encrypt or decrypt a message? (enter \"encrypt\" or \"decrypt\") ")
        if action == "exit":
                exit = True
        elif action == "end":
                exit = True
                end = True
        while (action != "encrypt" and action != "decrypt" and not exit and not end):
            action = input("This is not a valid input. Please try again: ")
            if action == "exit":
                exit = True
            elif action == "end":
                exit = True
                end = True

        if action == "encrypt":
            message = input("Please enter your message: ")
            if message == "exit":
                exit = True
            elif message == "end":
                exit = True
                end = True
            leave = False
            while not leave and not exit:
                numKeys = input("Please specify how many encryption keys you would like: ")
                try:
                    numKeys = int(numKeys)
                except:
                    if numKeys == "exit":
                        exit = True
                    elif numKeys == "end":
                        exit = True
                        end = True
                    else:
                        print("This is not a valid input.")
                else:
                    leave = True
                    print("Encrypting...")
            leave = False
            """cryptabet = input("Would you like a second layer cryptabet to be generated for your keys? (y/n) ")
            while (cryptabet != "y" and cryptabet != "n"):
            cryptabet = input("This is not a valid input. Please try again: ")"""
            a=0
            if not exit:
                keys = [""]*numKeys #needs to be length of numKeys
            #print(keys)
                a=numKeys-1
            while a>=0 and not exit:
                key = ""
                b=0
                while b<len(message):
                    ran = random.randint(0, len(alphabet)-1) #the amount subtracted
                    num = alphabet.index(message[b]) #index in alphabet of original letter in message
                    newNum = num-ran #index in alphabet of substitute character
                    """if newNum < 0:
                        newNum = len(alphabet)-1 + newNum"""
                    newCharacter = alphabet[newNum] #substitute character
                    #print(message[b])
                    #print(newCharacter)
                    message = message[:b] + newCharacter + message[b+1:]
                    #print(message)
                    #print("b: " + str(b))
                    #print("alphabet[ran]: " + alphabet[ran])
                    #print(key)
                    key = key + str(alphabet[ran]) #keep track of the amount subtracted
                    b+=1
                keys[a] = key
                a-=1
            a=1
            if not exit:
                print("\nEncrypted message: \"" + message + "\"")
                for x in keys:
                    print("\nKey #" + str(a) + ": \"" + str(x) + "\"")
                    a+=1
                #print(str(len(message)) + "\n" + str(len(keys[0])))




        if action == "decrypt":
            message = input("Please enter ciphertext: ")
            if message == "exit":
                exit = True
            elif message == "end":
                exit = True
                end = True
            leave = False
            while not leave and not exit:
                numKeys = input("Please specify how many encryption keys you have: ")
                try:
                    numKeys = int(numKeys)
                except:
                    if numKeys == "exit":
                        exit = True
                    elif numKeys == "end":
                        exit = True
                        end = True
                    else:
                        print("This is not a valid input.")
                    numKeys = 0
                else:
                    leave = True
            leave = False
            keys = [""]
            if not exit:
                keys = [""]*numKeys
            a=0
            while a<numKeys and not exit:
                keys[a] = input("Please enter encryption key #" + str(a+1) + " ")
                if keys[a] == "exit":
                    exit = True
                elif keys[a] == "end":
                    exit = True
                    end = True
                while (len(keys[a]) != len(message)) and not exit:
                    #print(str(len(message)) + "\n" + str(len(keys[a])))
                    keys[a] = input("This key is not the proper length. Please re-enter encyption key #" + str(a+1) + " ")
                    if keys[a] == "exit":
                        exit = True
                    elif keys[a] == "end":
                        exit = True
                        end = True
                a+=1
            if not exit:
                print("Decrypting...")
            a=0
            while a<len(keys) and not exit:
                key = keys[a]
                b=0
                while b<len(key):
                    num = alphabet.index(message[b])
                    add = alphabet.index(key[b]) #amount to be added
                    newNum = num + add
                    if newNum > len(alphabet)-1:
                        newNum = newNum - (len(alphabet))############################-1
                    newCharacter = alphabet[newNum]
                    message = message[:b] + newCharacter + message[b+1:]
                    b+=1
                a+=1
            if not exit:
                print("\nDecrypted message: ", message)
        if not end:
            blank = input()
            if blank == "end":
                end = True