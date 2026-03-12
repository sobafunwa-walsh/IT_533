# Weeks 9-10 Assignment: Classes and OOP (Chapters 26-29)

import re  # Used for pattern-based input validation


# ============================================================
# VALIDATOR CLASS - contains all validation methods as class-level methods
# ============================================================

class Validator:
    """class containing validation methods for all input fields."""

    def validate_name(self, name):
        """Validates that a name: Is not empty / Is primarily letters / Does not contain bad characters"""

        # Forbidden characters as specified in the assignment / also using "forbidden" instead of "bad" to be more descriptive
        forbidden = set('!"@#$%^&*()_=+,<>/?;:[]{}\\') #using 'set' for faster lookup 

        # Check for forbidden characters
        for char in name:
            if char in forbidden:
                return False

        # Must have at least some letter content and can be upper or lower case (not just spaces/symbols)
        if not any(c.isalpha() for c in name):
            return False

        # Must not be blank
        if not name.strip():
            return False

        return True

    def validate_email(self, email):
        """Validates that an email address: Is not empty / Does not contain forbidden special characters"""

        # Forbidden characters as specified in the assignment
        forbidden = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')

        # Check for forbidden characters
        for char in email:
            if char in forbidden:
                return False

            # Must not be blank
        if not email.strip():
            return False

        return True

    def validate_student_id(self, student_id):
        """Validates that a Student ID: Is a number (digits only) / Is 7 or fewer digits long"""

        # Must be all digits
        if not student_id.isdigit():
            return False

        # Must be 7 or fewer digits
        if len(student_id) > 7:
            return False

        # Must not be empty
        if not student_id.strip():
            return False

        return True

    def validate_instructor_id(self, instructor_id):
        """Validates that an Instructor ID: Is a number (digits only) / Is 5 or fewer digits long"""

        # Must be all digits
        if not instructor_id.isdigit():
            return False

        # Must be 5 or fewer digits
        if len(instructor_id) > 5:
            return False

        # Must not be empty
        if not instructor_id.strip():
            return False

        return True

    def validate_required(self, value):
        """Validate that a required field is not blank."""

        return bool(value.strip()) # Returns True if there is non-whitespace content, False if blank or only whitespace


# ============================================================
# PERSON CLASS: Holds attributes and behavior common to both Students and Instructors
# Will be the superclass that Student and Instructor inherit from
# ============================================================

class Person:
    """Person class representing anyone in the college system; Stores shared attributes like name and email."""

    def __init__(self, name, email):
        """Initialize shared attributes for any person."""
        self.name = name
        self.email = email

    def displayInformation(self):
        """Display the shared information for this person."""
        # This method is meant to be augmented (extended) by subclasses
        print(f"  Name:  {self.name}")
        print(f"  Email: {self.email}")


# ============================================================
# SUB-Person CLASS: Student - Inherits from Person and adds student-specific attributes.
# ============================================================

class Student(Person):
    """Represents a student in the college system; Inherits name and email from Person
    Adds: student_id and program_of_study."""

    def __init__(self, name, email, student_id, program_of_study):
        """Initialize a Student instance. Calls the parent __init__ to set shared fields,
        then sets student-specific fields."""
        # Augment the parent constructor using super()
        super().__init__(name, email)
        self.student_id = student_id
        self.program_of_study = program_of_study

    def displayInformation(self):
        """Display all information for this student. Augments the parent displayInformation by first calling it,
        then adding student-specific fields below."""
        print("\n  [STUDENT RECORD]")
        # Call the parent method to display shared fields (augmentation)
        super().displayInformation()
        # Now display student-specific fields
        print(f"  Student ID:        {self.student_id}")
        print(f"  Program of Study:  {self.program_of_study}")


# ============================================================
# SUB-Person CLASS: Instructor - Inherits from Person and adds instructor-specific attributes.
# ============================================================

class Instructor(Person):
    """Represents an instructor in the college system. Inherits name and email from Person.
    Adds: instructor_id, last_institution, and highest_degree."""

    def __init__(self, name, email, instructor_id, last_institution, highest_degree):
        """Initialize an Instructor instance. Calls the parent __init__ to set shared fields,
        then sets instructor-specific fields."""
        # Augment the parent constructor using super()
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.last_institution = last_institution
        self.highest_degree = highest_degree

    def displayInformation(self):
        """Display all information for this instructor. Augments the parent displayInformation by first calling it,
        then adding instructor-specific fields below."""
        print("\n  [INSTRUCTOR RECORD]")
        # Call the parent method to display shared fields (augmentation)
        super().displayInformation()
        # Now display instructor-specific fields
        print(f"  Instructor ID:      {self.instructor_id}")
        print(f"  Last Institution:   {self.last_institution}")
        print(f"  Highest Degree:     {self.highest_degree}")


