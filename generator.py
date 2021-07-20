import random

Digits = "01234567890"
Lower_Case = "abcdefghijklmnopqrstuvwxyz"
Upper_Case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols = "@#$%^&*"
Combined_List = Digits + Upper_Case + Lower_Case + Symbols
temp_password = random.choice(Digits) + random.choice(Upper_Case) + random.choice(Lower_Case) + random.choice(Symbols) 
password_len = int(input("What is the length of your password (minimum 4)"))

for x in range (0, password_len - 4):
    temp_password = temp_password + random.choice(Combined_List)
    l = list(temp_password)
    random.shuffle(l)
    password = ''.join(l)
print(password)