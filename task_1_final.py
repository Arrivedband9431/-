'''
    Author: yali sommer
Program name: encryption/decrypt
Description:
    options to either encrypt decrypt flip-encrypt or flip-decrypt

Date: 2025-10-09

'''


import sys
#----------------------------------------------
# value sending argv

#for getting the massage
if len(sys.argv) > 1:
    users_massage = sys.argv[1]
    print("Error: please provide a message!")
    sys.exit(1)



#for getting what choose you made
if len(sys.argv) > 2:
    option_chosen = int(sys.argv[2])
else:
    option_chosen = 1
#----------------------------------------------



#--
'''
for nir how to run:



step 1: open cmd

step 2: mount the location of file in this case its the line below without the .
cd C:\.Users\Your_Computers_name\PycharmProjects\Cyber

step 3:  example of encrypting hello world
python task_1_final.py "Hello world" 1

the numbers represent what action you are doing so:
1 - encrypt
2 - decrypt
3 - flip-encrypt
4 - flip-decrypt
5 - auto tester 
'''

#--




#-----------------------------------------------------------
# ----- manual input


# def encrypt_or_decrypt():
#     while True:
#         try:
#             option_chooser = int(input("do you want to encrypt or decrypt?\nenter 1-for encrypt or 2-for decrypt 3-for flip encryption:\n "))
#             assert option_chooser == 1 or option_chooser == 2 or option_chooser == 3 or option_chooser ==4, "Enter 1 2 3 or 4 please."
#             return option_chooser
#
#
#         except ValueError:
#             print("\n Invalid input enter a number")


#option_chosen = encrypt_or_decrypt()

#---------
#-----------------------------------------------------------





encryption_dictionary = {
    "A": 56, "B":57,"C": 58,"D":59,"E": 40,"F": 41, "G": 42,"H": 43,"I": 44,"J": 45,"K": 46,"L": 47,"M": 48,"N": 49,"O":60,"P":61,"Q": 62,"R": 63,"S":64,"T":65,"U": 66,"V":67,"W": 68,"X":69,"Y":10,"Z":11,
    "a":12,"b":13,"c":14,"d":15,"e":16,"f":17,"g":18,"h":19,"i":30,"j":31,"k":32,"l":33,"m":34,"n":35,"o":36,"p":37,"q": 38, "r": 39, "s":90,"t":91,"u":92,"v":93,"w":94,"x":95,"y":96,"z":97,
    " ":98 ,",":99,".":100,"’":101,"!":102,"-":103
}


decrypt_dictionary = {
    56: "A",57: "B", 58: "C",59: "D",40:"E", 41: "F",42: "G",43:"H", 44: "I",45:"J",46: "K", 47: "L",48: "M", 49: "N",60:"O", 61: "P",62:"Q", 63:"R",64:"S",65: "T",66: "U",67: "V", 68:"W",69: "X",10:"Y", 11:"Z",
    12: "a",13: "b",14:"c",15:"d", 16:"e",17:"f", 18:"g",19: "h",30: "i",31: "j",32:"k",33:"l",34:"m",35:"n", 36:"o",37:"p",38: "q",39:"r", 90:"s",91:"t",92:"u",93: "v",94: "w", 95:"x",96:"y",97: "z",
    98: " ", 99: ",", 100: ".", 101: "’", 102: "!",103: "-"
}




#-------------------------------------------
def encrypt(massage):
    list1= []
    for i in massage:
        try:
            letter_switch= encryption_dictionary[i]
            list1.append(letter_switch)
            print(letter_switch, end=',')
        except KeyError:
            list1.append(" symbol not part of the Encryption ")
#-------------------------------------------



#-------------------------------------------
def decrypt(massage):
    list2= []
    note = ""
    for i in massage:
        if i==",":
            assert int(note),"Cant be turned into a number"
            number= int(note)

            list2.append(number)
            note = ""
        else:
            note+=i

    decrypted_massage_list =[]
    for i in list2:
        decrypted_massage_list.append(decrypt_dictionary[i])
        print(decrypt_dictionary[i],end="")

    list3 = []
    for i in list2:
        try:
            letter_switch= decrypt_dictionary[i]
            list3.append(letter_switch)
        except KeyError:
            list2.append(" symbol not part of the Encryption ")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
#-------------------------------------------






#-------------------------------------------
def flip_encryption(massage):
    list1= []
    for i in massage:
        try:
            letter_switch= encryption_dictionary[i]
            list1.append(letter_switch)
        except KeyError:
            list1.append(" symbol not part of the Encryption ")

    list1.reverse()
    for i in list1:
        print(i,end=',')
#-------------------------------------------







#-------------------------------------------
def decrypt_with_flip(massage):
    list2= []
    note = ""
    for i in massage:
        if i==",":
            assert int(note),"Cant be turned into a number"
            number= int(note)

            list2.append(number)
            note = ""
        else:
            note+=i

    decrypted_massage_list =[]
    for i in list2:
        decrypted_massage_list.append(decrypt_dictionary[i])
    list3 = []
    for i in list2:
        try:
            letter_switch= decrypt_dictionary[i]
            list3.append(letter_switch)
        except KeyError:
            list2.append(" symbol not part of the Encryption ")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    list3.reverse()
    for i in list3:
        print(i,end='')
#-------------------------------------------





def tester_if_working(): # check if code is working and if code is running ok
    try:
        option_chosen =1 # place 1 2 3 or 4 for what ever you want to test
        users_massage = "enter here your massage" #numbers if its 2 or 4 letters if its 1 or 3
        if option_chosen == 1:
            encrypt(users_massage)
        elif option_chosen == 2:
            decrypt(users_massage)
        elif option_chosen == 3:
            flip_encryption(users_massage)
        elif option_chosen == 4:
            decrypt_with_flip(users_massage)
    except ValueError:
        print("Invalid input. change it and try again")
    except Exception as failed_error:
        print(f"the error was {failed_error}")
    finally:
        print()




#users_massage =input("enter your massage Encryption:\n       ")
if option_chosen == 1:
    encrypt(users_massage)
elif option_chosen == 2:
    decrypt(users_massage)
elif option_chosen == 3:
    flip_encryption(users_massage)
elif option_chosen == 4:
    decrypt_with_flip(users_massage)
elif option_chosen == 5:
    tester_if_working()