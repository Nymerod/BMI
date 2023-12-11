
name = input('Welcome to the BMI index calculator, to start, please enter your name\n')

print('Hello', name, 'what is your current weight in kilograms ? If you want to use lbs simply add \' lbs \' to your number, \n (eg ; 65, or 130lbs)')
weight = input()
height = input('Please enter your height in cm')

height = int(height)
weight = int(weight)

BMI = weight/((height*10**-2)**2)


print(BMI)




