"""
Author: yali sommer
Program name: server
Task Given: create a server and a client that can communicate with the server
            and get a response from the server
Description:
    this is the server side of the code
    commands are  TIME , NAME , RAND , EXIT
Date: 2025-10-09

important info:
ms - my socket
cs - client socket



longest line can be
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""
import socket
import random
import logging
from datetime import datetime


logging.basicConfig(
    filename='my_application.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

max_packet = 1024
queue_len = 1
MY_SERVER_NAME = "yali's server"


def main():
    while True:
        ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ms.bind(('0.0.0.0', 1730))
            ms.listen(queue_len)
            cs, client_address = ms.accept()
            try:
                request = cs.recv(max_packet).decode()
                request = request.upper()
                match request:
                    case "TIME":
                        time_and_date = str(datetime.now())
                        cs.send(time_and_date.encode())
                        logging.info(f'TIME sent successfully')
                    case "NAME":
                        cs.send(MY_SERVER_NAME.encode())
                        logging.info(f'NAME sent successfully')
                    case "RAND":
                        random_number = str(random.randint(1, 10))
                        cs.send(random_number.encode())
                        logging.info(f'RAND sent successfully')
                    case "EXIT":
                        cs.close()
                        logging.info(f'exited program successfully')
                        logging.warning(f'closed server from client command')
                        break
                    case _:
                        cs_length = len(str(request))
                        if cs_length < 4:
                            amount_of_zeros_needed = "0" * (4 - cs_length)
                            request += amount_of_zeros_needed
                        cs.send(f"{request} is NOT A COMMAND WRONG INPUT!! ".encode())
                        logging.warning(f'INPUT ERROR WRONG INPUT ENTERED')
                cs.send(request.encode())
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                cs.close()
                logging.info('closing client socket')
        except socket.error as err:
            print('received socket error on server socket' + str(err))
            logging.error(f'ERROR - {err}')
        finally:
            ms.close()


if __name__ == '__main__':
    main()
