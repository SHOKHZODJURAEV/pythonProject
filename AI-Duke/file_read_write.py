
# This script demonstrates how to read from and write to a file in Python.# Writing to a file
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
