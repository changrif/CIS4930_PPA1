import re

def verify(address):
    pattern = re.compile(r'^[^@.0-9(),:;<>@[\]](?![]*.{2})[^@.]@[^@]+$')
    return not(pattern.match(address) == None);