def add(num1,num2):
    return(num1+num2)
def subtract(num1,num2):
    return(num1-num2)
def divide(num1,num2):
    return(num1/num2)
def multiplication(num1,num2):
    return(num1*num2)
print("please select the opreation")
print("a.add")
print("b.subtract")
print("c.divide") 
print("d.multiplication")

choose=(input("enter your choice:"))

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
if choose=="a":
    print("result of addition opreation is:",add(num1,num2))
elif choose=="b":
    print("result of subtract opreation is:",subtract(num1,num2))

elif choose=="c":
    print("result of divide opreation is:",divide(num1,num2))

elif choose=="d":
    print("result of multiplication opreation is:",multiplication(num1,num2))

else:
    print("invalid input")








