import os
from os import system
system("clear")

name = input(" Whats your name ? ")
unit = input("Hello " + name + ", What unit do you prefer? (C or F)")
while unit != 'f' and unit != 'c':
    unit = input("This is not an option, Please choose C or F")
if unit == "f":
    while True:
        temp = input("What is the Temperature in celcuis")
        if temp.isdigit():
            temp = int(temp)
            break
        else:
            print("This is not a number, please try again.")
    solve = str((temp /1.8) + 32)
    print('The temperature in Farenhight is ' + solve + ".")
elif unit =="c":
    while True:
        temp = input("What is the Temperature in Farenhight")
        if temp.isdigit():
            temp = int(temp)
            break
        else:
            print("This is not a number, please try again.")
    solve = str((temp - 32) * 1.8)
    print('The temperature in Celcius is ' + solve + ".")
   
    
