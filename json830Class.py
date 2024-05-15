#Import json file
import json

#Dictionary named data
data = {
  'name': 'John Doe',
  'age': 30,
  'city': 'New York, NY',
  'interests': ['Reading', 'Traveling', 'Tennis', 'Ballet'],
  'is_student': False
}

#write the json file.
with open('data.json', 'w') as json_file:
  #Converting into json
  json.dump(data, json_file, indent=4)
#Result
print("Data has been written to data.json")


#Read a json file
with open('data.json', 'r') as json_file:
  #Load a json file
  loaded_data = json.load(json_file)


print("Successfully able to read data.json")
print(loaded_data)


#Change values to the json file
loaded_data['age'] = 34
loaded_data['interests'].append('History')

#loaded_data[interests].remove('Put Your String Here')

#Rewrite the changes to the json file.
with open('data.json', 'w') as json_file:
  #Converting into json
  json.dump(loaded_data, json_file, indent=4)
#Result
print("Data has been re-written to data.json")
print(loaded_data)