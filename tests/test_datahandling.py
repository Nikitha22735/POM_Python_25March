
import csv
import json
import os
import allure
from dotenv import load_dotenv
from openpyxl import load_workbook
import pytest

@pytest.mark.test1
@allure.step("Handling JSON file")
def test_sonhandling():
    filepath = "testData/credentials.json"

    #reading the jsonFile

    with open(filepath) as data:
        formattedData = json.load(data)
        print(formattedData["negitiveCredentials"]["password"])

def handlingCsv():
    values = []
    filepath="testData/credentails.csv"
    with open(filepath) as data:
        formattedData = csv.DictReader(data)
        for i in formattedData:
            values.append(i)

    print(values[0]["password"])

# #python -m pip install openpyxl
# def test_excelHandling():
#     filepath ="testData/creds.xlsx"
#     workbook = load_workbook(filepath)
#     sheet = workbook["creds"]
#     values = []
#     for i in sheet.iter_rows(min_row=2, values_only=True):
#         values.append(i)

#     print(values)

#cmd
# set usname=testing123&&set pw=welcome&&pytest tests/test_datahandling.py -s
#powershell
#$env:usname=testing123;$env:pw=welcome;pytest tests/test_datahandling.py -s
def test_passingDataThroughCLI():
    username = os.getenv("usname")
    pw = os.getenv("pw")
    print(username)
    print(pw)


#pip install python-dotenv
def passingDataThroughEnv():
    load_dotenv(dotenv_path=os.getenv("envpath"))
    username = os.getenv("usname")
    pw = os.getenv("pw")
    print(username)
    print(pw)







        
        
