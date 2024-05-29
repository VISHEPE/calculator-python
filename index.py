
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
   if y== 0:
       print("not divisible")
   else:
       x/y
       
num1  = int(input("enter your first number"))
operator = input("enter your operator: +,-,*,/")
num2  = int(input("enter your second number"))

if operator == '+':
    print("answer is:",add(num1,num2))
elif operator == '-':
    print("Your answer is:",subtarct(num1,num2))
elif operator == '/':
    print("your answer is:",divide(num1,num2))
elif operator == '*':
    print("your answer is:",multiply(num1,num2))
else:
    print("invalide choice")
    