import grpc
import protocol_pb2
import protocol_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = protocol_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(protocol_pb2.HelloRequest(name="Ariful"))
        print("Server Response:", response.message)

if __name__ == "__main__":
    run()
