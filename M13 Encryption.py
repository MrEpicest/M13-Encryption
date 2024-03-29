import random

alphabet = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

action = input("Would you like to encrypt or decrypt a message? (type \"encrypt\" or \"decrypt\")")
while (action != "encrypt" and action != "decrypt"):
  action = input("This is not a valid input. Please try again: ")

if action == "encrypt":
    message = input("Please enter your message: ")
    exit = False
    while not exit:
        try:
            numKeys = int(input("Please specify how many encryption keys you would like: "))
        except:
            print("This is not a valid input.")
        else:
            exit = True
    exit = False
    """cryptabet = input("Would you like a second layer cryptabet to be generated for your keys? (y/n) ")
    while (cryptabet != "y" and cryptabet != "n"):
    cryptabet = input("This is not a valid input. Please try again: ")"""
    keys = [""]*numKeys #needs to be length of numKeys
    #print(keys)
    a=numKeys-1

    while a>=0:
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
            print("b: " + str(b))
            print("alphabet[ran]: " + alphabet[ran])
            print(key)
            key = key + str(alphabet[ran]) #keep track of the amount subtracted
            b+=1
        keys[a] = key
        a-=1
    print("\nEncrypted message: \"" + message + "\"")
    a=1
    for x in keys:
        print("\nKey #" + str(a) + ": \"" + str(x) + "\"")
        a+=1
    print(str(len(message)) + "\n" + str(len(keys[0])))




if action == "decrypt":
    message = input("Please enter the ciphertext: ")
    exit = False
    while not exit:
        try:
            numKeys = int(input("Please specify how many encryption keys you have: "))
        except:
            print("This is not a valid input.")
        else:
            exit = True
    exit = False
    keys = [""]*numKeys
    a=0
    while a<numKeys:
        keys[a] = input("Please enter encryption key #" + str(a+1) + " ")
        while (len(keys[a]) != len(message)):
            print(str(len(message)) + "\n" + str(len(keys[a])))
            keys[a] = input("This key is not the proper length. Please re-enter encyption key #" + str(a+1) + " ")
        a+=1
    a=0
    while a<len(keys):
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
    print("\nDecrypted message: ", message)
    