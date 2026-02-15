Student_name = input("Student name: ")
Marks_maths = int(input("Marks in Maths: "))
Marks_science = int(input("Marks in Science: "))
Marks_english = int(input("Marks in English: "))
Result = ""
Grade = ""

Total_marks = Marks_maths + Marks_science + Marks_english
Average_marks = Total_marks / 3

if(Marks_maths < 35 or Marks_science < 35 or Marks_english < 35):
    Result = "Fail"
else:    
    Result = "Pass"

if(Average_marks >= 75):
    Grade = "A"
elif(Average_marks >= 60 and Average_marks < 75):
    Grade = "B"
elif(Average_marks >= 40 and Average_marks < 60):
    Grade = "C"

print(f"Student name: {Student_name}")
print(f"Total Marks: {Total_marks}")
print(f"Average Marks: {Average_marks}")
print(f"Result: {Result}")  
print(f"Grade: {Grade}")


