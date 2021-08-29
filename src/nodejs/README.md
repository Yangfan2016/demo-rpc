## install

编译 proto 文件

```shell

# 全局安装 protoc-gen-grpc 用于生产 proto 脚本
npm install protoc-gen-grpc -g

# 安装完成后，在protos目录下执行
protoc-gen-grpc --js_out=import_style=commonjs:. --grpc_out=. -I=. hello.proto

```

安装依赖

```shell
# 首先安装一下依赖，google-protobuf这个依赖是在hello_pb.js中require的，需要安装
$ npm install grpc google-protobuf --save

```



### ref

https://zhuanlan.zhihu.com/p/397811599