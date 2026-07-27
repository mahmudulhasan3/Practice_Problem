# print("Hello World!")
# print("Mahmudul Hasan")
# print("Student ID: CS-2203009")

# egg = 20
# milk = 40

# print(egg,milk)

# rice_price      = 65      # চালের দাম (প্রতি কেজি)
# oil_price       = 175     # তেলের দাম (প্রতি লিটার)
# sugar_price     = 120     # চিনির দাম (প্রতি কেজি)
# flour_price     = 55      # আটার দাম (প্রতি কেজি)
# lentil_price    = 130     # ডালের দাম (প্রতি কেজি)
# salt_price      = 35      # লবণের দাম (প্রতি কেজি)
# milk_price      = 80      # দুধের দাম (প্রতি লিটার)
# egg_price       = 12      # ডিমের দাম (প্রতিটা)
# potato_price    = 45      # আলুর দাম (প্রতি কেজি)
# onion_price     = 60      # পেঁয়াজের দাম (প্রতি কেজি)


# print("=" * 35)
# print("     আমার দোকানের দাম তালিকা")
# print("=" * 35)
# print(f"চাল        : {rice_price} টাকা/কেজি")
# print(f"তেল        : {oil_price} টাকা/লিটার")
# print(f"চিনি       : {sugar_price} টাকা/কেজি")
# print(f"আটা        : {flour_price} টাকা/কেজি")
# print(f"ডাল        : {lentil_price} টাকা/কেজি")
# print(f"লবণ        : {salt_price} টাকা/কেজি")
# print(f"দুধ        : {milk_price} টাকা/লিটার")
# print(f"ডিম        : {egg_price} টাকা/পিস")
# print(f"আলু        : {potato_price} টাকা/কেজি")
# print(f"পেঁয়াজ    : {onion_price} টাকা/কেজি")
# print("=" * 35)

# তোমার নিজের তথ্য দিয়ে একটা program লেখো:
# name, age, city, dream_job — এই ৪টা variable বানাও
# এবং সুন্দরভাবে print করো।

name = "Mahmudul Hasan"
age = 24
city = "Dhaka"

print(f"My name is {name}, I am {age} years old. I live in {city} ")

# দোকানের program-এ একটা "total" variable যোগ করো
# যেটা সব জিনিসের দামের যোগফল রাখবে।
# Hint: total = rice_price + oil_price + ...

rice_price      = 65      
oil_price       = 175   
sugar_price     = 120     
flour_price     = 55    
lentil_price    = 130    
salt_price      = 35     
milk_price      = 80      
egg_price       = 12      
potato_price    = 45     
onion_price     = 60   

total = rice_price + oil_price + sugar_price + flour_price + lentil_price + salt_price + milk_price + egg_price + potato_price + onion_price

print(f"Your total price has= {total}")

# একটা "discount" variable বানাও (যেমন 10)
# প্রতিটা জিনিসের উপর ১০% discount দেওয়া price
# আলাদাভাবে print করো।
# Hint: discounted = original_price - (original_price * discount / 100)

discount = total * .01
total_price = total - discount
print(f"Your discounted  = {discount} tk and total price = {total_price} ")