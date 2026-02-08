# Week 5 assignment: If Statement Homework

# 1. Created a single list with all the data from the assignment
raw_employee_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# 2. Programmatically sorted the information into a list of dictionary items, and did it for each employee
# to ensure each dictionary is in a database-like format.
# (Note: Having already read chapter 13, I am looking forward to Looping!!)

# Created list to hold all employee dictionaries
employees = []

# Employee 1: Jackie Grainger 
# Data found at indices: 0, 1, 2
if type(raw_employee_data[0]) is int and type(raw_employee_data[1]) is str and type(raw_employee_data[2]) is float:
    employee1 = {
        'employee_id': raw_employee_data[0],
        'name': raw_employee_data[1],
        'hourly_wage': raw_employee_data[2]
    }
    employees.append(employee1)

# Employee 2: Jignesh Thrakkar (ID 1122, wage 25.25)
# Data found at indices: 3, 4, 5
if type(raw_employee_data[3]) is int and type(raw_employee_data[4]) is str and type(raw_employee_data[5]) is float:
    employee2 = {
        'employee_id': raw_employee_data[3],
        'name': raw_employee_data[4],
        'hourly_wage': raw_employee_data[5]
    }
    employees.append(employee2)

# Employee 3: Dion Green 
# Data found at indices: 6, 7, 8 (9 is False - so I ignored it)
if type(raw_employee_data[6]) is int and type(raw_employee_data[7]) is str and type(raw_employee_data[8]) is float:
    employee3 = {
        'employee_id': raw_employee_data[6],
        'name': raw_employee_data[7],
        'hourly_wage': raw_employee_data[8]
    }
    employees.append(employee3)

# Employee 4: Jacob Gerber 
# Data found at indices: 11, 12, 10 
if type(raw_employee_data[11]) is int and type(raw_employee_data[12]) is str and type(raw_employee_data[10]) is float:
    employee4 = {
        'employee_id': raw_employee_data[11],
        'name': raw_employee_data[12],
        'hourly_wage': raw_employee_data[10]
    }
    employees.append(employee4)

# Employee 5: Sarah Sanderson 
# Data found at indices: 15, 13, 14
if type(raw_employee_data[15]) is int and type(raw_employee_data[13]) is str and type(raw_employee_data[14]) is float:
    employee5 = {
        'employee_id': raw_employee_data[15],
        'name': raw_employee_data[13],
        'hourly_wage': raw_employee_data[14]
    }
    employees.append(employee5)

# Employee 6: Brandon Heck 
# Data found at indices: 18, 17, 19
if type(raw_employee_data[18]) is int and type(raw_employee_data[17]) is str and type(raw_employee_data[19]) is float:
    employee6 = {
        'employee_id': raw_employee_data[18],
        'name': raw_employee_data[17],
        'hourly_wage': raw_employee_data[19]
    }
    employees.append(employee6)

# Employee 7: David Toma 
# Data found at indices: 21, 22, 23
if type(raw_employee_data[21]) is int and type(raw_employee_data[22]) is str and type(raw_employee_data[23]) is float:
    employee7 = {
        'employee_id': raw_employee_data[21],
        'name': raw_employee_data[22],
        'hourly_wage': raw_employee_data[23]
    }
    employees.append(employee7)

# Employee 8: Charles King 
# Data found at indices: 25, 26, 24
if type(raw_employee_data[25]) is int and type(raw_employee_data[26]) is str and type(raw_employee_data[24]) is float:
    employee8 = {
        'employee_id': raw_employee_data[25],
        'name': raw_employee_data[26],
        'hourly_wage': raw_employee_data[24]
    }
    employees.append(employee8)

# 3. No duplicates - As I did not add Jackie Grainger (indices 27-29) and David Toma (indices 30-32)

# 4. Multiplied each hourly wage by 1.3 and added total_hourly_rate key
employees[0]['total_hourly_rate'] = round(employees[0]['hourly_wage'] * 1.3, 2)
employees[1]['total_hourly_rate'] = round(employees[1]['hourly_wage'] * 1.3, 2)
employees[2]['total_hourly_rate'] = round(employees[2]['hourly_wage'] * 1.3, 2)
employees[3]['total_hourly_rate'] = round(employees[3]['hourly_wage'] * 1.3, 2)
employees[4]['total_hourly_rate'] = round(employees[4]['hourly_wage'] * 1.3, 2)
employees[5]['total_hourly_rate'] = round(employees[5]['hourly_wage'] * 1.3, 2)
employees[6]['total_hourly_rate'] = round(employees[6]['hourly_wage'] * 1.3, 2)
employees[7]['total_hourly_rate'] = round(employees[7]['hourly_wage'] * 1.3, 2)

# 5. Checked to see if anyone's total hourly rate is between 28.15 and 30.65
underpaid_salaries = [] # added info to list to hold underpaid salaries

if 28.15 <= employees[0]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[0])

if 28.15 <= employees[1]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[1])

if 28.15 <= employees[2]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[2])

