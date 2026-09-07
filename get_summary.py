import json


file_path = "accounts.json"


def get_summary(keyParam):
    # this should return transaction array?
    header = ["--Type--", "--Amount--", "--Status--"]
    
    
    arrayofArray = [header]
    current_Total = 0
    with open(file_path, "r") as readFile:
        data = json.load(readFile)

    for key, value in enumerate(data["accounts"][keyParam]["Transactions"]):
        arrayofArray.append([value['type'], value['amount'], value['status']])

    # get the balanace
    current_Total = data["accounts"][keyParam]["Balance"]

    return (current_Total,arrayofArray)


# get_summary(1)
