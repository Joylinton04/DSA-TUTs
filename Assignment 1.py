#Name: Ezekiel Kombat
#Class: CSCI 133
#Date : May 27, 2025
word = 'coronavirus'
unique_letters = ''
for letter in word:
    if letter not in unique_letters:
        unique_letters += letter

for letter in unique_letters:
    print(f"coronavirus contains {letter}")

medications = ['remdesivir', 'hydroxychloroquine', 'kaletra', 'favipiravir']
diseases = ['coronavirus', 'hepatitis', 'malaria', 'influenza']

for med in medications:
    for disease in diseases:
        print(f"Can {med} treat {disease}?")
for letter in unique_letters:
    for med in medications:
        if letter in med:
            print(f"{letter} is in coronavirus and also in {med}")
