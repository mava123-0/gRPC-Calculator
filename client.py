import grpc
import calc_pb2 as pb2
import calc_pb2_grpc as pb2_grpc

class calcClient(object):
    def __init__(self):
        self.channel=grpc.insecure_channel('localhost:50051')
        self.stub=pb2_grpc.CalculatorStub(self.channel)
    def sum_num(self,value1,value2):
        #serialize the value
        ser_val=pb2.NumberTwo(number1=value1,number2=value2)
        return self.stub.getSum(ser_val)
    def prod_num(self,value1,value2):
        #serialize the value
        ser_val=pb2.NumberTwo(number1=value1,number2=value2)
        return self.stub.getProduct(ser_val)
    def diff_num(self,value1,value2):
        #serialize the value
        ser_val=pb2.NumberTwo(number1=value1,number2=value2)
        return self.stub.getDiff(ser_val)
    def div_num(self,value1,value2):
        #serialize the value
        ser_val=pb2.NumberTwo(number1=value1,number2=value2)
        return self.stub.getDiv(ser_val)
    def sq_root(self,value):
        #serialize the value
        ser_val=pb2.Number(number=value)
        return self.stub.getSqrt(ser_val)
    
if __name__=='__main__':
    client1=calcClient()
    menu=0
    while(menu!=6):
        print("Menu\n1.Sum\n2.Product\n3.Difference\n4.Division\n5.Square Root\n6.Exit")
        menu=int(input("Value: "))
        if(menu==1):
            x=float(input("Enter number1: "))
            y=float(input("Enter number2: "))
            result=client1.sum_num(x,y)
            print(result)
        elif(menu==2):
            x=float(input("Enter number1: "))
            y=float(input("Enter number2: "))
            result=client1.prod_num(x,y)
            print(result)
        elif(menu==3):
            x=float(input("Enter number1: "))
            y=float(input("Enter number2: "))
            result=client1.diff_num(x,y)
            print(result)
        elif(menu==4):
            x=float(input("Enter number1: "))
            y=float(input("Enter number2: "))
            result=client1.div_num(x,y)
            print(result)
        elif(menu==5):
            x=float(input("Enter the number of which sqrt needed: "))
            result=client1.sq_root(x)
            print(result)
        elif(menu==6):
            print("\nExiting!!")
            break