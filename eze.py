word = "coronavirus"
medications = ['remdesivir', 'hydroxychloroquine', 'kaletra', 'favipiravir']
diseases = ['coronavirus', 'hepatitis', 'malaria', 'influenza']

unique_letters = ""

for letter in word:
    if letter not in unique_letters:
        unique_letters += letter

# I sorted the unique letters here to get them in alphabetical order
sorted_letters = sorted(unique_letters)

for sorted_letter in sorted_letters:
    print(f"{word} contains {sorted_letter}")

for med in medications:
    for disease in diseases:
        print(f"Can {med} treat {disease}?")
    print("\n")

for sorted_letter in sorted_letters:
    for letter in medications:
        if sorted_letter in letter:
            print(f"{sorted_letter} is in {word} and also in {letter}")
