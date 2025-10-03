# geting if you are want to encrypt or decrypt safely
while True:
    try:
        option_chooser  = int(input("do you want to encrypt or decrypt?\nenter 1-for encrypt or 2-for decrypt:\n "))
        if (option_chooser==1 or option_chooser==2):
            break
        else:
            print("\n Enter 1 or 2 please.")
    except ValueError:
        print("\n Invalid input enter a number")


encryption_dictionary1 = {
    "A": 56, "B":57,"C": 58,"D":59,"E": 40,"F": 41, "G": 42,"H": 43,"I": 44,"J": 45,"K": 46,"L": 47,"M": 48,"N": 49,"O":60,"P":61,"Q": 62,"R": 63,"S":64,"T":65,"U": 66,"V":67,"W": 68,"X":69,"Y":10,"Z":11,
    "a":12,"b":13,"c":14,"d":15,"e":16,"f":17,"g":18,"h":19,"i":30,"j":31,"k":32,"l":33,"m":34,"n":35,"o":36,"p":37,"q": 38, "r": 39, "s":90,"t":91,"u":92,"v":93,"w":94,"x":95,"y":96,"z":97,
    " ":98 ,",":99,".":100,"’":101,"!":102,"-":103,":":104
}