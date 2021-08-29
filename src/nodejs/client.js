const grpc = require("grpc");
const messages = require("../hello_pb");
const services = require("../hello_grpc_pb");

function main() {
    // 认证方式要和服务端一致，否则就会导致认证失败
    const client = new services.HelloYeahClient("127.0.0.1:5000", grpc.credentials.createInsecure());
    const req = new messages.HelloReq();
    req.setName("zhang");
    req.setAge(10);
    // call
    client.sayHello(req, (err, res) => {
        if (err) {
            console.log('err', err.message);
        } else {
            console.log('我收到了server的消息', res.getContent());
        }
    });
}


main();