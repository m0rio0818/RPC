import socket
import sys
import json

class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_address = "./rpc_server_address"
        
    def start(self):
        print("Connecting to {}".format(self.server_address))
        try:
            self.sock.connect(self.server_address)
            print("Connected!")
        except socket.error as e:
            print("errorrr!!!!!!!!! => ",e)
            sys.exit(1)
        self.sendAndRecive()
            
    def sendAndRecive(self):
        message = {
            "method": "subtract", 
            "params": [42, 23], 
            "param_types": ["int", "int"],
            "id": 1
        }
        
        message_json = json.dumps(message)
        b_message = bytes(message_json, "utf-8")
        print(b_message)

        self.sock.sendall(b_message)
        self.sock.settimeout(2)
        
        try:
            while True:
                data = str(self.sock.recv(32))
                if data:
                    print("Server response :", data)
                else:
                    break
        except TimeoutError:
            print("Socket timeout, ending listening gor server messages")
        self.sock.close()
          
          
    def close(self):
        print("Closing socket")
        self.sock.close()
        
        
def main():
    client = Client()
    client.start()
    
if __name__ == "__main__":
    main()