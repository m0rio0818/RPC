const net = require("net")
class Client {
    constructor(address) { 
        this.socket = net.createConnection(address)    

        this.socket.setTimeout(3000)

        this.socket.on("connect", () => {
            console.log("接続しました。")
        })

        this.socket.on("data", (data) => {
            console.log(`サーバーから受信したデータ: ${data}`);
            this.socket.end();
        })

        this.socket.on("end" , () => {
            console.log("サーバーとの処理が切断されました")
        })
    }

    write(data){
        this.socket.write(data)
    }
    
    destroy(){
        this.socket.destroy();
    }
}

data = {
    "method": "subtract", 
    "params": [42, 23], 
    "param_types": ["int", "int"],
    "id": 1
}

serverAddress= "./rpc_server_address"
let client = new Client(serverAddress);
client.write(JSON.stringify(data))