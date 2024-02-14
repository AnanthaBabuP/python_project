a = int(input("Enter A Value : "))
b = int(input("Enter B Value : "))
process = input("Enter the Process For add/sub/mul/div/all :")
if (process == "add"):	
    print("Addtion value Of a,b are :",a+b)
elif(process== "sub"):	
    print("Subration Value Of a,b are :",a-b)
elif(process== "mul"):	
    print("Multiplication Value Of a,b are :",a*b)
elif(process== "div"):	
    print("Division Value Of a,b are :",a/b)
elif(process== "all"):		
    print("Addtion value Of a,b are :",a+b)	
    print("Subration Value Of a,b are :",a-b)
    print("Multiplication Value Of a,b are :",a*b)
    print("Division Value Of a,b are :",a/b)
else:	
	print("Invalid Process")
