# What is gRPC?
gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

# Explanation
In this project, the client communicates and passes requests to the server using gRPC. The structure of the data to be passed is defined in the .proto file.
Protocol buffers are used since they are very more efficient than JSON, since the data is in binary format and efficiently serialized.
The rpc functions in the proto file takes requests from the client in the specified format and returns responses. 

A major advantages of gRPC are that it supports HTTP/2 and it's capability of streaming requests and responses. gRPC suports unary, client-side streaming, server-side streaming and bi-directional streaming. Here, I have only used the concept of Unary (Single request and single response).

In the code, it looks like the client is calling the function in the server side, this is through the RPC call. The client sends the request the the server in serialized 
format and once the server runs the request, it also sends the response serialized.
