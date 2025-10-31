"""
Author: yali sommer
Program name: client
Task Given: create a server and a client that can communicate with the server
            and get a response from the server
Description:
    this is the client side of the code
    commands are  TIME , NAME , RAND , EXIT
Date: 2025-10-09

more info -
ms - stands for "my socket"

longest line allowed is-
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""


import socket

max_packet = 1024
while True:
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ms.connect(('127.0.0.1', 1730))
        users_input = input("Commands are allowed ,TIME,NAME,RAND,EXIT,: \n")
        users_input = users_input[:4]

        ms.send(users_input.encode())
        response = ms.recv(max_packet).decode()
        print(response)
        if users_input == "EXIT" or users_input == "exit":
            break
    except socket.error as err:
        print('received socket error ' + str(err))
    finally:
        ms.close()
