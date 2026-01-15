import math

#1 stored first name as variable; using lower case letters to declare
firstname = "sylvester"

#2 stored last name as variable; using upper case letters to declare
LASTNAME= "obafunwa"

#3 & 4: printing Hello, with full name in different formats (upper case and lower case), and added two lines))
print("Hello, " + "\n" + firstname.upper() + " " + LASTNAME.lower())

#5 variable that stores full name
name = "sylvester obafunwa"

#6 the code below seeks to extract "obafunwa" from the full name
print(name[10:18])

#7 the code below seeks to replace "obafunwa" with "Obafunwa, Walsh College Student"
name = name.replace("obafunwa", "Obafunwa, Walsh College Student")
print(name)

#8 printing a quote by Francis of Assisi but including double quotes at the beginning and end of the quote
string_quote = "\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible -Francis of Assisi \""
print(string_quote)

#9 storing two decimal variables; intentionally not using output as prefix (output_decimal1, etc.) to keep clean
decimal_1 = 1.987
decimal_2 = 2.026

#10 storing outputs of arithmetic operations on the decimal variables
addition = decimal_1 + decimal_2
subtraction = decimal_1 - decimal_2
multiplication = decimal_1 * decimal_2
division = decimal_1 / decimal_2

#11 printing the outputs of the arithmetic operations using different methods

# first method: concatenation
print("addition: " + str(decimal_1) + " + " + str(decimal_2) + " = " + str(addition))
# second method: string formatting expression (using % operator as seen on page 153 of textbook)
print("subtraction: %s - %s = %s" % (decimal_1, decimal_2, subtraction))
# third method: string formatting method (using .format() as seen on page 157 of textbook)
print("multiplication: {} * {} = {}".format(decimal_1, decimal_2, multiplication))
# fourth method: f-string (as seen on page 164 of textbook)
print(f"division: {decimal_1} / {decimal_2} = {division}")

#12 created square root variable of the multiplication result within 2 decimal places (this approach was explained on page 101 of textbook)| used math module
sq_root = round(math.sqrt(multiplication), 2)
# printing the square root result using concatenation
print("The Square Root of " + str(multiplication) + " equals " + str(sq_root))

#13 storing current month as string variable
current_month = "January"
#storing current date as number variable
current_date = 14

#14 printing output that combines both variables using an f-string, and tabbed over twice
print(f"\t\tToday is day {current_date} of {current_month}.")