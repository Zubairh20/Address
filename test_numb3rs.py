from numb3rs import validate

def main():
    test_format()
    test_range()

# Test the format of the function
def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False

# Test the range of the function
def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'300.255.255.255') == False
    assert validate(r'255.300.255.255') == False
    assert validate(r'255.255.300.255') == False
    assert validate(r'255.255.255.300') == False

if __name__ == "__main__":
    main()