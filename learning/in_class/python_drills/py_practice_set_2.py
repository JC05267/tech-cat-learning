from typing import List
import pandas as pd


def list_to_dict(student_list: List[dict[str, int]]):
    result = {}
    for d in student_list:
        result[d["name"]] = d["score"]
    return result

def grade_converter(grade: int) -> str:
    match grade:
        case grade if grade <= 100 and grade >= 90:
            return 'A'
        case grade if grade <= 89 and grade >= 80:
            return 'B'
        case grade if grade <= 79 and grade >= 70:
            return 'C'
        case grade if grade <= 69 and grade >= 60:
            return 'D'
        case grade if grade <= 59 and grade >= 0:
            return 'F'
        case _:
            return 'Invalid grade'

def add_grades(input_file: str, output_file: str):
    df = pd.read_csv(input_file) 
    df['grade'] = [grade_converter(x) for x in df['score']]
    df.to_csv(output_file)

def count_even_odd(numbers: List[int]) -> dict[str, int]:
    evenCnt = 0
    oddCnt = 0
    for x in numbers:
        if x % 2 == 0:
            evenCnt += 1 
        else: 
            oddCnt += 1
    return {
        'even': evenCnt,
        'odd': oddCnt
    }

def calculate_statistics():
    input_str = input("Enter a series of numbers separated by spaces: ")
    lst = input_str.split(" ")
    lstInt = [int(x) for x in lst]

    s = sum(lstInt)
    avg = s/len(lstInt)
    m = min(lstInt)
    ma = max(lstInt)

    return {
        'sum': s,
        'average': avg,
        'max': ma,
        'min': m
    }


# Example asserts for testing the function (you can simulate inputs when testing)
def test_calculate_statistics():
    import builtins
    input_values = ["1 2 3 4 5"]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    builtins.input = mock_input
    result = calculate_statistics()

    # Asserts to ensure the function is working correctly
    assert result == {'sum': 15, 'average': 3.0, 'min': 1, 'max': 5}, "Test Case 1 Failed"
    print("All test cases passed!")


if __name__ == '__main__':
    # Example input
    students = [
        {'name': 'Alice', 'score': 90},
        {'name': 'Bob', 'score': 85},
        {'name': 'Charlie', 'score': 92}
    ]
    
    # Call the function with example input
    output = list_to_dict(students)
    # Asserts to ensure the function is working correctly
    assert output == {'Alice': 90, 'Bob': 85, 'Charlie': 92}, "Test Case 1 Failed"
    
    print("All test cases passed!")
    # Example usage
    input_file = 'students_scores.csv'
    output_file = 'students_with_grades.csv'
    
    # Create a sample input file for testing purposes
    sample_data = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'score': [95, 82, 78, 61]
    })
    sample_data.to_csv(input_file, index=False)
    
    # Call the function with example input
    add_grades(input_file, output_file)
    
    # Asserts to ensure the function is working correctly
    output_data = pd.read_csv(output_file)
    assert 'grade' in output_data.columns, "Grade column is missing"
    assert output_data.loc[output_data['name'] == 'Alice', 'grade'].values[0] == 'A', "Alice's grade is incorrect"
    assert output_data.loc[output_data['name'] == 'Bob', 'grade'].values[0] == 'B', "Bob's grade is incorrect"
    assert output_data.loc[output_data['name'] == 'Charlie', 'grade'].values[0] == 'C', "Charlie's grade is incorrect"
    assert output_data.loc[output_data['name'] == 'David', 'grade'].values[0] == 'D', "David's grade is incorrect"
    
    print("All test cases passed!")

    # Example input
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Call the function with example input
    output = count_even_odd(numbers)
    
    # Asserts to ensure the function is working correctly
    assert output == {'even': 5, 'odd': 5}, "Test Case 1 Failed"
    
    print("All test cases passed!")

    # Call the function and print the result
    statistics = calculate_statistics()
    print(statistics)
    # Run the test
    test_calculate_statistics()
