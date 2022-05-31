num1=float(input("enter first number"))
num2=float(input("enter second number"))
num3=float(input("enter third  number"))
if num1>num2:
    if num1<num3:
        med=num1
        print(med)
    elif num2>num3:
        med=num2
        print(med)
    else:
        med=num3
else:
    if num1>num3:
        med=num1
    elif num2<num3:
        med=num2
    else:
        med=num3 
print("the median is=",med)                           
    

