num1=float(input("Enter first number: "))
operator=input("Enter operator: ")
num2=float(input("Enter second number: "))
if operator=="+":
  result1=float(num1) + float(num2)
  print(result1)
elif operator=="-":
  result2=float(num1) - float(num2)
  print(result2)
elif operator=="*":
  result3=float(num1) * float(num2)
  print(result3)
elif operator=="/":
  result4=float(num1) / float(num2)
  print(result4)
else: 
  print("Enter a True operator")
#comment