# Retrieve accounts by Reading Json file?
import json

file_path = "accounts.json"


def check_account(nameParam):
    print("Inside check_account")

    with open(file_path, "r") as file:
        data = json.load(file)

    for account in data["accounts"]:
        print(account)
        if account["name"] == nameParam:
            print("Found")
            return ("Exist", "True")
        else:
            continue

    return ("Not Found", "False")
