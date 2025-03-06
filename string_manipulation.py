
# -> Take a string input from the user and print the number of vowels and consonants in it.


vowels = 'aeiouAEIOU'  

value = input("Enter any word: ")

vowelsCount = 0
consonantsCount = 0

for char in value:
    if char.isalpha():  
        if char in vowels:
            vowelsCount += 1  
        else:
            consonantsCount += 1  

print(f"Vowels count: {vowelsCount} and Consonants count: {consonantsCount}")


