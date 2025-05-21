height = float(input("Enter Your Height In CM"))
weight = float(input("Enter Your weight In kg"))

BMI = weight/(height/100)**2
print("Your BMI Is ",BMI)

if BMI <= 18.4 :
   print("Your are UNDERWEIGHT") 

elif BMI <= 24.9 :
   print("Your are HEALTHY")    

elif BMI <= 29.9 :
   print("Your are OVER WEIGHT")  

else : 
   print("You are OBESE")