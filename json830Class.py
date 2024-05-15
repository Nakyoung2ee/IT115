#Import json library
import json

#Dictionary named data
data = {
  'name': 'John Doe',
  'age': 30,
  'city': 'New York, NY',
  'interests': ['Reading', 'Traveling', 'Tennis', 'Ballet'],
  'is_student': False
}

#Open the json file and write to the json file.
with open('data.json', 'w') as json_file:
  #Write content of data to json_file
  json.dump(data, json_file, indent=4)
#Print a statement to inform that writing is done.
print("Data has been written to data.json")


#Read a json file
with open('data.json', 'r') as json_file:
  #Load a json content to loaded_data
  loaded_data = json.load(json_file)


print("Successfully able to read data.json")
print(loaded_data)


#Change the content of loaded_data
loaded_data['age'] = 34
loaded_data['interests'].append('History')

#loaded_data[interests].remove('Put Your String Here')

#Rewrite the changes to the json file.
with open('data.json', 'w') as json_file:
  #Write contet of loaded_data to json_file
  json.dump(loaded_data, json_file, indent=4)
#Print the json content
print("Data has been re-written to data.json")
print(loaded_data)