if 28.15 <= employees[3]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[3])

if 28.15 <= employees[4]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[4])

if 28.15 <= employees[5]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[5])

if 28.15 <= employees[6]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[6])

if 28.15 <= employees[7]['total_hourly_rate'] <= 30.65:
    underpaid_salaries.append(employees[7])

# 6. Calculated raises based on hourly_wage ranges / Again wish I could use loops!
company_raises = [] # added info to list to hold company raises

# Employee 1 - Jackie Grainger
wage1 = employees[0]['hourly_wage']
if 22.00 <= wage1 < 24.00:
    raise_amount1 = round(wage1 * 0.05, 2)
elif 24.00 <= wage1 < 26.00:
    raise_amount1 = round(wage1 * 0.04, 2)
elif 26.00 <= wage1 < 28.00:
    raise_amount1 = round(wage1 * 0.03, 2)
else:
    raise_amount1 = round(wage1 * 0.02, 2)

raise1 = {
    'name': employees[0]['name'],
    'raise': raise_amount1
}
company_raises.append(raise1)

# Employee 2 - Jignesh Thrakkar
wage2 = employees[1]['hourly_wage']
if 22.00 <= wage2 < 24.00:
    raise_amount2 = round(wage2 * 0.05, 2)
elif 24.00 <= wage2 < 26.00:
    raise_amount2 = round(wage2 * 0.04, 2)
elif 26.00 <= wage2 < 28.00:
    raise_amount2 = round(wage2 * 0.03, 2)
else:
    raise_amount2 = round(wage2 * 0.02, 2)

raise2 = {
    'name': employees[1]['name'],
    'raise': raise_amount2
}
company_raises.append(raise2)

# Employee 3 - Dion Green
wage3 = employees[2]['hourly_wage']
if 22.00 <= wage3 < 24.00:
    raise_amount3 = round(wage3 * 0.05, 2)
elif 24.00 <= wage3 < 26.00:
    raise_amount3 = round(wage3 * 0.04, 2)
elif 26.00 <= wage3 < 28.00:
    raise_amount3 = round(wage3 * 0.03, 2)
else:
    raise_amount3 = round(wage3 * 0.02, 2)

raise3 = {
    'name': employees[2]['name'],
    'raise': raise_amount3
}
company_raises.append(raise3)

# Employee 4 - Jacob Gerber
wage4 = employees[3]['hourly_wage']
if 22.00 <= wage4 < 24.00:
    raise_amount4 = round(wage4 * 0.05, 2)
elif 24.00 <= wage4 < 26.00:
    raise_amount4 = round(wage4 * 0.04, 2)
elif 26.00 <= wage4 < 28.00:
    raise_amount4 = round(wage4 * 0.03, 2)
else:
    raise_amount4 = round(wage4 * 0.02, 2)

raise4 = {
    'name': employees[3]['name'],
    'raise': raise_amount4
}
company_raises.append(raise4)

# Employee 5 - Sarah Sanderson
wage5 = employees[4]['hourly_wage']
if 22.00 <= wage5 < 24.00:
    raise_amount5 = round(wage5 * 0.05, 2)
elif 24.00 <= wage5 < 26.00:
    raise_amount5 = round(wage5 * 0.04, 2)
elif 26.00 <= wage5 < 28.00:
    raise_amount5 = round(wage5 * 0.03, 2)
else:
    raise_amount5 = round(wage5 * 0.02, 2)

raise5 = {
    'name': employees[4]['name'],
    'raise': raise_amount5
}
company_raises.append(raise5)

# Employee 6 - Brandon Heck
wage6 = employees[5]['hourly_wage']
if 22.00 <= wage6 < 24.00:
    raise_amount6 = round(wage6 * 0.05, 2)
elif 24.00 <= wage6 < 26.00:
    raise_amount6 = round(wage6 * 0.04, 2)
elif 26.00 <= wage6 < 28.00:
    raise_amount6 = round(wage6 * 0.03, 2)
else:
    raise_amount6 = round(wage6 * 0.02, 2)

raise6 = {
    'name': employees[5]['name'],
    'raise': raise_amount6
}
company_raises.append(raise6)

# Employee 7 - David Toma
wage7 = employees[6]['hourly_wage']
if 22.00 <= wage7 < 24.00:
    raise_amount7 = round(wage7 * 0.05, 2)
elif 24.00 <= wage7 < 26.00:
    raise_amount7 = round(wage7 * 0.04, 2)
elif 26.00 <= wage7 < 28.00:
    raise_amount7 = round(wage7 * 0.03, 2)
else:
    raise_amount7 = round(wage7 * 0.02, 2)

raise7 = {
    'name': employees[6]['name'],
    'raise': raise_amount7
}
company_raises.append(raise7)

# Employee 8 - Charles King
wage8 = employees[7]['hourly_wage']
if 22.00 <= wage8 < 24.00:
    raise_amount8 = round(wage8 * 0.05, 2)
elif 24.00 <= wage8 < 26.00:
    raise_amount8 = round(wage8 * 0.04, 2)
