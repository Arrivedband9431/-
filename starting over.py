import sys
import logging
'''
    Author: yali sommer
Program name: encryption/decrypt
Description:
    options to either encrypt decrypt flip-encrypt or flip-decrypt

Date: 2025-10-09

'''


encryption_dictionary = {
    "A": 56, "B":57,"C": 58,"D":59,"E": 40,"F": 41,"G": 42,"H": 43,"I": 44,"J": 45,"K": 46,"L": 47,"M": 48,"N": 49,"O":60,"P":61,"Q": 62,"R": 63,"S":64,"T":65,"U": 66,"V":67,"W": 68,"X":69,"Y":10,"Z":11,
    "a":12,"b":13,"c":14,"d":15,"e":16,"f":17,"g":18,"h":19,"i":30,"j":31,"k":32,"l":33,"m":34,"n":35,"o":36,"p":37,"q":38,"r":39,"s":90,"t":91,"u":92,"v":93,"w":94,"x":95,"y":96,"z":97,
    " ":98 ,",":99,".":100,"’":101,"!":102,"-":103
}

decrypt_dictionary = {
    56: "A",57: "B", 58: "C",59: "D",40:"E", 41: "F",42: "G",43:"H", 44: "I",45:"J",46: "K", 47: "L",48: "M", 49: "N",60:"O", 61: "P",62:"Q", 63:"R",64:"S",65: "T",66: "U",67: "V", 68:"W",69: "X",10:"Y", 11:"Z",
    12: "a",13: "b",14:"c",15:"d", 16:"e",17:"f", 18:"g",19: "h",30: "i",31: "j",32:"k",33:"l",34:"m",35:"n", 36:"o",37:"p",38: "q",39:"r", 90:"s",91:"t",92:"u",93: "v",94: "w", 95:"x",96:"y",97: "z",
    98: " ", 99: ",", 100: ".", 101: "’", 102: "!",103: "-"
}

LOG_FILE = "my_encryption.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# '''
# for nir how to run:
#
#
#
# step 1: open cmd
#
# step 2: mount the location of file in this case its the line below without the .
# cd C:\.Users\Your_Computers_name\PycharmProjects\Cyber
#
# step 3:  example of encrypting hello world
# python task_1_final.py "Hello world" 1
#
# the numbers represent what action you are doing so:
# 1 - encrypt
# 2 - decrypt
# 3 - flip-encrypt
# 4 - flip-decrypt
# 5 - auto tester
# '''


#-----------------------
# argv code
if len(sys.argv) < 2:
    print("Error: please provide a message!")
    sys.exit(1)
else:
    users_massage = sys.argv[1]

if len(sys.argv) > 2:
    option_chosen = int(sys.argv[2])
else:
    option_chosen = 1
# -----------------------


# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()






# users_massage = input(" Enter your massage: ")


def Encrypt(message):

    message_in_numbers = ""
    for i in message:


        message_in_numbers+=str(encryption_dictionary[i])+","
    logger.info("successful message encrypted message: " + message_in_numbers)
    return message_in_numbers


def Decrypt(message):
    note = ""
    message_in_letters = ""
    for i in message:
        if i != ",":
            note += i
        else:
            message_in_letters+= decrypt_dictionary[int(note)]
            note = ""
    logger.info("successful message decrypt message: " + message_in_letters)
    return message_in_letters





def main():
    assert Encrypt("this is a test") == "91,19,30,90,98,30,90,98,12,98,91,16,90,91,", "Encryption Failed"
    assert Decrypt("91,19,30,90,98,30,90,98,12,98,91,16,90,91,") == "this is a test" , "Decryption Failed"




    if option_chosen == 1:
        print(Encrypt(users_massage))
    elif option_chosen == 2:
        print(Decrypt(users_massage))
    else:
        print()
        logger.error("That is not an option!")


if __name__ == "__main__":
    main()
