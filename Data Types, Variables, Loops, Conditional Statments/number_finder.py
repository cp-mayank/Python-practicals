# ->  Write a program to print all prime numbers between 1 and 100 using a loop and conditional statements.

for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("Prime number: ", num)