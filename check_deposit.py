# this will check if the amount is valid or not
# should check the function name to - check if it's a integer/float rather than deposit 'check_deposit_amount'


def check_deposit_amount(depositParam):
    try:
        toFloatDeposit = float(depositParam)
        if toFloatDeposit <= 0:
            return ("Invalid", toFloatDeposit)
        else:
            return ("Valid", toFloatDeposit)

    except ValueError:
        print(f"Cannot conver this amount to float-- NaN {depositParam}")
        return ("Invalid", depositParam)


# check_deposit_amount("2313212.2")
