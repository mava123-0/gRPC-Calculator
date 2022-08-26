import grpc 
import time
from concurrent import futures
import calculator

import calc_pb2_grpc as pb2_grpc
import calc_pb2 as pb2

class CalcServer(pb2_grpc.CalculatorServicer):
    def __init__(self,*args,**kwargs):
        pass

    def getSum(self,request,context):
        print("Sum Called")
        final_result=pb2.Number()
        final_result.number=calculator.sum_num(request.number1,request.number2)
        return final_result

    def getProduct(self,request,context):
        print("Product Called")
        final_result=pb2.Number()
        final_result.number=calculator.prod_num(request.number1,request.number2)
        return final_result

    def getDiv(self,request,context):
        print("Division Called")
        final_result=pb2.Number()
        final_result.number=calculator.div_num(request.number1,request.number2)
        return final_result

    def getDiff(self,request,context):
        print("Difference Called")
        final_result=pb2.Number()
        final_result.number=calculator.diff_num(request.number1,request.number2)
        return final_result

    def getSqrt(self,request,context):
        print("Square Root Called")
        value=pb2.Number()
        value.number=calculator.squareRoot(request.number)
        return value

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CalculatorServicer_to_server(CalcServer(),server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print("Server Started")
    server.wait_for_termination()

if __name__=='__main__':
    serve()