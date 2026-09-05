import json


file_path = "accounts.json"


def get_sum(keyParam):
    # this should return transaction array?
    header = ["--Type--", "--Amount--", "--Status--"]
    arrayofArray = [header]
    with open(file_path, "r") as readFile:
        data = json.load(readFile)

    for key, value in enumerate(data["accounts"][keyParam]["Transactions"]):
        arrayofArray.append([value['type'], value['amount'], value['status']])

    return arrayofArray
  


# get_sum(0)
