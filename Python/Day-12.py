# def div(a,b):
#     try:
#         return a/b
#     except (ZeroDivisionError):
#         return None

# print(div(10,0))

# def division(a:int,b:int):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Not divided by zero"
#     except ValueError:
#         return "Value Not match, enter correct value"
#     # finally:
#     #     return "All code are run"

# a = int(input("Enter a number: "))
# b = int(input("Enter number: "))
# print(division(a,b))

# try:
#     a = int(input("Number-1: "))
#     b = int(input("Number-2: "))
#     print(a / b)

# except ValueError:
#     print("Input a number")

# except ZeroDivisionError:
#     print("Not divided by zero")


# try:
#     a = int(input("প্রথম সংখ্যা: "))
#     b = int(input("দ্বিতীয় সংখ্যা: "))
#     print(a / b)

# except ZeroDivisionError:
#     print("শূন্য দিয়ে ভাগ দেওয়া যাবে না!")

# finally:
#     print("কাজ শেষ!")  # সবসময় চলবে

# try:
#     a = int(input("Enter number-1: "))
#     b = int(input("Enter number-2: "))
#     result = a / b
# except ZeroDivisionError:
#     print(ZeroDivisionError)
# except ValueError:
#     print(ValueError)
# else:
#     print(result)
# finally:
#     print("All code are run")


# class InsuficientBalance(Exception):
#     pass


# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsuficientBalance("Amount is lower")


# try:
#     withdraw(500, 1000)
# except InsuficientBalance as e:
#     print(e)


# একটা withdraw function বানাও যেখানে —

# Balance 0 এর কম হলে — ValueError দেবে
# Amount, Balance এর বেশি হলে — InsufficientFundsError দেবে
# সফল হলে — বাকি balance দেখাবে
# সবশেষে সবসময় — "transaction শেষ" print হবে


# class InsufficientFundsError(Exception):
#     pass


# def withdraw(balance, amount):
#     if balance <= 0:
#         raise ValueError("Value error")
#     elif amount > balance:
#         raise InsufficientFundsError("Amount is Lower")
#     else:
#         result = balance - amount
#         print(result)

# try:
#     withdraw(0,500)
# except InsufficientFundsError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("transaction শেষ")

# 1. একটা function বানাও যেটা user এর বয়স নেবে। বয়স negative হলে ValueError, ১৫০ এর বেশি হলে custom AgeError দেবে।

# class AgeError(Exception):
#     pass

# def Age(age):
#     if age <= 0:
#         raise ValueError("Enter your valid age")
#     elif age > 150:
#         raise AgeError("Long live")
#     else:
#         print(f"Hello, your age is {age}")
# try:
#     Age(160)
# except ValueError as e:
#     print(e)
# except AgeError as e:
#     print(e)


# 2. একটা function বানাও যেটা list থেকে index দিয়ে value বের করবে। ভুল index দিলে সুন্দর message দেবে, crash করবে না।


def list_function(llist, index):
    try:
        print(llist[index])
    except IndexError:
        print("ভুল index দিয়েছ!")


list_function([10, 20, 30], 5)
list_function([10, 20, 30], 1)
