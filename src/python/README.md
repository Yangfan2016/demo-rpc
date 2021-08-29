## install



```shell

# 安装 pip （python 包管理工具，注意版本）
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python get-pip.py

# pip 升级
pip install -U pip

```


```shell

# 1. 安装Python的gRPC源码包grpcio，用于执行gRPC的各种底层协议和请求响应方法 

sudo python -m pip install grpcio
# 2. 安装Python基于gRPC的proto生成python源代码的工具grpcio-tools
python -m pip install grpcio-tools


# 3. 编译 proto 文件
python -m grpc_tools.protoc --python_out=.  --grpc_python_out=.  -I. hello.proto

# python -m grpc_tools.protoc: python 下的 protoc 编译器通过 python 模块(module) 实现, 所以说这一步非常省心
# --python_out=. : 编译生成处理 protobuf 相关的代码的路径, 这里生成到当前目录
# --grpc_python_out=. : 编译生成处理 grpc 相关的代码的路径, 这里生

```


### ref

https://www.bilibili.com/video/BV1NL4y1v7YA?p=3