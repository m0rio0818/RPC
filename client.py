import socket
import sys
import json

class CLient:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./rpc_server_address"
        
    def start(self):
        print("Connecting to {}".format(self.server_address))
        try:
            self.sock.connect(self.server_address)
        except socket.error as e:
            print(e)
            sys.exit(1)