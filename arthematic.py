#arthametic operations
a=10
b=3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("floor Division:",a//b)
print("Remainder:", a % b)
print("power:", a**b)

#simple calculatior
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks calculator
name=input("Enter student name: ")
m1=int(input("Enter python marks: "))
m2=int(input("Enter Java marks: "))
m3=int(input("Enter SQL marks : "))
total=m1+m2+m3
average=total/3
print("\n-----student name-----")
print("Name:", name)
print("Total :", total)

#shopping bill calculator
price1=float(input("Enter product 1 price"))
price2=float(input("Enter product 2 price"))
price3=float(input("Enter product 3 price"))
total=price1+price2+price3
discount=total*0.1
final_amount=total-discount
print("Discount:", discount)
print("Final Amount:",final_amount)
print("Total bill:",total)

#assignment operators
x = 10
x+=5
print(x)

x-=2
print(x)

x*3
print(x)

#bank balance

balance=10000

deposite=5000
balance+=deposite
print(" after deposite:", balance)

withdraw = 2000
balance-=withdraw
print(" after withdrawal:", balance)

#comparis0n operators

a=10
b=20

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#age eligibility checker
age=int(input("Enter your age: "))
print("Eligible:", age>=18)

#pas or fail checker
marks = int(input("Enter marks: "))
print("passed:", marks>=40)
#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)



