number1 = int(input("First integer: "))
number2 = int(input("Second integer: "))
number3 = int(input("Third integer: "))
maximum = number1

if number2 > maximum:
  maximum= number2
if number3 > maximum:
  maximum= number3
print('Maximum value is', maximum)
