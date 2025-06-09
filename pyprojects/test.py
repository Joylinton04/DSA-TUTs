import re

email_pattern = "[A-Za-z0-9]+@[a-z]+\.(com|edu|net)"
email = "example@gmailcom"

if(re.search(email_pattern, email)):
    print("Valid Email")
else:
    print("Invalid Email")
