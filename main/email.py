import re

# ************************************************************************       
# *** VERIFY METHOD - Takes in address and returns boolean (validated) ***
# ************************************************************************
def verify(address):
    pattern = re.compile(r'^[^@.0-9\"(),:;<>[\\\]\'](?!.*?\.\.)[^@\"(),:;<>[\\\]\']+[^@.\"(),:;<>[\\\]\']+@(?!.*?--)(?!.*?@)[a-zA-z0-9-]+\.[a-zA-z0-9-.]*[a-zA-z0-9]$')
    return not(pattern.match(address) == None)