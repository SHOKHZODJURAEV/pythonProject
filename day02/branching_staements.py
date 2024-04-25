
for i in range(1, 6):
    print(i)
    if i == 3:
        break
print('---------------------------------------')

for i in range(1, 6):
    if i == 3 or i == 5:
        continue
    print(i)

print('--------------------------------------')
for i in range(1, 6):
    if i == 3 or i == 5:
        pass
    print(i)


def function():
    pass


if True:
    pass


class Class:

    def method(self):
        pass
    pass

