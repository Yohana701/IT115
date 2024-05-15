#Import the json class library
import json 

#Create the data dictionary
data = {
    'name':'John Doe',
    'age': 30,
    'city':'New York,NY',
    'interest':['Photography','Running','Football','Traveling'],
    'is_student':False
}

#Creating a Json and writing the phyton object contents to the json
with open('data.json','w') as json_file:

#Converting the data dictionary into a Json string
    json.dump(data,json_file,indent=4)

#Printing a confirmation message 
print("Data has been written to data.json")


#Reading data from the data.json
with open('data.json','r') as json_file:

#Converting the Json string into a python object
    loaded_data = json.load(json_file)

#Printing a confirmation message along with the loaded data
print("Successfully able to read data.json")
print(loaded_data)

loaded_data['age'] = 34
loaded_data['interest'].append('Coding')
loaded_data['interest'].remove('Running')

#Rewriting the changes to the json
with open('data.json','w') as json_file:

#Converting the data dictionary into a Json string
    json.dump(loaded_data,json_file,indent=4)

#Printing a confirmation message 
print("Data has been re-written to data.json")

