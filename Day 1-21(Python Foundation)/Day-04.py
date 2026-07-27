# marks = 130
# if marks >= 80 and marks <= 100:
#     print("A+")
# elif marks >= 70 and marks < 80:
#     print("A")
# elif marks >= 60 and marks < 70:
#     print("A-")
# elif marks >= 50 and marks < 60:
#     print("B")
# elif marks >= 40 and marks < 50:
#     print("C")
# elif marks > 100:
#     print("Invalid")
# else:
#     print("Fail")


# marks = int(input("Enter your marks (0-100): "))

# if marks < 0 or marks > 100:
#     print("Invalid marks! Please enter between 0-100")
# elif marks >= 80 and marks <= 100:
#     grade = "A+"
# elif marks >= 70 and marks < 80:
#     grade = "A"
# elif marks >= 60 and marks < 70:
#     grade = "A-"
# elif marks >= 50 and marks < 60:
#     grade = "B"
# elif marks >= 40 and marks < 50:
#     grade = "C"
# else:
#     grade = "F" 

# print(f"Your marks= {marks}")
# print(f"Your grade has= {grade}")


# Challenge 1:
# BMI calculator বানাও। User height (meter) আর weight (kg) দেবে। BMI = weight / height² এই formula তে calculate করো। তারপর range দেখে print করো:

# BMI < 18.5 → Underweight
# 18.5 to 24.9 → Normal
# 25 to 29.9 → Overweight
# 30+ → Obese

# height = float(input("Enter your height: "))
# weight = float(input("Enter your weight: "))

# bmiCalculation = weight / (height*height)

# if bmiCalculation < 18.5:
#     bmi = "Underweight"
# elif bmiCalculation <= 24.9:
#     bmi = "Normal"
# elif bmiCalculation <= 29.9:
#     bmi = "Overweight"
# else:
#     bmi = "Obese"

# print(f"You are {bmi}")


# একটা simple login system। username আর password নাও। যদি দুটোই সঠিক হয় তাহলে "Login successful", শুধু password ভুল হলে "Wrong password", শুধু username ভুল হলে "User not found"।

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if password != "CS2203009":
#     print("Wrong password")
# elif username != "mahmud":
#     print("User not found")   
# else:
#     print("Login successful")

# Challenge 3 (একটু harder):
# Marks নাও। তারপর check করো:

# 3 subject এর marks আলাদাভাবে নাও
# যদি কোনো একটায় 33 এর নিচে হয় → "Failed in one subject"
# তিনটার average দিয়ে grade দাও
# কিন্তু যদি fail থাকে তাহলে final grade সবসময় F


# english = int(input("Enter your English mark: "))
# math = int(input("Enter your Math mark: "))
# dsa = int(input("Enter your DSA mark: "))

# if english < 33 or math < 33 or dsa < 33:
#     print("You failed in one subject")
#     grade = "F"
# else:
#     avg = (english + math + dsa) / 3
#     if avg >= 80:
#         grade = "A+"
#     elif avg >= 70:
#         grade = "A"
#     elif avg >= 60:
#         grade = "A-"
#     elif avg >= 50:
#         grade = "B"
#     elif avg >= 40:
#         grade = "C"
#     else:
#         grade = "F"
    
# print(f"Your grade has= {grade}")



# Challenge 4:
# একটা number নাও। check করো সেটা positive, negative নাকি zero। তারপর positive হলে odd নাকি even সেটাও বলো।
# input: 7  → "Positive, Odd"
# input: -3 → "Negative"
# input: 0  → "Zero"

# number = int(input("Enter a number: "))
# if number > 0:
#     if number % 2 == 0:
#         print("Positive, Even")
#     else:
#         print("Positive, ODD")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")


# Challenge 5:
# তিনটা number নাও। সবচেয়ে বড়টা print করো। if/elif/else দিয়ে করো, max() function use করবে না।

# num1 = int(input("Enter number-1: "))
# num2 = int(input("Enter number-2: "))
# num3 = int(input("Enter number-3: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is greater")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is greater")
# elif num3 > num1 and num3 > num2:
#     print(f"{num3} is greater")
# else:
#     print("The numbers are equal")



# Challenge 6:
# একটা year নাও। সেটা leap year কিনা check করো।
# Leap year rules:

# 4 দিয়ে divisible হতে হবে
# কিন্তু 100 দিয়ে divisible হলে leap year না
# কিন্তু 400 দিয়ে divisible হলে আবার leap year


year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")