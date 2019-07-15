import re

test = "the ghost that says boo haunts the loo"

found = re.findall(".oo", test)

print(found)
