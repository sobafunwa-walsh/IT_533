# Week 6 - Loops, User Input, and Comprehension Assignment


# Bad characters lists for validation
bad_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
bad_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

# List to store all employee dictionaries
employee_list = []

# Variable to control whether to keep adding employees
keep_adding = True

# Main loop to add employee details until otherwise stated
while keep_adding:

    print("\n Enter Employee Information:") # Just adding a line to make it look cleaner

    # 1. EMPLOYEE ID INPUT AND VALIDATION / Id is required and will need to be 7 or less digits long
    # ===========================
    employee_id_ok = False

    while not employee_id_ok:
        employee_id  = input("Please enter Employee ID (required, max 7 digits): ") # Getting the employee ID input
        if employee_id:
            try:
                int(employee_id)  # Checking if it's a number
                if len(employee_id) <=7: # Checking if it's 7 digits or less
                    print("Employee ID accepted: " + employee_id)
                    employee_id_ok = True
                else:
                    print("Employee ID must be 7 digits or less.") 
            except:
                print("Invalid Employee ID. Please enter a numeric value.") # Catching non-numeric input
        else:
            print("You did not enter an Employee ID, This field is required.") # Catching an empty input


     # 2. EMPLOYEE NAME VALIDATION / Name is required, and must be primarily letters, with spaces, the ' and - characters allowed
    # ===========================
    employee_name_ok = False

    while not employee_name_ok:
        employee_name = input("Please enter Employee Name (required): ")  # Getting the employee name input
        if employee_name:
            bad_characters_found = False
            # check each character, as only letters, spaces, apostrophes, and hyphens allowed
            for character in employee_name:
                if not (character.isalpha() or character == " " or character == "'" or character == "-"): # Checking if the character is not a letter, space, apostrophe, or hyphen
                    print("Employee Name can only contain letters, spaces, apostrophes, and hyphens.") # This message will print if bad character is found
                    bad_characters_found = True
                    break # If bad character is found, no need to check rest of the characters, so we can break out of the loop. Seen on page 315 of the text book
                
            if not bad_characters_found: # If no bad characters are found, then the name is accepted
                    print("Employee Name accepted: " + employee_name)
                    employee_name_ok = True
        else:
            print("You did not enter an Employee Name. THis field is required.") # Catching an empty input
    

    # 3. EMPLOYEE EMAIL ADDRESS VALIDATION / Email required, cannot contain specific bad characters
    # ===========================
    employee_email_ok = False

    while not employee_email_ok:
        employee_email = input("Please enter Employee Email (required): ") # Getting the employee email input
        if employee_email:
            bad_characters_found = False # variable to track if bad characters are found
            for character in bad_email_characters:
                if character in employee_email:
                    # This message will print and append the list of bad characters found in the email; 
                    # the join function is used to append the list of bad characters to the text
                    # I found this on page 353 of the textbook (sixth edition)) 
                    print("Employee Email cannot contain the following characters: " + ", ".join(bad_email_characters)) 
                    bad_characters_found = True
                    break # If bad character is found, no need to check rest of the characters; loop can be broken
                    
            if not bad_characters_found:
                print("Employee Email accepted: " + employee_email) # If no bad characters are found, then the email is accepted
                employee_email_ok = True
        else:
            print("You did not enter an Employee Email. This field is required.") # Catching an empty input

    
    # 4. EMPLOYEE ADDRESS VALIDATION / Address is optional; cannot contain specific bad characters
    # ===========================
    employee_address_ok = False
    
    while not employee_address_ok:
        # Getting the employee address input, this field is optional so the user can press enter to skip
        employee_address = input("Please enter Employee Address (optional, press Enter to skip): ") 
        if employee_address:
            bad_characters_found = False
            # checking each character, as the address cannot contain specific bad characters
            for character in bad_address_characters: 
                if character in employee_address:
                    # This message will print and append the list of bad characters found in the address
                    print("Employee Address cannot contain the following characters: " + ", ".join(bad_address_characters)) # added break below, as I kept seeing same error multiple times when I was testing
                    bad_characters_found = True
                    break # If bad character is found, no need to check rest of the characters; loop can be broken 

            if not bad_characters_found:
                print("Employee Address accepted: " + employee_address) # If no bad characters are found, then the address is accepted
                employee_address_ok = True
        else:
           print("No address provided.")  # Address is optional, so empty is okay
           employee_address_ok = True  # Set to true to exit the loop if no address is provided
    

     # 5. EMPLOYEE SALARY VALIDATION / Salary  is required, but must be a floating number between 18 and 27
    # ===========================
    employee_salary_ok = False
    
    while not employee_salary_ok:
        employee_salary = input("Please enter Employee Hourly Salary (required, between 18.00 and 27.00): ") # Getting the employee salary input
        if employee_salary:
            try:
                salary_value = float(employee_salary) # Checking if the input can be converted to a float, which is necessary for salary
                if salary_value >= 18 and salary_value <= 27: # Checking if the salary is between 18 and 27
                    print("Employee Salary accepted: $" + str(salary_value)) # If the salary is valid, then it is accepted
                    employee_salary_ok = True
                else:
                    print("Employee Salary must be between 18.00 and 27.00.") # If salary is not within the stated range above, message will print
            except:
                print("Invalid salary. Please enter a numeric value.") # If the input cannot be converted to a float, message will print
        else:
            print("You did not enter an Employee Salary. This field is required.") # Catching an empty input
    

    # CREATING EMPLOYEE DICTIONARY and LIST APPEND 
    # Once all the employee details are collected and validated, will create a dictionary for the employee 
    # and append it to the employee list
    # ===========================
    employee_dict = {
        "id": employee_id,
        "name": employee_name,
        "email": employee_email,
        "address": employee_address,
        "salary": salary_value
    }
    
    employee_list.append(employee_dict)
    print("\nEmployee added successfully!")

    # NEED TO ASK IF USER WANTS TO ADD MORE EMPLOYEES
    # Following logic will ask the user if they want to add another employee, and w
    # And will only accept "yes" or "no" as valid responses
    # ===========================
    
    # Trying to get user input and convert it to lowercase in one step
    add_more = input("\nWould you like to add another employee? (yes/no): ") # getting user input and then adding their response to the add_more variable
    add_more = add_more.lower() # Converting the input to lowercase to make it case-insensitive
    
    if add_more == "no" or add_more == "n":
        keep_adding = False


