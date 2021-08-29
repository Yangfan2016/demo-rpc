# -*- coding: utf-8 -*-
import hello_pb2 as messages
import hello_pb2_grpc as services
from concurrent import futures
import grpc


class HelloYeah(services.HelloYeahServicer):
    def sayHello(self, req, context):
        print('我收到了client的请求')
        return messages.HelloRes(content='hello, {}'.format(req.name))


def serve():
    # 设置线程池 实例化 server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册逻辑到 server
    services.add_HelloYeahServicer_to_server(HelloYeah(), server)
    # 启动 server
    server.add_insecure_port("0.0.0.0:5000")
    server.start()
    print("py-server: running... 0.0.0.0:5000")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
