import json


def jsonFile(filepath):
    # filepath = "testData/credentials.json"
    with open(filepath) as data:
        formattedData = json.load(data)
    return formattedData