import socket
import os
import math

class RPC:
    def __init__(self, method, params, param_types, id) -> None:
        self.method = method
        self.params = params
        self.param_tyes= param_types
        self.id = id
        
        
    def floor(self, x):
        return math.floor(x)
    
    def nroot(self, n, x):
        return math.pow(x, 1/n)
    
    def reverse(self, s):
        return "".join(list(reversed(s)))

    def validAnagram(self, str1, str2):
        return lambda params: set(str1) == set(str2)
    
    def sort(self, strArr) -> None:
        return strArr.sort()
        
class Server:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_addressess = "./rpc_server_address"
        
    def start(self):
        try:
            os.unlink(self.sock)
        except FileNotFoundError:
            pass
        
    def accept(self):
        self.sock.bind(self.server_addressess)
        self.sock.listen(10)
        
    def sendAndRecive(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print("Connection from ", client_address)
                
                while True:
                    data = connection.recv(32)
                    data_str = data.decode("utf-8")
                    print("Recived :", data_str)
                    
                    if data:
                        response = "Processing " + data_str
                        connection.sendall(response.encode())
                        
                    else:
                        print("no data from ", client_address)
                        break
            finally:
                self.close()

    def close(self):
        print("Closing current socket")
        self.sock.close()
        
def main():
    server = Server()
    server.start()
        
if __name__ == "__main__":
    main()