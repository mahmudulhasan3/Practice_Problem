# def add(a:int, b:int) -> int:
#     return a+b
# print(add(3,4))
# # print(add("3", 4))


# def add(a,b):
#     return a + b
# print(add(3, 4))
# print(add("3", 4))


# def greet(name:str) -> str:
#     return name
# print(greet("Mahmud"))

# def greet(name:str) -> None:
#     print(name)
# greet("Mahmud")

# from typing import List
# def process(items: List[str]) -> str:
#     return

# from typing import List,Dict

# def create_marksheet(name:List[str],mark: List[int]) -> Dict[str,int]:
#     marksheet = {}
#     for names,marks in zip(name,mark):
#         marksheet[names] = marks
#     return marksheet
# names: List[str] = ["Mahmud", "Rahim", "Karim"]
# marks: List[int] = [90, 45, 75]
# print(create_marksheet(names,marks))

# 1. Simple
# greet(name) — নাম নেবে, "Hello, Mahmud!" return করবে। Type hint যোগ করো।

# def greet(name: str) -> str:
#     return f"Hello {name}"
# print(greet("Mahmud"))

# 2. Medium
# add(a, b) — দুইটা number নেবে, যোগ করে return করবে। Type hint যোগ করো।

# def add(a: int,b: int) -> int:
#     return a+b
# print(f"Summation = {add(4,5)}")

# 3. Hard
# find_user(user_id) — id নেবে, id == 1 হলে "Mahmud" return করবে, নাহলে None। Type hint যোগ করো।

# from typing import Optional

# def find_user(user_id: int) -> Optional[str]:
#     if user_id == 1:
#         return "Mahmud"
#     return None
# print(find_user(2))

# 1. Simple
# power(base, exponent) — দুইটা number নেবে, base ** exponent return করবে। Type hint যোগ করো।

# def power(base: int,exponent: int) -> int:
#     return base**exponent
# print(f"Result={power(3,4)}")

# 2. Medium
# get_length(words) — List[str] নেবে, প্রতিটা word এর length Dict[str, int] এ return করবে।
# ["Mahmud", "Rahim"] → {"Mahmud": 6, "Rahim": 5}

# from typing import List,Dict
# result = {}
# def get_length(words: List[str]) -> Dict[str,int]:
#     for i in words:
#         result[i]=len(i)
#     return result
# print(get_length(["Mahmud","hasan"]))

# 3. Hard
# find_even(numbers) — List[int] নেবে, শুধু even numbers গুলো List[int] এ return করবে। কোনো even না থাকলে None return করবে।
# [1, 2, 3, 4] → [2, 4]
# [1, 3, 5]    → None

# from typing import List,Optional


# def find_even(numbers: List[int]) -> Optional[List[int]]:
#     new_list = []
#     for i in numbers:
#         if i % 2 == 0:
#             new_list.append(i)
#     if len(new_list) == 0:
#         return None
#     return new_list
# print(find_even([1,3,5,7]))

# 1.
# student_pass(names, marks) — List[str] আর List[int] নেবে, যাদের marks 50+ তাদের Dict[str, int] return করবে।
# ["Mahmud", "Rahim", "Karim"], [90, 45, 75]
# → {"Mahmud": 90, "Karim": 75}

from typing import List, Dict
def student_pass(names: List[str],marks: List[int]) -> Dict[str,int]:
    result = {}
    for k,v in zip(names,marks):
        if v >= 50:
            result[k] = v
    return result
print(student_pass(["Mahmud","Hasan","Jubair"],[70,80,50]))