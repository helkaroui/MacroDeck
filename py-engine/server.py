from concurrent import futures
import logging

import grpc
import exec_actions_pb2, exec_actions_pb2_grpc


GLOBAL_VAR="my global var"

class RouteGuideServicer(exec_actions_pb2_grpc.ExecActionServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def RunAction(self, request: exec_actions_pb2.ActionList, context):
        for i, action in enumerate(request.actions):
            exec(action.code)
            yield exec_actions_pb2.ActionStatus(id=i, current_step=i, total_steps=request.count)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    exec_actions_pb2_grpc.add_ExecActionServicer_to_server(
        RouteGuideServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Starting server on localhost:50051")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    serve()
