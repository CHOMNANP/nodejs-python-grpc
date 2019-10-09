from concurrent import futures
import logging

import grpc

import Hello_pb2
import Hello_pb2_grpc


class HelloController(Hello_pb2_grpc.HelloServicer):

    def call(self, request, context):
        print("hello, there is an input")
        return Hello_pb2.Response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Hello_pb2_grpc.add_HelloServicer_to_server(HelloController(), server)
    server.add_insecure_port('0.0.0.0:5051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print("hello")
    serve()