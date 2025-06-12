import re


# this method substitutes the pattern with nothing 
# re.sub(r"[^a-zA-Z0-9\s.,@]", "")

def checkEmail():
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net)"

    email = input("Enter your email: ")

    if(re.search(pattern, email)):
        print("Valid")
    else:
        print("Invalid"),


def formatPhone():
    phone_pattern = r"(\d{3})(\d{4})(\d{4})"
    phone = input("Enter your phone: ")
    formatted = re.sub(phone_pattern, r"\1-\2-\3", phone)
    
    if(formatted):
        print(formatted)
    else:
        print("Invalid")

formatPhone()