
import check_accounts as c_accounts

### spaghetti~

def account_exist(name):
    isAccountTakenMessage, isAccountTakenStringBool = c_accounts.check_account(name);
    print(isAccountTakenStringBool)
    if isAccountTakenMessage == "Exist":
        return "Existing"
    else: 
        return "Not Found"
   
   
   
   
   