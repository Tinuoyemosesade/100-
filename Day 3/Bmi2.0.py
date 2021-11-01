user_height = float(input("what is your height"))
user_weight = float(input("what is your weight"))
user_bmi =  round (user_weight /(user_height**2), 2)

if user_bmi < 18.5:
    print( f"your bmi is{user_bmi}, you are underweight")
elif user_bmi < 25 :
        print ("you have normal weight")
elif user_bmi < 30:
            print ("you are overweight")
else:
                print ("you are obese")
