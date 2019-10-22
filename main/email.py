import re
import db

# **********************      
# *** CONSOLE METHOD ***
# **********************
def console():
    db.printAllEmails();
    address = raw_input(" Email: ")

    try:
        verified = verify(address)
        if verified:
            print("\n \"" + address + "\" is a valid email address.\n")
        else:
            print("\n \"" + address + "\" is not a valid email address.\n")

        db.saveEmail(address, verified)
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")

# ************************************************************************       
# *** VERIFY METHOD - Takes in address and returns boolean (validated) ***
# ************************************************************************
def verify(address):
    pattern = re.compile(r'^[^@.0-9\"(),:;<>[\\\]\'](?!.*?\.\.)[^@\"(),:;<>[\\\]\']+[^@.\"(),:;<>[\\\]\']+@(?!.*?--)(?!.*?@)[a-zA-z0-9-]+\.[a-zA-z0-9-.]*[a-zA-z0-9]$')
    return not(pattern.match(address) == None)