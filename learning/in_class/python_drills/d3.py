# Step 1: Create a Dictionary
student_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# Step 2: Add and Update Entries
# Add a new student
# Update an existing student's grade
student_grades['foo'] = 100
student_grades['Alice'] = 0 

# Step 3: Calculate Average Grade
def calculate_average_grade(grades) -> float:
    tot = 0
    cnt = 0
    for k, v in student_grades.items():
        tot += v
        cnt += 1
        
    return tot/cnt

# Step 4: Find the Highest Grade
def find_highest_grade(grades) -> str:
    highest_grade = 0
    student = ""
    for k, v in student_grades.items():
        if v > highest_grade:
            highest_grade = v
            student = k
    return student 


if __name__ == '__main__':
    # Test the Functions
    # Adding a new student
    student_grades["Eve"] = 91
    # Updating an existing student's grade
    student_grades["Bob"] = 82
    
    # Calculating the average grade
    average_grade = calculate_average_grade(student_grades)
    print("Average grade:", average_grade)
    
    # Finding the highest grade
    top_student = find_highest_grade(student_grades)
    print("Top student:", top_student)
    
    # Validation using assert statements
    assert average_grade == 75.5, "Average grade calculation is incorrect"
    assert top_student == "foo", "Highest grade calculation is incorrect"
    
    print("All test cases passed")

