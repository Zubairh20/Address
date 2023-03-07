### Address Project


***Program Functionality***

The purpose of this program is to check whether or not the input entered while the code is running is a valid IP address.  It simply checks if the contents of the input align with what is typically classified as an IP address (e.g., each number in the address is between 0 and 255, inclusive).  The main() function calls validate(ip) and takes care of tasks such as printing and inputting.


**numb3rs.py**

This file contains the critical code of the program.  The code contains an if statement that establishes a specific format for IP addresses, a for statement that establishes the required range for the addresses, and two functions that carry out the main functionalities of the program.  There is the main() function, where input is accepted, one other function is called, and the final result is printed.  The other function in addition to main() is validate(ip) .  The purpose of validate(ip) is to see if the input entered fits the format and range requirements for an IP address.  If it does, then the input is valid.


*main()*

    - Calls one additional function and stores the primary input and print statements.
    - The results are output here.
  
  
*validate(ip)*

This function determines whether or not the entered input is a valid IP address.  There is an if statement which establishes the basic format for the address, and a for statement with a nested if statement that requires each number in the address to fall in a range between 0 and 255, inclusive.  The address needs to follow both requirements in order to be valid.  If the input is valid, the code returns “True”.  If it isn’t valid, then “False” is returned.


**test_numb3rs.py**

This file stores code testing numb3rs.py using pytest.  In addition to the main() function, which calls other functions to begin with, there are two other functions.  They are test_format() and test_join_book_club().  They both test the functionality of their corresponding functions in numb3rs.py depending on what input is entered while the program runs.
