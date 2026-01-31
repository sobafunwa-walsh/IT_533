# Week 4 Assignment, Expressions and Print Assignment

# Below I have created 5 different assignment statement forms, across 5 different scenarios/contexts that will
# apply to each form. Each scenario is explained in comments above the code block.
# ALso noted the ask that there should be at least one assignment, expression, and print statement for this activity. 
# I will be noting that at the end of the scenario title.
# Also I will be separating each printed scenario with 2 blank lines for clarity when printed.



# SCENARIO 1: Sequence Assignment (Assignment Statement) - Student Grade Quiz Results
## ============================================================================
# Context: IT 533 professor receives students quiz results and needs to separate
# them into individual variables for further analysis.

# student quiz results comes in as a sequence
student_quiz_results = ("Sylvester", 86, 91, 86)

# unpacking the sequence into individual variables
student_name, quiz1_score, quiz2_score, quiz3_score = student_quiz_results

# printing the unpacked variables
print("SCENARIO 1: Sequence Assignment (Assignment Statement) - Student Grade Quiz Results")
print("Student Name:", student_name)
print("Quiz 1 Score:", quiz1_score)
print("Quiz 2 Score:", quiz2_score)
print("Quiz 3 Score:", quiz3_score)



# SCENARIO 2: Augmented Assignment (Assignment Statement) - NFL player Score tracker
## ============================================================================
# Context: Seahawk NFL coach is looking to track Sam Darnold's scores in a game leading up to Superbowl 2026,
# where he earns points through various plays and actions. Augmented assignment is used to update his score.

# Initial score
sam_darnold_score = 0

# Simulating points earned through various plays
sam_darnold_score += 6  # Throws for a touchdown
sam_darnold_score += 4  # Successfully hands off for a touchdown
sam_darnold_score += 3  # Throws to receiver for a touchdown
sam_darnold_score += 2  # Completes a two-point conversion
sam_darnold_score += -3  # Throws an interception 

# Print the final score
print("\n\nSCENARIO 2: Augmented Assignment (Assignment Statement) - NFL player Score tracker")
print("Throws for a touchdown: 6 points")
print("Successfully hands off for a touchdown: 4 points")
print("Throws to receiver for a touchdown: 3 points")
print("Completes a two-point conversion: 2 points")
print("Throws an interception: -3 points")
print("Sam Darnold's Final Score:", sam_darnold_score)



# SCENARIO 3: Multiple-Target Assignment (Assignment Statement) - Nordstrom Sale Prices
## ============================================================================
# Context: Nordstrom is having a sale where all items in certain categories start at the same price.
# The store manager wants to assign the same sale price to multiple items in these categories. 
# Multiple-target assignment is used to set the sale price for all items in these categories.

# Initial sale price for shirts, pants, and shoes starting at $39.99
shirt_price = pants_price = shoes_price = 39.99

# Printing the sale prices for each item
print("\n\nSCENARIO 3: Multiple-Target Assignment (Assignment Statement) - Nordstrom Sale Prices")
print("Shirt Sale Price: $", shirt_price)
print("Pants Sale Price: $", pants_price)
print("Shoes Sale Price: $", shoes_price)



# SCENARIO 4: Expression Statement - Method Calls - Southwest Airlines Flight Status
## ============================================================================
# Context: I want to track the status of real-time flight updates from Southwest Airlines
# in my city, at Houston Hobby Airport. I am going to use the following script, using method calls, to fetch 
# and display the current status of flights.

# Simulated function to get flight status (in reality, this would call an API or database or site like flightaware.com)
def get_flight_status(flight_number): # used the def keyword as seen in Table 11-3 (Python Reserved Words)
        flight_statuses = {
        "SW123": "On Time",
        "SW456": "Delayed",
        "SW789": "Cancelled"
    }
        return flight_statuses.get(flight_number, "Flight not found") # used return as seen in Table 11-3 (Python Reserved Words)

# Fetching and printing flight status for a specific flight
flight_number = "SW123"
print("\n\nSCENARIO 4: Expression Statement - Method Calls - Southwest Airlines Flight Status")
print("Flight Number:", flight_number)
print("Flight Status:", get_flight_status(flight_number))



# SCENARIO 5: Print Statement - Valentine's Day Menu for my Wife
## ============================================================================ 
# Context: I am planning a special Valentine's Day dinner for my wife and want to create a 
# Nigerian themed menu that I can PRINT and present to her on the day. In planning the menu, 
# I plan to capture how long each dish will take to make.

# V-Day menu with prep time
valentines_day_menu = [
        ("Suya Skewers with Spicy Peanut Sauce", 20),
        ("Puff-Puff Bites with Honey Drizzle", 15),
        ("Jollof Rice with Grilled Chicken", 45),
        ("Egusi Soup with Pounded Yam", 20),
        ("Chin Chin with Chocolate Dip", 25),
        ("Nigerian Coconut Cake", 30),
        ("Hibiscus Tea", 10),
        ("Palm Wine", 5)
        ]


# Processing each menu item
print("\n\nSCENARIO 5: Print Statement - Valentine's Day Menu for my Wife")
for menu_item_name, menu_item_prep_time in valentines_day_menu:
        print(menu_item_name, f"{menu_item_prep_time} mins", sep=" - ", end="\n")
