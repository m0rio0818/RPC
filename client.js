const net = require("net")
class Client {
    constructor(address) {
        this.data = {
            "method": "subtract", 
            "params": [42, 23], 
            "param_types": ["int", "int"],
            "id": 1
        }
    
        this.socket = net.createConnection(address, () => {
            console.log("connecting to the server");
        })      

        // console.log(JSON.stringify(this.data), typeof(JSON.stringify(this.data)))


        this.socket.setTimeout(3000)

        this.socket.on("connect", () => {
            console.log("これから接続します。")
            this.socket.write(JSON.stringify(this.data));
        })

        this.socket.on("data", (data) => {
            console.log(`サーバーから受信したデータ: ${data}`);
            this.socket.end();
        })

        this.socket.on("end" , () => {
            console.log("サーバーとの処理が切断されました")
        })
    }
}


serverAddress= "./rpc_server_address"
let client = new Client(serverAddress);