# Week 7-8 - Functions Assignment

import json  # Importing json module to handle writing employee data to a JSON file

# Bad characters lists for validation
# ===========================
bad_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
bad_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]


# ===========================
# Function: get_employee_id - will prompt the user for an Employee ID, validate it, and return it.
# ===========================
def get_employee_id(): # Prompt for and validate Employee ID
    while True:  # Keep looping until a valid ID is entered
        employee_id = input("Please enter Employee ID (required, max 7 digits): ")
        if employee_id:
            try:
                int(employee_id)  # Checking if the input is numeric
                if len(employee_id) <= 7:
                    print("Employee ID accepted: " + employee_id)
                    return employee_id  # Return valid ID back to the caller (Chapter 16)
                else:
                    print("Employee ID must be 7 digits or less.")
            except:
                print("Invalid Employee ID. Please enter a numeric value.")
        else:
            print("You did not enter an Employee ID. This field is required.")


# ===========================
# Function: get_employee_name - will prompt the user for an Employee Name, validate allowed characters, and return it.
# ===========================
def get_employee_name(): # Prompt for and validate Employee Name
    while True:
        employee_name = input("Please enter Employee Name (required): ")
        if employee_name:
            bad_characters_found = False
            for character in employee_name:
                # Only letters, spaces, apostrophes, and hyphens are allowed
                if not (character.isalpha() or character == " " or character == "'" or character == "-"):
                    print("Employee Name can only contain letters, spaces, apostrophes, and hyphens.")
                    bad_characters_found = True
                    break  # Stop checking once a bad character is found (page 315 of textbook)
            if not bad_characters_found:
                print("Employee Name accepted: " + employee_name)
                return employee_name  # Return valid name back to the caller
        else:
            print("You did not enter an Employee Name. This field is required.")


# ===========================
# Function: get_employee_email - will prompt the user for an Employee Email, validate against bad_email characters list, and return it.
# ===========================
def get_employee_email(): # Prompt for and validate Employee Email
    while True:
        employee_email = input("Please enter Employee Email (required): ")
        if employee_email:
            bad_characters_found = False
            for character in bad_email_characters:
                if character in employee_email:
                    # join() used to display bad characters in a readable format (page 353 of textbook)
                    print("Employee Email cannot contain the following characters: " + ", ".join(bad_email_characters))
                    bad_characters_found = True
                    break
            if not bad_characters_found:
                print("Employee Email accepted: " + employee_email)
                return employee_email  # Return valid email back to the caller
        else:
            print("You did not enter an Employee Email. This field is required.")


# ===========================
# Function: get_employee_address - will prompt the user for an optional Employee Address, validate it against the bad_address_characters list, and return it.
# ===========================
def get_employee_address(): # Prompt for and validate Employee Address
    while True:
        employee_address = input("Please enter Employee Address (optional, press Enter to skip): ")
        if employee_address:
            bad_characters_found = False
            for character in bad_address_characters:
                if character in employee_address:
                    print("Employee Address cannot contain the following characters: " + ", ".join(bad_address_characters))
                    bad_characters_found = True
                    break
            if not bad_characters_found:
                print("Employee Address accepted: " + employee_address)
                return employee_address  # Return valid address
        else:
            print("No address provided.")
            return ""  # Address is optional; return empty string if skipped


# ===========================
# Function: get_employee_salary - will prompt the user for an Employee Salary, validate it is a float between 18.00 and 27.00, and return it.
# ===========================
def get_employee_salary():
    while True:
        employee_salary = input("Please enter Employee Hourly Salary (required, between 18.00 and 27.00): ")
        if employee_salary:
            try:
                salary_value = float(employee_salary)  # Convert to float for decimal salary support
                if 18 <= salary_value <= 27:
                    print("Employee Salary accepted: $" + str(salary_value))
                    return salary_value  # Return the validated float salary
                else:
                    print("Employee Salary must be between 18.00 and 27.00.")
            except:
                print("Invalid salary. Please enter a numeric value.")
        else:
            print("You did not enter an Employee Salary. This field is required.")


# ===========================
# Function: collect_employee -  will accept the employee list as an argument, collect and validates one employee's
#          details by calling each field function. Then itbuilds the employee dictionary,
#          then appends it to the passed-in list, and returns the updated list.
# This mirrors the practice that we did in the lecture video, where the list is passed in, modified, and returned.
# ===========================
def collect_employee(employee_list):
    print("\n Enter Employee Information:")

    # Call each field function — each one handles its own validation loop
    # and returns only when a valid value has been entered
    employee_id      = get_employee_id()
    employee_name    = get_employee_name()
    employee_email   = get_employee_email()
    employee_address = get_employee_address()
    employee_salary  = get_employee_salary()

    # Build the employee dictionary from the validated field values
    employee_dict = {
        "id":      employee_id,
        "name":    employee_name,
        "email":   employee_email,
        "address": employee_address,
        "salary":  employee_salary
    }

    # Appends the new employee dictionary to the list that was passed in
    employee_list.append(employee_dict)
    print("\nEmployee added successfully!")

    return employee_list  # Return the updated list back to the caller


# ===========================
# Function: apply_department_and_raise - changed the comprehension logic from Week 6 into a reusable function.
# ===========================
def apply_department_and_raise(employee_list):
    # List comprehension builds a brand-new list with the updated fields
    # Each employee dictionary is rebuilt with the modified name and salary
    updated_list = [
        {
            "id":      emp["id"],
            "name":    emp["name"] + " - IT Department",  # Appending department label
            "email":   emp["email"],
            "address": emp["address"],
            "salary":  emp["salary"] * 1.30               # Applying 30% raise
        }
        for emp in employee_list  # Iterating over each employee in the original list
    ]
    return updated_list  # Return the newly processed list


# ===========================
# Function: write_employees_to_json - takes the final employee list and writes it to a JSON file.
# ===========================
def write_employees_to_json(employee_list, filename="employees.json"):
    output_file = open(filename, "w")           # Opening the file for writing
    json.dump(employee_list, output_file, indent=4)  # Writing the list as formatted JSON
    output_file.close()                         # Closing the file
    print("\nEmployee data successfully written to: " + filename)


# ===========================
# Function: print_employee_list 
# ===========================
def print_employee_list(employee_list):
    print("\n FINAL EMPLOYEE LIST:")
    for employee in employee_list:
        print("Employee ID: " + employee["id"])
        print("Employee Name: " + employee["name"])
        print("Employee Email: " + employee["email"])
        if employee["address"]:
            print("Employee Address: " + employee["address"])
        else:
            print("Employee Address: Not provided")
        print("Total Hourly Salary: $" + str(round(employee["salary"], 2)))
        print("\n")
    print("End of Employee List.")


# ===========================
# Main logic - calls the functions above in sequence to collect, process, display, and save employee data.
# ===========================

employee_list = []   # List to store all employee dictionaries collected during the session
keep_adding = True   # Control variable for the main loop

# Main loop: keep collecting employees until the user says no
while keep_adding:

    # Call collect_employee() to gather and validate one full set of employee data, then append the returned dictionary to our master list
    employee_list = collect_employee(employee_list)

    # Ask user if they want to add another employee
    add_more = input("\nWould you like to add another employee? (yes/no): ").lower()
    if add_more == "no" or add_more == "n":
        keep_adding = False  # Exit the loop

print("\n PROCESSING EMPLOYEE DATA...") # Once data collection is complete, processing the list using the comprehension function
employee_list = apply_department_and_raise(employee_list)

print_employee_list(employee_list) # Displaying the final processed employee list
write_employees_to_json(employee_list) # Writing the final employee list to a JSON file