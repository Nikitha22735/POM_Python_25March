
import csv
import json


def jsonhandling():
    filepath = "testData/credentials.json"

    #reading the jsonFile
    with open(filepath) as data:
        formattedData = json.load(data)
        print(formattedData["negitiveCredentials"]["password"])

def test_handlingCsv():
    values = []
    filepath="testData/credentails.csv"
    with open(filepath) as data:
        formattedData = csv.DictReader(data)
        for i in formattedData:
            values.append(i)

    print(values[0]["password"])



# [1,2,3]
#     [
#         {'username': 'test1@gmail.com', 
#          'password': 'Admin1@123', 
#          'age': '20'
#          }, 
#          {'username': 'test2@gmail.com', 
#           'password': 'Admin2@123', 
#           'age': '20'
#           }
#     ]
        
        
