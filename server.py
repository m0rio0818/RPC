import socket
import os

class Server:
    def __init__(self) -> None:
        self.address = "./rpc_server_address"
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    
    def start(self):
        try:
            os.unlink(self.address)
        except FileNotFoundError:
            pass
        print("Starting up on {}".format(self.address))
        self.connect()
        self.getMessage()
        
        
    def connect(self):
        self.sock.bind(self.address)
        self.sock.listen(1)
    
    def getMessage(self):
        while True:
            connection, client_address = self.sock.accept()
            try:
                print("Connection from".format(client_address))
                while True:
                    data = connection.recv(32)
                    data_str = data.decode("utf-8")
                    print("Recived : " + data_str)
                    if data:
                        response = "Processing : " + data_str
                        connection.sendall(response.encode())
                    else:
                        print("No data from", client_address)
                        break
            finally:
                print("Closing current connection")
                connection.close()
                
                
def main():
    server = Server()
    server.start()
    
if __name__ == "__main__":
    main()