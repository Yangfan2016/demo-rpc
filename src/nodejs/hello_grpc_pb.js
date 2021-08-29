// GENERATED CODE -- DO NOT EDIT!

// Original file comments:
// 协议 proto 版本 3
'use strict';
var grpc = require('grpc');
var hello_pb = require('./hello_pb.js');

function serialize_hello_HelloReq(arg) {
  if (!(arg instanceof hello_pb.HelloReq)) {
    throw new Error('Expected argument of type hello.HelloReq');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hello_HelloReq(buffer_arg) {
  return hello_pb.HelloReq.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hello_HelloRes(arg) {
  if (!(arg instanceof hello_pb.HelloRes)) {
    throw new Error('Expected argument of type hello.HelloRes');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hello_HelloRes(buffer_arg) {
  return hello_pb.HelloRes.deserializeBinary(new Uint8Array(buffer_arg));
}


// 服务
var HelloYeahService = exports.HelloYeahService = {
  // 方法
sayHello: {
    path: '/hello.HelloYeah/sayHello',
    requestStream: false,
    responseStream: false,
    requestType: hello_pb.HelloReq,
    responseType: hello_pb.HelloRes,
    requestSerialize: serialize_hello_HelloReq,
    requestDeserialize: deserialize_hello_HelloReq,
    responseSerialize: serialize_hello_HelloRes,
    responseDeserialize: deserialize_hello_HelloRes,
  },
};

exports.HelloYeahClient = grpc.makeGenericClientConstructor(HelloYeahService);
