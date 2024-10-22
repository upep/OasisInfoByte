import random
import string

length=int(input("Please enter the length of your password"))

characters=input("Do you want to include characters (y/n) ?")
numbers=input("Do you want to include numbers (y/n) ?")
symbols=input("Do you want to include symbols (y/n) ?")

char=""
if characters.lower()=="y":
 char=string.ascii_letters

if numbers.lower()=="y":   
 char+=string.digits

if symbols.lower()=="y": 
 char+=string.punctuation

password=""

for i in range(length):
    password +=random.choice(char)

print("Your random password is : ",password)
    
