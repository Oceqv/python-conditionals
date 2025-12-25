# Used int() to convert string to int otherwise you could only type words no numbers

temp = int(input("What Temperature is outside right now? "))
if temp >= 25:
    print("ITS VERY WARM!")
else:
    print("ITS VERY COLD!")
