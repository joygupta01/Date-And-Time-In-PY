number = int(input("Enter Number : "))
print("This Is Your Number" ,number)

if number%2==0 :
    print("This is even number")

else :
    print("This Is Odd Number")

num= int(input("Enter Your number "))

if num>50 :
    print("Your Number Is Greater Than 50")

    if num%2==0 :
        print("And Is even Too")
    else :
        print("And it is odd")

else :
     print("Your Number Is Lesser Than 50")


import datetime

current_time = datetime.datetime.now()
print("\n",current_time)

import calendar
print("\n",calendar.calendar(2025))
