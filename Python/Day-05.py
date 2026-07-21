# For Loop

# fruits = ["Mango", "Apple", "Pineapple"]
# for fruit in fruits:
#     print(fruit)

# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# for i in range(1, 10, 2):
#     print(i)

# while Loop

# count = 0
# while count < 10:
#     print(count)
#     count += 1

# fruits = ["Mango", "Banana", "Apple"]
# for fruit in fruits:
#     print(fruit)
# it = iter(fruits)
# print(next(it))

# for char in "AI":
#     print(char)

# list = [1,2,3,4,5,8,6,7]
# for i in list:
#     if i == 5:
#         continue
#     elif i == 7:
#         break
#     print(i)

# 1 theke 50 er modhye shudhu odd number print koro (loop diye)
# print("The ODD numbers are: ")
# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)
# else:
#     continue


# Ekta list dewa ache numbers = [3, 7, 2, 9, 1, 5] — loop diye shobcheye boro number khujে ber koro (max() use kora jabena)
# numbers = [3, 7, 20, 9, 1, 5]
# count = 0
# swap = 0
# while count < len(numbers):
#     if numbers[count] > swap:
#         swap = numbers[count]
#     count += 1
# print(swap)


# Ekta word input nao user theke, loop diye count koro oi word e kotta vowel (a, e, i, o, u) ache

# userInput =  input("Enter a word: ").lower()
# word = list(userInput)
# count = 0
# for i in word:
#     if i == "a" or i == "i" or i == "u" or i == "e" or i == "o":
#         count += 1
#     else:
#         continue
# print(count)


# userInput = input("Enter a word: ").lower()
# count = 0
# for i in userInput:
#     if i in "aeiou":
#         count += 1
# print(count)

userInput = int(input("Enter your number that your multiplication table create: "))
for i in range(1, 11):
    print(f"{userInput} x {i} = {userInput*i}")

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# FizzBuzz

# 1 থেকে 50 print করো, কিন্তু:

# 3 এর গুণিতক হলে number এর বদলে "Fizz"
# 5 এর গুণিতক হলে "Buzz"
# দুইটাই হলে "FizzBuzz"

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"{i} - FizzBuzz")
#     elif i % 3 == 0:
#         print(f"{i} - Buzz")
#     elif i % 5 == 0:
#         print(f"{i} - Fizz")
#     else:
#         print(i)


# Factorial

# User থেকে একটা number নাও, সেটার factorial বের করো loop দিয়ে।
# Input:  5
# Output: 120  (5 x 4 x 3 x 2 x 1)


# user = int(input("Enter a number: "))
# i = 1
# fact = 1
# while i <= user:
#     fact *= i
#     i += 1
# print(f"The factorial has = {fact}")


# Number Guessing Game

# Computer একটা fixed number মাথায় রাখবে (যেমন 42), user guess করতে থাকবে যতক্ষণ না সঠিক হয়।
# Too low!
# Too high!
# Correct! You guessed in 4 tries.


# num = 42
# tries = 1
# while True:
#     user = int(input("Enter a number: "))
#     if user > num:
#         print("Too high!")
#     elif user < num:
#         print("Too Low")
#     else:
#         print(f"Correct! You guessed in {tries} tries.")
#         break
#     tries += 1


# Count Digits

# User থেকে একটা number নাও, loop দিয়ে গণো সেই number এ কয়টা digit আছে।
# Input:  94821
# Output: 5

# user = int(input("Enter a number: "))
# count = 0
# while user > 0:
#      user //= 10
#      count +=1
# print(count)
