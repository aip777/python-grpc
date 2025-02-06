import grpc
from concurrent import futures
import protocol_pb2
import protocol_pb2_grpc

class GreeterServicer(protocol_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return protocol_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protocol_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
