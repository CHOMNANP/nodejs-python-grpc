# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Hello_pb2 as Hello__pb2


class HelloStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.call = channel.unary_unary(
        '/demo.Hello/call',
        request_serializer=Hello__pb2.Request.SerializeToString,
        response_deserializer=Hello__pb2.Response.FromString,
        )


class HelloServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'call': grpc.unary_unary_rpc_method_handler(
          servicer.call,
          request_deserializer=Hello__pb2.Request.FromString,
          response_serializer=Hello__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'demo.Hello', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))