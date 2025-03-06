
#  -> Implement a recursive function to find the greatest common divisor (GCD) of two numbers.

num1 = int(input("Enter number 1 : "))

num2 = int(input("Enter number 2 : "))

def gcd(num1,num2):
    if (num2 == 0):
        return num1
    else:
        return gcd(num1, num1 % num2)
    
print(f"GCD is {gcd(num1,num2)}")