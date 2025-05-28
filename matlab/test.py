marks = {
    'enviroment_studies': int(input('Enter mark for Environment Studies: ')),
    'engineering_tech': int(input('Enter mark for Engineering Technology: ')),
    'algebra': int(input('Enter mark for Algebra: ')),
    'basic_mech': int(input('Enter mark for Basic Mechanics: ')),
    'applied_elec': int(input('Enter mark for Applied Electricity: ')),
    'tech_drawing': int(input('Enter mark for Technical Drawing: ')),
    'communication_skills': int(input('Enter mark for Communication Skills: '))
}


credit_hours = {
    'enviroment_studies': 2,
    'engineering_tech': 2,
    'algebra': 4,
    'basic_mech': 3,
    'applied_elec': 3,
    'tech_drawing': 2,
    'communication_skills': 2
}

total_marks = sum(marks[subject] * credit_hours[subject] for subject in marks)
standard_marks = 0
for course in credit_hours:
    standard_marks += 100*credit_hours[course]
    
print((total_marks/standard_marks)*100)

# ask and store input in an object *
# store credit hours in an object *
# write the equation for calculating the total marks 
# divide the total marks by 1800 and print the output
