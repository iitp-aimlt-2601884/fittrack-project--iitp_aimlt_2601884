# STUDENT GRADE BOOK
# Using Lists, Dictionaries, Tuples, and Sets

# List - student names (ordered, mutable)
students = ["Raj", "Priya", "Amit", "Sneha", "Karan"]

# Tuple - subject names (immutable, won't change)
subjects = ("Math", "Science", "English")

# Dictionary - store marks (key-value pairs for easy access)
marks = {
    "Raj": {"Math": 85, "Science": 78, "English": 90},
    "Priya": {"Math": 92, "Science": 88, "English": 85},
    "Amit": {"Math": 70, "Science": 75, "English": 68},
    "Sneha": {"Math": 95, "Science": 90, "English": 92},
    "Karan": {"Math": 80, "Science": 82, "English": 78}
}

# Set - unique grades (no duplicates)
grades = set()

# Display all students
print(f"All Students: {students}")

# Slicing - first 3 students
print(f"First 3 Students: {students[0:3]}\n")

# Calculate averages and assign grades
top_student = ""
highest_avg = 0

for student in students:
    # Get total marks
    total = marks[student]["Math"] + marks[student]["Science"] + marks[student]["English"]
    
    # Calculate average
    average = total / 3
    
    # Assign grade
    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "C"
    
    # Add to set
    grades.add(grade)
    
    # Print student info
    print(f"{student} - Average: {average:.2f} - Grade: {grade}")
    
    # Track top student
    if average > highest_avg:
        highest_avg = average
        top_student = student

# Display results
print(f"\nTop Student: {top_student}")
print(f"Unique Grades: {grades}")
