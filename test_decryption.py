decrypt_dictionary = {
    56: "A",57: "B", 58: "C",59: "D",40:"E", 41: "F",42: "G",43:"H", 44: "I",45:"J",46: "K", 47: "L",48: "M", 49: "N",60:"O", 61: "P",62:"Q", 63:"R",64:"S",65: "T",66: "U",67: "V", 68:"W",69: "X",10:"Y", 11:"Z",
    12: "a",13: "b",14:"c",15:"d", 16:"e",17:"f", 18:"g",19:"h",30: "i",31: "j",32:"k",33:"l",34:"m",35:"n", 36:"o",37:"p",38: "q",39:"r", 90:"s",91:"t",92:"u",93: "v",94: "w", 95:"x",96:"y",97: "z",
    98: " ", 99: ",", 100: ".", 101: "’", 102: "!",103: "-",1:54
}


def decrypt(massge):
    list2= []
    note = ""
    for i in massge:
        if i==",":
            number= int(note)
            list2.append(number)
            note = ""
        else:
            note+=i
    decrypted_massage_list =[]
    for i in list2:
        decrypted_massage_list.append(decrypt_dictionary[i])
        print(decrypt_dictionary[i],end="")

    # print()
    # print(decrypted_massage_list)



massge = input("enter the mass you want to decrypt:\n")
decrypt(massge)