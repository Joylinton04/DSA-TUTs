import re

pattern = "[a-zA-Z0-9]+@[a-z](.com)"
word = "example05@gmail.com"

if(re.search(pattern, word)):
    print("Valid")
else:
    print("Invalid")
