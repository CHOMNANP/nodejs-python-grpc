#
pip install grpcio-tools

#
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_ou
t=. protos/Hello.proto