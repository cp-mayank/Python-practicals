
# -> Create a function that checks whether a given string is a palindrome or not.


n = int(input("Enter random number : "))

def rev(n,temp):

    if(n == 0):
        return temp
    
    temp = (temp * 10) + (n % 10)

    return rev(n // 10, temp)

if(n == rev(n,0)):
    print(f"{n} is palindrome number")
else:
    print(f"{n} is not palindrome number")