"""
# task 1 - Create and Write Student Data (Basic)

Newfile = open("student.txt", "x")
with open("student.txt", "a") as file:
    file.write("Alice,85\n")
    file.write("Bob,92\n")
    file.write("Charlie,78\n")
    file.write("Diana,95\n")
file.close()


# task 2 - Read and Display Data (Basic)

readfile = open("student.txt", "r")
for line in readfile:
    name, grade = line.strip().split(",")
    print(f"Student: {name}, Grade: {grade}")
readfile.close()
"""

# task 3 - Calculate Average Grade (Intermediate)

with open("student.txt", "a") as file:
    file.write("Eve,88\n")

Newlogfile = open("activity.log", "x")
with open("activity.log", "a") as log_file:
    log_file.write("Added new student: Eve\n")

log_file.close()
file.close()