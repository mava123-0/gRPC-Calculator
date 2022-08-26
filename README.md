# gRPC-Calculator
Calculator made using gRPC client-server connection.

# What is gRPC?
gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

# Working
In this project, the client communicates and passes requests to the server using gRPC. The structure of the data to be passed is defined in the .proto file.
The rpc functions in the proto file takes requests from the client in the specified format and returns responses. Main adantage of gRPC is the capability of streaming
requests and responses. gRPC suports Unary, Client-side streaming, server-side streaming and bi-directional streaming. Here, I have used the concept of only Unary
(Single request and single response).

The client 
