const grpc = require("grpc");
const messages = require("./hello_pb");
const services = require("./hello_grpc_pb");

function main() {
    const server = new grpc.Server();
    server.addService(services.HelloYeahService, { sayHello });
    // 监听所有地址，绑定5000端口
    // grpc.ServerCredentials.createInsecure() 表示没有做任何认证机制
    // 这里，你可以设置SSL，Google认证机制，都是可以的，具体可以看一下文档
    server.bind('0.0.0.0:5000', grpc.ServerCredentials.createInsecure());
    server.start();
    console.log('node-server: runing... 0.0.0.0:5000');
}

function sayHello(call, callback) {
    const res = new messages.HelloRes();
    res.setContent(`hello ${call.request.getName()}`);
    callback(null, res);
}


main();
