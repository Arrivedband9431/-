'''
Author: yali sommer
Program name: server
Task Given: create a server and a client that can communicate with the server
            and get a response from the server
Description:
    this is the server side of the code
    commands are  TIME , NAME , RAND , EXIT
Date: 2025-10-09
'''
import socket
import random
import logging
from datetime import date, time, datetime


logging.basicConfig(
    filename='my_application.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
'''
logging.info('Application started successfully.')
logging.debug('This debug message will not appear in the log file')
logging.warning('A potential issue was detected.')
logging.error('An error occurred during processing.')
'''

MAX_PACKET = 1024
QUEUE_LEN = 1
MY_SERVER_NAME = "yali's server"

def main():
    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            my_socket.bind(('0.0.0.0', 1730))
            my_socket.listen(QUEUE_LEN)
            client_socket, client_address = my_socket.accept()
            try:
                request = client_socket.recv(MAX_PACKET).decode()
                request = request.upper()
                match request:
                    case "TIME":
                        time_and_date = str(datetime.now())
                        client_socket.send(time_and_date.encode())
                        logging.info(f'TIME sent successfully')
                    case "NAME":
                        client_socket.send(MY_SERVER_NAME.encode())
                        logging.info(f'NAME sent successfully')
                    case "RAND":
                        random_number = str(random.randint(1, 10))
                        client_socket.send(random_number.encode())
                        logging.info(f'RAND sent successfully')
                    case "EXIT":
                        client_socket.close()
                        logging.info(f'exited program successfully')
                        logging.warning(f'closed server from client command')
                        break
                    case _:
                        client_socket.send("NOT A COMMAND WRONG INPUT!! ".encode())
                        logging.warning(f'INPUT ERROR WRONG INPUT ENTERED')
                # print('server received ' + request)
                client_socket.send(request.encode())
            except socket.error as err:
                print('received socket error on client socket' + str(err))
            finally:
                client_socket.close()
                logging.info('closing client socket')
        except socket.error as err:
            print('received socket error on server socket' + str(err))
            logging.error(f'ERROR - {err}')
        finally:
            my_socket.close()

if __name__ == '__main__':
    main()