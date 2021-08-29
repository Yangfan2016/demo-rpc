# -*- coding: utf-8 -*-
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_pb2 as hello__pb2


class HelloYeahStub(object):
    """服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sayHello = channel.unary_unary(
                '/hello.HelloYeah/sayHello',
                request_serializer=hello__pb2.HelloReq.SerializeToString,
                response_deserializer=hello__pb2.HelloRes.FromString,
                )


class HelloYeahServicer(object):
    """服务
    """

    def sayHello(self, request, context):
        """方法
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloYeahServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.sayHello,
                    request_deserializer=hello__pb2.HelloReq.FromString,
                    response_serializer=hello__pb2.HelloRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.HelloYeah', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloYeah(object):
    """服务
    """

    @staticmethod
    def sayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.HelloYeah/sayHello',
            hello__pb2.HelloReq.SerializeToString,
            hello__pb2.HelloRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)