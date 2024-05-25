import os

path = '/Users/shokhzodjuraev/Desktop/Hello'
print(path)

text_file = open(path, 'r')

print(text_file.read())
print(text_file.readline())
text_file.close()



newPath = 'files/Test2.txt'

text_file2 = open(newPath, 'w')

text_file2.write('This is a new text file \n Python created this file')

text_file2.close()

print('---------------------------------------------')

os.remove(newPath)


