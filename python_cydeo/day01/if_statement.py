browser_name = "chromee"

if browser_name == "chrome":
    print("Chrome browser detected")
elif browser_name == "firefox":
    print("Firefox browser detected")
else:
    print("Unknown browser detected")
print("End of the program")

print('-----------------------------------------------')

score = -200
if score >= 0 and score <= 100:
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("Invalid score")

print('-----------------------------------------------')

if True:
    pass
    print("This will always execute")
else:
    print("This will never execute")

print('-----------------------------------------------')

def function_name():
    print("Function executed")
    return True

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Skipping number 3")
        continue
    print(f"Processing number: {num}")