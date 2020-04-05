import socket
from core.utils  import display_msg
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

CHUNK_SIZE = 1024

class Client:
    def __init__(self, server_ip, server_port=8080):
        self.DELIMETER = "<END_OF_BYTES>"
        self.CHUNK_SIZE = 64 * 1024
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
            self.server_addr = (server_ip, server_port)
        except Exception as err:
            print(err)

    def connect_with_server(self):
        try:
            # display_msg("Trying to connect with server: " + self.server_addr[0])
            self.sock.connect(self.server_addr)

            display_msg("Connection established with " + self.server_addr[0])
        except ConnectionRefusedError as err:
            display_msg(str(err), "r")

    def send_data(self, data=""):
        data_to_send = data + self.DELIMETER
        data_bin = data_to_send.encode()
        self.sock.sendall(data_bin)
        

    def receive_data(self):
        data = b''
        while True:
            chunk = self.sock.recv(self.CHUNK_SIZE)

            if self.DELIMETER.encode() in chunk:
                chunk = chunk[:-len(self.DELIMETER)]
                data += chunk
                break
            data += chunk
        return data.decode()

    
    def send(self, msg=""):
        """send a simple 1024 bytes message
        
        Keyword Arguments:
            msg {str} -- Message you want to send (default: {""})
        """        
        msg_bin = msg.encode()
        self.sock.send(msg_bin)

    def recv(self):
        """Receive simple message in 1024 bytes
        
        Returns:
            msg -->> [type str] Message you want to receive 
        """        
        msg_bin = self.sock.recv(self.CHUNK_SIZE)
        msg = msg_bin.decode()
        return msg

    def close(self):
        self.sock.close()
    