# ============================================================
# INPUT HELPER FUNCTIONS: These functions use the Validator class to gather and re-prompt
# for data until the user provides valid input.
# ============================================================

def get_valid_input(prompt, validation_method, error_message):
    """Repeatedly prompt the user until valid input is provided."""

    while True:
        value = input(prompt).strip()
        if validation_method(value):
            return value
        else:
            print(f"Invalid input: {error_message} Please try again.")


def collect_student(validator):
    """Collect and validate all information for a new Student. Uses the Validator instance to check each field."""
    
    print("\n  --- Entering Student Information ---")

    # Collect and validate name
    name = get_valid_input(
        "  Enter student's full name: ",
        validator.validate_name,
        "Name cannot be blank and must not contain: ! \" @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \\"
    )

    # Collect and validate email
    email = get_valid_input(
        "  Enter student's email address: ",
        validator.validate_email,
        "Email must not contain: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\"
    )

    # Collect and validate student ID (7 or fewer digits)
    student_id = get_valid_input(
        "  Enter student ID (numbers only, up to 7 digits): ",
        validator.validate_student_id,
        "Student ID must be numeric and 7 digits or fewer."
    )

    # Collect and validate program of study (required, non-empty)
    program_of_study = get_valid_input(
        "  Enter program of study: ",
        validator.validate_required,
        "Program of study cannot be blank."
    )

    # Build and return the Student object
    return Student(name, email, student_id, program_of_study)


def collect_instructor(validator):
    """Collect and validate all information for a new Instructor. Uses the Validator instance to check each field."""

    print("\n  --- Entering Instructor Information ---")

    # Collect and validate name
    name = get_valid_input(
        "  Enter instructor's full name: ",
        validator.validate_name,
        "Name cannot be blank and must not contain: ! \" @ # $ % ^ & * ( ) _ = + , < > / ? ; : [ ] { } \\"
    )

    # Collect and validate email
    email = get_valid_input(
        "  Enter instructor's email address: ",
        validator.validate_email,
        "Email must not contain: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\"
    )

    # Collect and validate instructor ID (5 or fewer digits)
    instructor_id = get_valid_input(
        "  Enter instructor ID (numbers only, up to 5 digits): ",
        validator.validate_instructor_id,
        "Instructor ID must be numeric and 5 digits or fewer."
    )

    # Collect and validate last institution (required, non-empty)
    last_institution = get_valid_input(
        "  Enter name of last institution graduated from: ",
        validator.validate_required,
        "Institution name cannot be blank." 
    )

    # Collect and validate highest degree (required, non-empty)
    highest_degree = get_valid_input(
        "  Enter highest degree earned: ",
        validator.validate_required,
        "Highest degree cannot be blank."
    )

    # Build and return the Instructor object
    return Instructor(name, email, instructor_id, last_institution, highest_degree)


# ============================================================
# Main logic - collect records and display them
# ============================================================

def main():
    """Main function that drives the college records collection program."""

    print("=" * 20)
    print("   Welcome to the College Records System")
    print("=" * 20)

    # The list that stores all collected Person objects (Students and Instructors)
    college_records = []

    # Creates a single Validator instance to be reused throughout
    validator = Validator()

    # Keeps collecting records until the user says they are done
    while True:

        # Asks what type of individual is being entered
        print("\nWhat type of individual are you entering?")
        print("  1 - Student")
        print("  2 - Instructor")
        print("  3 - Done (stop entering records)")

        choice = input("Enter your choice (1, 2, or 3): ").strip() # Stripping whitespace for cleaner input and to make it easier for users

        if choice == '1':
            # Collect student data, build object, add to list
            student = collect_student(validator)
            college_records.append(student)
            print(f"\n  ✔ Student record for '{student.name}' added successfully.")

        elif choice == '2':
            # Collect instructor data, build object, add to list
            instructor = collect_instructor(validator)
            college_records.append(instructor)
            print(f"\n  ✔ Instructor record for '{instructor.name}' added successfully.")

        elif choice == '3':
            # User is done entering records
            print("\nNo more records to enter.")
            break

        else:
            # Invalid menu choice — re-prompt
            print("  *** Invalid choice. Please enter 1, 2, or 3.")

    # --------------------------------------------------------
    # Print all collected records using each object's displayInformation method as requested in the assignment. 
    # --------------------------------------------------------

    print("\n" + "=" * 20)
    print("       ALL COLLEGE RECORDS")
    print("=" * 20)

    if not college_records:
        print("  No records were entered.")
    else:
        for index, record in enumerate(college_records, start=1):
            print(f"\n  Record #{index}:")
            record.displayInformation()  # Polymorphic call

    print("\n" + "=" * 50)
    print("  End of College Records.")
    print("=" * 50)


# Run the program
main()