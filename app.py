# mini depositing system :)
import json
from nt import close
from tkinter import Scrollbar
import account_exist as accountExistFunc
import check_deposit as checkDepositFunc
import create_account as createfunc

import log_deposit as key_checkFunc
import log_withdraw as key_withDrawClass
import get_summary as key_summaryFunc


import FreeSimpleGUI as cv


def close_program():
    window.close()


def test():
    return "x"


action_holder = ""
# events are those clicks/buttons

# Texts are labels
user_name_label = cv.Text("Enter account name")
user_name_input_box = cv.InputText(
    tooltip="Enter account name", key="AccountName")

user_amount_label = cv.Text("Enter amount")
user_amount_input = cv.InputText(
    tooltip="Amount will be entered", default_text="0", key="Amount")

user_actions_label = cv.Text("Actions: ")

# event buttons:
user_button_create_account = cv.Button("Create Account")
user_button_deposit = cv.Button("Deposit")
user_button_withdraw = cv.Button("Withdraw")
user_button_summary = cv.Button("Show Account Summary")
user_button_close = cv.Button("Close Program")


# listbox
# enable_event=True if you want the item to be the actual event
user_list_box_label = cv.Text("Account Summary")
user_list_box = cv.Listbox(
    ["----"], size=[45, 5], key="AccountSummaryKey")


window = cv.Window("Mini Banking System", layout=[
    [user_name_label, user_name_input_box],
    [user_amount_label, user_amount_input],
    [user_list_box_label],
    [user_list_box],
    [user_actions_label],
    [user_button_create_account, user_button_deposit,
        user_button_withdraw, user_button_summary, user_button_close]
]  # layout end
)

while action_holder != "Close Program":
    event, data = window.read()
    print(event, data)

    action_holder = event

    # match case
    match event:

        case "Create Account":
            print("Creating account...")
            isAccountExist = accountExistFunc.account_exist(
                data["AccountName"])
            if isAccountExist == "Existing":
                cv.popup(
                    f"Account is already existing for {data["AccountName"]}, you mean Deposit?")
            elif isAccountExist != "Existing" or isAccountExist == "Not Found":
                print("Further Check... check amount")
                isValidAmountMessage, isValidAmount,  = checkDepositFunc.check_deposit_amount(
                    data["Amount"])
                if isValidAmountMessage == "Valid":
                    cv.popup(
                        f"Customer: {data["AccountName"]} with depositing amount of: {isValidAmount}, message : {isValidAmountMessage}")
                    # Creating new account
                    # Inserting to json.
                    createfunc.create_account(
                        data["AccountName"], isValidAmount)
                    cv.popup("Account Created")
                else:  # invalid
                    cv.popup(
                        f"Customer: {data["AccountName"]} with depositing amount of: {isValidAmount}, message : {isValidAmountMessage}")
                    # None - just pop-up error?

            else:
                print("Unknown error Creating Account")

        case "Deposit":
            print("Depositing to the account...")
            isAccountExist = accountExistFunc.account_exist(
                data["AccountName"])
            if isAccountExist == "Existing":
                cv.popup("Account Existing for Deposit")
                isValidAmountMessage, isValidAmount,  = checkDepositFunc.check_deposit_amount(
                    data["Amount"])
                print(data["AccountName"], isValidAmount)
                if isValidAmountMessage == "Invalid":
                    print("the amount is invalid for deposit")
                else:
                    get_key = key_checkFunc.check_key(data["AccountName"])
                    if get_key != "NF":
                        inserted = key_checkFunc.insert_tran(
                            get_key, isValidAmount)
                        if inserted == 'Successful':
                            cv.popup(
                                f"Deposit Logged for {data["AccountName"]}")
                        else:
                            cv.popup(
                                f"Erro in depositing for {data["AccountName"]}")
                    else:
                        print(
                            f"unable to insert transaction for the key {get_key}, NF")

            elif isAccountExist == "Not Found":
                cv.popup(
                    "This account is not existing for Deposit. Please create new first.")
            else:
                cv.popup("Unknown error, clear Text Boxes")

        case "Withdraw":
            print("Withdrawing from the account...")
            isAccountExist = accountExistFunc.account_exist(
                data["AccountName"])
            if isAccountExist == "Existing":
                # check if the withdraw amount is a number
                isValidAmountMessage, isValidAmount,  = checkDepositFunc.check_deposit_amount(
                    data["Amount"])
                if isValidAmountMessage == "Invalid":
                    cv.popup(
                        f"This withdraw 'amount' is invalid {data["Amount"]}")
                else:
                    # get key -- first check exist okay -- 2nd check amount okay
                    get_key = key_checkFunc.check_key(data["AccountName"])
                    if get_key != "NF":
                        withdrawStatus = key_withDrawClass.log_withdraw(
                            get_key, isValidAmount)
                        if withdrawStatus == "Valid":
                            cv.popup("Valid Withdrawal -- Logged")
                        else:
                            cv.popup(
                                "The amount to withdraw is bigger than current Balance, are you high?")
                    else:
                        cv.popup(
                            "This account not existing for withdrawal. Create new Account First?")

            else:
                cv.popup(
                    "This account not existing for withdrawal. Create new Account First?")

        case "Show Account Summary":
            # work on this next~
            print("Showing Account Summary...")
            # mother Window -- updates based on KEYS real time update of GUI -- on event
            # if 'value' then string if values then enclosed with [] as array
            if data["AccountName"] == '':
                print("empty")
            else:
                isAccountExist = accountExistFunc.account_exist(
                    data["AccountName"])
                if isAccountExist == "Existing":
                    get_key = key_checkFunc.check_key(data["AccountName"])
                    returnedArrayValues = key_summaryFunc.get_sum(get_key)

                    window["AccountSummaryKey"].update(
                        values=returnedArrayValues)
                else:
                    cv.popup("Account not found for Summary, create new?")

        case "Close Program":
            print("Closing the programm...")
        case cv.WIN_CLOSED:
            # X button
            action_holder = "Close Program"
            close_program()
        case _:
            print("Unknown command...")

else:
    print(action_holder)
    print("Closing the program gracefully...")
    close_program()
