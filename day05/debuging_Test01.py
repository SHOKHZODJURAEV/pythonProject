def my_function():
    for i in range(1, 20+1):
        if i == 20:
            print("You got it")

my_function()

from random import randint
dice_imgs = ["@1", "@2", "@3", "@4", "@5", "@6", "@7"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])


# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1995:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z")


# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print("You can drive the car")