# DATA MODIFICATIONS USING COMPREHENSIONS 
# Once user is done adding employees, comprehensions will be used to append "IT Department"
# Will also add salary increase info (^30% to original salary)
# ===========================

print("\n PROCESSING EMPLOYEE DATA...") # Just adding a line to make it look cleaner

# Comprehension to add "IT Department" to each employee dictionary and 
# to calculate the new salary with a 30% increase, and then create a new list of employee dictionaries with the updated information
employee_list = [{"id": emp["id"], "name": emp["name"] + " - IT Department", "email": emp["email"], # add IT dempartment to the name field
                  "address": emp["address"], "salary": emp["salary"] * 1.30} for emp in employee_list] # multiplying the original salary by 1.30 to calculate the new salary with a 30% increase


# PRINTING FINAL UPDATED EMPLOYEE LIST 
# ===========================

print("\n FINAL EMPLOYEE LIST:") # Just making final output look cleaner

for employee in employee_list: # Looping through the employee list and printing the details of each employee in a readable format
    print("Employee ID: " + employee["id"])
    print("Employee Name: " + employee["name"])
    print("Employee Email: " + employee["email"])
    if employee["address"]:
        print("Employee Address: " + employee["address"]) # If an address was provided, it will print the address; if the address is empty, it will skip
    else:
        print("Employee Address: Not provided") # If no address was provided, this message will print instead
    print("Total Hourly Salary: $" + str(round(employee["salary"], 2))) # Rounding the salary to 2 decimal places for better readability
    print("\n") # Just adding a line break between employees for better readability
   
print("End of Employee List.")