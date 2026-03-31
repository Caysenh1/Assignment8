rates = [(12,"Child"), (19, "Teen"), (59,"Adult")]
num1 = int(input("Enter an age: "))
if num1 > 59:
    print("Senior")
elif num1 > 20:
    print("Adult")
elif num1 > 12:
    print("Teen")
elif num1 <= 12 and num1 >= 0:
    print("Child")
else:
    print("No rate available")

