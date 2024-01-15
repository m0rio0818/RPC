import socket
import sys


class Client:
    def __init__(self) -> None:
        self.address ="./rpc_server_address"
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        
    def start(self):
        self.connect()
        self.sendMessage()
            
    def connect(self):
        try:
            self.sock.connect(self.address)
        except socket.error as err:
            print(err)
            sys.exit(1)
            
    def sendMessage(self):
        try:
            message = b"Message from client"
            self.sock.sendall(message)
            self.sock.settimeout(2)
            
            try:
                while True:
                    data = str(self.sock.recv(32))
                    if data:
                        print("Server response :", data)
                    else:
                        break
            except TimeoutError:
                print('Socket timeout, ending listening for server messages')
        finally:
            print("Closing socket")
            self.sock.close()
            
                   
                   
                   
def main():
    client = Client();
    client.start()
    
if __name__ == "__main__":
    main()