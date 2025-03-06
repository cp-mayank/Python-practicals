
# -> Write a program that takes an integer input from the user and checks if it is positive, negative, or zero.


num = int(input("Enter number :"))

if (num == 0):
    print("Number is ZERO")
elif (num > 0):
    print(f"{num} is POSITIVE")
else:
    print(f"{num} is NEGATIVE")