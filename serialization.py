# serialization and deserialization in python
# marshall module
# pickle module
# JSON module
import json
import pickle
import marshal

data = {'name': 'sreekanth', 'age': 22, 'address': 'hyderabad'}


bytes = marshal.dumps(data)
print('After serialization:', bytes)

new_data = marshal.loads(bytes)
print('After deserialization:', new_data)

# pickle module
data = {'st_name': 'Sunny', 'st_id': '9607', 'st_add': 'Nasik'}
with open('data.pickle', 'wb') as f1:
    pickle.dump(data, f1)
    print('pickling completed')
with open('data.pickle', 'rb') as f2:
    print('unpickling the data')
    data = pickle.load(f2)
    print(data)


# importing the module

# JSON string
students = '{"id":"9607", "name": "Sunny", "department":"Computer"}'

# convert string to Python dict
student_dict = json.loads(students)
print(student_dict)

print(student_dict['name'])
print('Deserialization Completed.')


# importing the module

data = {
    "id": "877",
    "name": "Mayur",
    "department": "Comp"
}

# Serializing json
json_object = json.dumps(data)
print(json_object)
print('Serialization Completed.')
