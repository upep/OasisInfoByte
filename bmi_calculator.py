weight=float(input("Please enter your weight in kg : "))
height=float(input("Please enter your height in m : "))

bmi=weight/(height*height)

print("Your bmi is "+str(bmi))

if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<=24.9  :
    print("You are normal weight")
elif bmi>=25 and bmi<=29.9:
    print("You are overweight")
elif bmi>=30:
    print("You are obese") 

                   