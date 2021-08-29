# -*- coding: utf-8 -*-
import hello_pb2 as messages
import hello_pb2_grpc as services
import grpc


def serve():
    channel = grpc.insecure_channel("127.0.0.1:5000")
    stub = services.HelloYeahStub(channel)
    res = stub.sayHello(
        messages.HelloReq(name='yf', age=100))
    print(res.content)


if __name__ == "__main__":
    serve()
