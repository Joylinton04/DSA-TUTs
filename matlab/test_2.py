number_of_students = {
    'Monday': 500,
    'Tuesday': 510,
    'Wednesday': 480,
    'Thursday': 500,
    'Friday': 570,
}

amount_for_each_day = {
    'Monday': 6.2,
    'Tuesday': 8.2,
    'Wednesday': 7.2,
    'Thursday': 6.2,
    'Friday': 7.2,
}

discount = (5.5/100)
total_sales = 0
for day in number_of_students:
    daily_cost = amount_for_each_day[day]
    discount_off = (daily_cost - (discount*daily_cost))
    total_amount_collected = discount_off * number_of_students[day]
    total_sales += total_amount_collected
    print(f'{day}:   {total_amount_collected:.2f}')
    
print('Total sales(GHC): ',total_sales)