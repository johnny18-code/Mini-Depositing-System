import json

file_path = "accounts.json"

def log_withdraw(keyName,Amount):
    print("Logging withdraw")
    loadLog = { "type": "Withdraw", "amount": Amount, "status": "successful" }

    with open(file_path,"r") as readFile:
        dataKey = json.load(readFile)
        print(dataKey["accounts"][keyName])
    dataCurrentBalanace = dataKey["accounts"][keyName]["Balance"]
    toPasteTotal = 0;
    if (dataCurrentBalanace - Amount) <= 0:
        return "Invalid"
    else:
        # update the current balance and log now
        toPasteTotal = dataCurrentBalanace - Amount
        dataKey["accounts"][keyName]["Balance"] = toPasteTotal;

        # append transaction 
        dataKey["accounts"][keyName]["Transactions"].append(loadLog)

        # re-write...
        with open(file_path,"w") as writeFile:
             json.dump(dataKey,writeFile)

        return "Valid"
    print("here",dataCurrentBalanace)

    print("Ending withdraw func")
    # caculate first if eligible for withdraw~
