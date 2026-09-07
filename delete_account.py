# this method will remove the account from file

import json

file_path = "accounts.json"


def remove_account(keyParm):
    # read json file
    # remove the account via pop?
    # dump it agai
    with open(file_path, mode="r") as readFile:
        data = json.load(readFile)

    print(data["accounts"].pop(keyParm))
    print("Current", data)

    with open(file_path,mode='w') as reWrite:
        json.dump(data,reWrite)

# remove_account(1)
