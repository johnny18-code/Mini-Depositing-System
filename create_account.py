# Account creation -- appending to Json??
# still need fixing

import json
file_path = "accounts.json"


def create_account(namePara, AmountPara):
    print(namePara, AmountPara)
    dataInput = {"name": namePara, "Balance": AmountPara, "Transactions": [{"type": "Creation", "amount":
                                                                            AmountPara, "status": "successful"}]}
    # READ THE file first then re-write;
    file_path = "accounts.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    print(data)
    print(data["accounts"].append(dataInput))
    print(len(data["accounts"]))
    print(data)

    with open(file_path,"w") as toWriteFile:
        json.dump(data,toWriteFile)

    # combineData = data["accounts"].append(dataInput);

    #
    # with open(file_path, "w") as file:
    # json.dump(combineData, file)


# seems like read then rewrite....

# create_account("Johnny", 350)
