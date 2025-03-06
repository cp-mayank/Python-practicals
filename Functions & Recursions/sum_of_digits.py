
#  -> Write a recursive function to find the sum of digits of a number.

def sum_of_digit(n):
    if(n == 0):
        return 0
    return (n % 10  + sum_of_digit(int(n / 10)))

num = int(input("Enter number :"))

print(f"Sum of digits {num} in {sum_of_digit(num)}")

