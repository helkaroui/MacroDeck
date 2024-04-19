
generate_proto:
	python3 -m grpc_tools.protoc -I protos --python_out=py-engine/server --pyi_out=py-engine/server --grpc_python_out=py-engine/server protos/exec_actions.proto
