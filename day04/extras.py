from functools import reduce

print('---------------------------Closure-------------------------')


def display_message():

    def method():
        for i in range(0,5):
            print('Hello World')
            print('I love Python')


    method()
    method()

display_message()


print('------------------------------------------------')

def display_palindromes(strings: list):

    for s in strings:
        new_s = ''
        for i in reversed(range(0, len(str(s)))):
            new_s += str(s)[i]

    def is_palindrome(s: str) -> bool:
        return s == s[::-1].lower() == s.lower()

    for s in strings:
        if is_palindrome(s):
            print(s)


listTest = ['level', 'test', 'cool']
display_palindromes(listTest)

print('-------------------------Map----------------------------')


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

nums = list(map(lambda x: x * 10, nums))
print(nums)

names = ('Java', 'JAVA', 'PHP', 'Python', 'Ruby', 'CyDEo', 'JavaSCript')

pLanguages = list(map(lambda x: str(x).upper(), names))

print(pLanguages)

dictionaryData = {'x': 100, 'y': 200, 'z': 300}

dictionaryTest = dict(map(lambda t: (t[0], t[1] * 10), dictionaryData.items()))
print(dictionaryTest)

print('---------------------------------Filter-------------------------------')
raqam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#raqam = [x for x in raqam if x % 5 == 0]
filteredRaqam = list(filter(lambda x: x % 5 == 0, raqam))
print(filteredRaqam)

names = ['Java', 'JAVA', 'PHP', 'Python', 'Ruby', 'CyDEo', 'JavaSCript']

#namesResult = [a for a in names if not a.lower().startswith('j')]

namesResult = list(filter(lambda x: not str(x).lower().startswith('c'), names))
print(namesResult)

print('--------------------------Reduce-------------------------------')
listCheck = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, listCheck))

list2 = ['Java', 'Python', 'Ruby', 'CyDEo', 'JavaSCript', 'C#']
print(list2)
print(reduce(lambda x, y: f'{x} {y}', list2))





