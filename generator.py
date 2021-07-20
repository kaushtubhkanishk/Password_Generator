import random

#Listing all the digits and alphabets as strings 
Digits = "01234567890"
Lower_Case = "abcdefghijklmnopqrstuvwxyz"
Upper_Case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols = "@#$%^&*"

#Combining the lists into a combined list
Combined_List = Digits + Upper_Case + Lower_Case + Symbols
temp_password = random.choice(Digits) + random.choice(Upper_Case) + random.choice(Lower_Case) + random.choice(Symbols) 
password_len = int(input("What is the length of your password (minimum 4)"))


#For loop to generate the password
for x in range (0, password_len - 4):
    temp_password = temp_password + random.choice(Combined_List)
    l = list(temp_password)
    random.shuffle(l)
    password = ''.join(l)
print(password)