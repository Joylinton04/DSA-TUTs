import re

pattern = "[a-zA-Z0-9]+@[a-z](.com)"

# this method substitutes the pattern with nothing 
# re.sub(r"[^a-zA-Z0-9\s.,@]", "")

word = "example05@gmail.com"

if(re.search(pattern, word)):
    print("Valid")
else:
    print("Invalid")



