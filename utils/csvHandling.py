import csv


def csvData(filepath):
    values = []
    with open(filepath) as data:
        formattedData = csv.DictReader(data)
        for i in formattedData:
            values.append(i)

    return values