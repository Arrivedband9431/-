import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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


def encrypt(massage):
    list1=[]
    for i in massage:
        code = encryption_dictionary.get(i,"?")
        list1.append(str(code))
        logging.info(f"Encrypt '{i}' -> {code}")
    result=",".join(list1)
    logging.info(f"Encrypted message: {result}")
    return result

def decrypt(massage):
    list2=[]
    note=""
    for i in massage:
        if i==",":
            if note.strip()=="":
                note=""
                continue
            try:
                list2.append(int(note))
            except ValueError:
                logging.warning(f"Wrong number: {note}")
            note=""
        else:
            note+=i
    if note.strip():
        try:
            list2.append(int(note))
        except ValueError:
            logging.warning(f"Wrong number: {note}")
    decrypted=""
    for i in list2:
        decrypted+=decrypt_dictionary.get(i,"?")
        logging.info(f"Decrypt {i} -> '{decrypt_dictionary.get(i,'?')}'")
    logging.info(f"Decrypted message: {decrypted}")
    return decrypted

def flip_encryption(massage):
    list1=[]
    for i in massage:
        code = encryption_dictionary.get(i,"?")
        list1.append(str(code))
        logging.info(f"Encrypt '{i}' -> {code}")
    list1.reverse()
    result=",".join(list1)
    logging.info(f"Flip encrypted message: {result}")
    return result

def decrypt_with_flip(massage):
    list2=[]
    note=""
    for i in massage:
        if i==",":
            if note.strip()=="":
                note=""
                continue
            try:
                list2.append(int(note))
            except ValueError:
                logging.warning(f"Wrong number: {note}")
            note=""
        else:
            note+=i
    if note.strip():
        try:
            list2.append(int(note))
        except ValueError:
            logging.warning(f"Wrong number: {note}")
    decrypted=""
    for i in reversed(list2):
        decrypted+=decrypt_dictionary.get(i,"?")
        logging.info(f"Decrypt {i} -> '{decrypt_dictionary.get(i,'?')}'")
    logging.info(f"Flip decrypted message: {decrypted}")
    return decrypted

def encrypt_or_decrypt():
    while True:
        try:
            option=int(input("Enter 1-encrypt 2-decrypt 3-flip encrypt 4-flip decrypt:\n"))
            if option in [1,2,3,4]:
                return option
        except ValueError:
            pass

def main():
    users_massage=input("Enter your message: ")
    option=encrypt_or_decrypt()
    if option==1:
        encrypt(users_massage)
    elif option==2:
        decrypt(users_massage)
    elif option==3:
        flip_encryption(users_massage)
    elif option==4:
        decrypt_with_flip(users_massage)

if __name__=="__main__":
    assert encrypt("this is a test"), "encryption failed"
    assert decrypt("91,19,30,90,98,30,90,98,12,98,91,16,90,91,98"), "decryption failed"
    assert flip_encryption("this is a test"), "flip encrypt failed"
    assert decrypt_with_flip("91,19,30,90,98,30,90,98,12,98,91,16,90,91,98"), "flip decrypt failed"
    main()
