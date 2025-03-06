
# -> Create a list of 10 numbers, find the sum, average, maximum, and minimum values.

list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
max = 1
min = 1

for num in list:
    sum += num
    if (num < min):
        min = num
    if(num > max):
        max = num

average = sum / len(list)

print(f"Sum of :{sum}")

print(f"Average of :{average}")

print(f"Maximum num : {max}")

print(f"Minimum num : {min}")




