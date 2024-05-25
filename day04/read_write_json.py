import json

path = 'files/Test.json'
# open(path, 'r')
json_file = open(path, 'r')
print(json_file.read())

#load_dict = json.load(json_file)  # converting from json to dictionary

#print(load_dict)

#for x in dict(load_dict).keys():
    #print(x)
    #print(load_dict[x])


json_file.close()

#json_file['name'] = "Shawn Wang"
#json_file['age'] = 45

print(json_file)

students = {
    'A01': {
        'name': 'A01',
        'age': 18,
        'height': 1.5,
        'weight': 23,
        'eye_color': ['blue', 'green']
    },

    'A02': {
        'name': 'A02',
        'age': 18,
        'height': 1.5,
        'weight': 23,
        'eye_color': ['blue', 'green']
    }
}

jason_file = open('files/Test2.json', 'w')
json_object = json.dumps(students, indent=3)  # converting dictionary object to json object
jason_file.write(json_object)


"""
Web Automation Solution 2
BeautifulSoup4
request
pytest
robot

web development

    Django
    FastApi
    flask

"""





