#THIS PROGRAM FOR CALCULATE THE BMI AND TELL ABOUT BMI CATEGORY....
weight=input("Enter your Weight (in kg):")
height=input("Enter your Height (in foot):")
HeightinMeter=round(float(height)*0.3048,4)#HERE PROGRAMER CONVERT THE HEIGHT INTO METER AND ROUND IT..
print('Your weight is: '+weight)
print('YOur Height is(in Meter): '+str(HeightinMeter))
BMI=int(int(weight)//float(HeightinMeter)**2)
if BMI<16.0:
    print(f'Your BMI is {BMI} and you are underweight(Servere thinness)')
elif (BMI==16.0 and BMI<=16.9):
    print(f'Your BMI is {BMI} and you are underweight(Moderate thinness)')
elif BMI>=17.0 and BMI<=18.4:
    print(f'Your BMI is {BMI} and you are underweight(Mild thinness)')
elif BMI>=18.5 and BMI<=24.9:
    print(f'Your BMI is {BMI} and you are Normal range')
elif (BMI>=25.0 and BMI<=29.9):
    print(f'Your BMI is {BMI} and you are Overweight(Pre-obese)')
elif BMI>=30.0 and BMI<=34.9:
    print(f'Your BMI is {BMI} and you are Obese(Class 1)')
elif BMI>=35.0 and BMI<=39.9:
    print(f'Your BMI is{BMI} and you are Obese(Class 2)')
elif BMI>=40.0:
    print(f'Your BMI is{BMI} and you are Obese(Class 3)')

