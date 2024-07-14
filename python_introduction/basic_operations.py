# number1 = 10
# number2 = 5
# sum = number1 + number2
# difference = number1 - number2
# product = number1 * number2
# print ( "Addition of", number1, "and", number2, "is", sum)
# print ("Subtraction of", number1, "and", number2, "is", difference)
# print ("Multiplication of", number1, "and", number2, "is", product)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    difference = num1 / num2
    print(f"The difference is {difference}")
except ZeroDivisionError:
    print("You can't divide by 0")
    pass #
else:
    print("You are killing it") #to print if the instructions in try are true
finally:
    print("Whatever happened up. You are amazing at your job")