elif 26.00 <= wage8 < 28.00:
    raise_amount8 = round(wage8 * 0.03, 2)
else:
    raise_amount8 = round(wage8 * 0.02, 2)

raise8 = {
    'name': employees[7]['name'],
    'raise': raise_amount8
}
company_raises.append(raise8)

# 7. Printed out the data in all three lists that were created above, and did it for each employee
print("EMPLOYEES LIST (with Total Hourly Rates)") #added list 1 of 3
print("=" * 20) # added a separator line to create heading
print(f"ID: {employees[0]['employee_id']}, Name: {employees[0]['name']}, "
      f"Hourly Wage: ${employees[0]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[0]['total_hourly_rate']:.2f}")
print(f"ID: {employees[1]['employee_id']}, Name: {employees[1]['name']}, "
      f"Hourly Wage: ${employees[1]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[1]['total_hourly_rate']:.2f}")
print(f"ID: {employees[2]['employee_id']}, Name: {employees[2]['name']}, "
      f"Hourly Wage: ${employees[2]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[2]['total_hourly_rate']:.2f}")
print(f"ID: {employees[3]['employee_id']}, Name: {employees[3]['name']}, "
      f"Hourly Wage: ${employees[3]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[3]['total_hourly_rate']:.2f}")
print(f"ID: {employees[4]['employee_id']}, Name: {employees[4]['name']}, "
      f"Hourly Wage: ${employees[4]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[4]['total_hourly_rate']:.2f}")
print(f"ID: {employees[5]['employee_id']}, Name: {employees[5]['name']}, "
      f"Hourly Wage: ${employees[5]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[5]['total_hourly_rate']:.2f}")
print(f"ID: {employees[6]['employee_id']}, Name: {employees[6]['name']}, "
      f"Hourly Wage: ${employees[6]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[6]['total_hourly_rate']:.2f}")
print(f"ID: {employees[7]['employee_id']}, Name: {employees[7]['name']}, "
      f"Hourly Wage: ${employees[7]['hourly_wage']:.2f}, "
      f"Total Hourly Rate: ${employees[7]['total_hourly_rate']:.2f}")

print("\n") # added a space to separate the lists
print("UNDERPAID SALARIES LIST (Total Hourly Rate between $28.15 and $30.65)") #added list 2 of 3
print("=" * 20)
if len(underpaid_salaries) > 0:
    index = 0
    if index < len(underpaid_salaries):
        print(f"ID: {underpaid_salaries[index]['employee_id']}, Name: {underpaid_salaries[index]['name']}, "
              f"Hourly Wage: ${underpaid_salaries[index]['hourly_wage']:.2f}, "
              f"Total Hourly Rate: ${underpaid_salaries[index]['total_hourly_rate']:.2f}")
        index = index + 1
    if index < len(underpaid_salaries):
        print(f"ID: {underpaid_salaries[index]['employee_id']}, Name: {underpaid_salaries[index]['name']}, "
              f"Hourly Wage: ${underpaid_salaries[index]['hourly_wage']:.2f}, "
              f"Total Hourly Rate: ${underpaid_salaries[index]['total_hourly_rate']:.2f}")
        index = index + 1
    if index < len(underpaid_salaries):
        print(f"ID: {underpaid_salaries[index]['employee_id']}, Name: {underpaid_salaries[index]['name']}, "
              f"Hourly Wage: ${underpaid_salaries[index]['hourly_wage']:.2f}, "
              f"Total Hourly Rate: ${underpaid_salaries[index]['total_hourly_rate']:.2f}")
        index = index + 1
    if index < len(underpaid_salaries):
        print(f"ID: {underpaid_salaries[index]['employee_id']}, Name: {underpaid_salaries[index]['name']}, "
              f"Hourly Wage: ${underpaid_salaries[index]['hourly_wage']:.2f}, "
              f"Total Hourly Rate: ${underpaid_salaries[index]['total_hourly_rate']:.2f}")
else:
    print("No employees found in this salary range.")

print("\n") # added a space to separate the lists
print("COMPANY RAISES LIST") #added list 3 of 3
print("=" * 20)
print(f"Name: {company_raises[0]['name']}, Raise: ${company_raises[0]['raise']:.2f}")
print(f"Name: {company_raises[1]['name']}, Raise: ${company_raises[1]['raise']:.2f}")
print(f"Name: {company_raises[2]['name']}, Raise: ${company_raises[2]['raise']:.2f}")
print(f"Name: {company_raises[3]['name']}, Raise: ${company_raises[3]['raise']:.2f}")
print(f"Name: {company_raises[4]['name']}, Raise: ${company_raises[4]['raise']:.2f}")
print(f"Name: {company_raises[5]['name']}, Raise: ${company_raises[5]['raise']:.2f}")
print(f"Name: {company_raises[6]['name']}, Raise: ${company_raises[6]['raise']:.2f}")
print(f"Name: {company_raises[7]['name']}, Raise: ${company_raises[7]['raise']:.2f}")