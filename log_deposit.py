import json


file_path = "accounts.json"


# already spaghetting code ~
def check_key(nameParam):
    with open(file_path, mode="r") as jFile:
        dataKey = json.load(jFile)

    for key, account in enumerate(dataKey["accounts"]):
        if account["name"] == nameParam:
            return key
        else:
            continue
    return "NF"


# print(check_key("Johnny"))

def insert_tran(keyParam, amountToInsert):
    # can put Try/Catch on KeyError
    try:
        loadToTran = {"type": "Deposit",
                      "amount": amountToInsert, "status": "successful"}

        with open(file_path, mode="r") as jFile:
            dataKey = json.load(jFile)

    # Update Balance first:
            dataKey["accounts"][keyParam]["Balance"] += amountToInsert

    # insert Transaction

            dataKey["accounts"][keyParam]["Transactions"].append(loadToTran)

    # then dump
        with open(file_path, mode="w") as dumpFile:
            json.dump(dataKey, dumpFile)

        return "Successful"

    except IndexError as e:
        print(f"Index error {e}")
        return "Unsuccessful"

# 
# print(insert_tran(keyParam=10,amountToInsert=300))
