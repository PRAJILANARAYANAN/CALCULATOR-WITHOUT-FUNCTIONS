replace1=""
flag="print"
print("*********  Welcome to the Zodiac calculator")
print("Enter the number1 :")
num1=int(input())
print("Enter the number2 :")
num2=int(input())
print(num2)
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")
result=0
operator=input("Please choose an optional from these (1,2,3,4,5):")
print(operator)
if operator=="1":
    result=num1+num2
    print("The result of addition of ",num1,"and",num2,"is",result)
if operator=="2":
    if num1<num2:
         print("Cannot subtract the First number is less then the Second number")
    else:
     result==num1-num2
     print("The result of substraction of",num1,"and",num2,"is",result)
if operator=="3":
    if num2==0 or num1==0:
        print("cannot multiplication by zero")
    else:
        result=num1*num2
        print("The result of  multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("cannot divide by zero")
    else:
        result= num1//num2
        print("The result of division of",num1,"and",num2,"is",result)
if operator=="5":
    if num2==0:
        print("modulus cannot be done")
    else:
         result=num1%num2
         print("The result of modulas of",num1,"and",num2,"is",result)

