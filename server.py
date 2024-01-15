import socket
import os
import json
import RPC

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
                    data = connection.recv(4096)
                    data_str = data.decode("utf-8")
                    # ここで受け取ったデータをjson => str
                    
                    if data:
                        try:
                            strJson = json.loads(data_str)
                            print("type",type(data_str), data_str)
                            print("total: ",strJson, type(strJson))
                            print("method: ",strJson["method"])
                            print("params: ",strJson["params"])
                            print("param_types: ",strJson["param_types"])
                            print("id: ",strJson["id"])
                            response = "Processing : " + data_str
                            rpc = RPC.RPC(strJson["id"], strJson["method"], strJson["params"], strJson["param_types"])
                            print(type(rpc.makeJson()), rpc.makeJson())
                            connection.sendall(bytes(rpc.makeJson(), "utf-8"))
                        except json.JSONDecodeError as e:
                            print("JSON Decode Error :", e)
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