
# -> Write a function that returns the first N Fibonacci numbers using recursion.


def Fibonacci(n):
    if(n < 0):
        print("Invalid number")
    elif(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    

print(Fibonacci(5))
    

