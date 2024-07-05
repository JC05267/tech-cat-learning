def write_to_file(fname: str, lst: list[str]) -> None:
    with open(fname, "w") as file:
        for lan in lst:
            file.write(lan + "\n")

def read_from_file(fname: str) -> list[str]:
    with open(fname, "r") as file:
        lines = file.readlines()
        lst = []
        for line in lines:
            lst.append(line.replace("\n", ""))
        return lst

def count_words_in_file(fname: str) -> int:
    lst = read_from_file(fname)
    counter = 0
    for line in lst:
        words = line.split()
        counter += len(words)
    return counter


if __name__ == '__main__':
    # Test the Functions
    test_filename = "test_file.txt"
    test_lines = ["Hello world", "This is a test file", "It contains multiple lines of text"]
    
    write_to_file(test_filename, test_lines)
    read_lines = read_from_file(test_filename)
    print("Read lines:", read_lines)
    
    word_count = count_words_in_file(test_filename)
    print("Total word count:", word_count)
    
    # Validation using assert statements
    assert read_lines == test_lines, "Read lines do not match written lines"
    assert word_count == 13, "Word count does not match expected value"
    
    print("All test cases passed")
