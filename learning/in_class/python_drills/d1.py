def is_even(num: int) -> bool:
    return num % 2 == 0

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
        

if __name__ == '__main__':
    print("Testing is_even function")
    assert is_even(10) == True, "Test case 1 failed"
    assert is_even(7) == False, "Test case 2 failed"
    assert is_even(0) == True, "Test case 3 failed"
    assert is_even(-2) == True, "Test case 4 failed"
    print("All is_even test cases passed")
    
    # Testing grade_converter function
    print("Testing grade_converter function")
    assert grade_converter(95) == 'A', "Test case 1 failed"
    assert grade_converter(85) == 'B', "Test case 2 failed"
    assert grade_converter(75) == 'C', "Test case 3 failed"
    assert grade_converter(65) == 'D', "Test case 4 failed"
    assert grade_converter(55) == 'F', "Test case 5 failed"
    assert grade_converter(105) == 'Invalid grade', "Test case 6 failed"
    assert grade_converter(-5) == 'Invalid grade', "Test case 7 failed"
    print("All grade_converter test cases passed")
    
    # Print results for visual confirmation
    print("is_even(10):", is_even(10))  # Should return True
    print("is_even(7):", is_even(7))    # Should return False
    print("grade_converter(95):", grade_converter(95))  # Should return 'A'
    print("grade_converter(55):", grade_converter(55))  # Should return 'F'
