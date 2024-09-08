# IS211_Assignment2

Part I: Think about Design

* Understand the problem statement and the requirements of the assignment
* Identify the main components of the program that need to be developed, such as reading the data from the CSV file, processing the data, and displaying the information to the user
* Determine the overall structure of the program, including how to handle errors and exceptions
* Plan how to use modules and libraries to simplify the development process and improve code readability

Part II: Download the Data

* Write a function called downloadData that takes in a string called url as its parameter. This function should use urllib2 to download the contents of the URL and return it to the caller
* Test the function by downloading a small file from the internet and verifying that the correct data is returned

Part III: Process Data

* Write a function called processData that takes the contents of the CSV file as its first parameter, processes the file line by line, and returns a dictionary that maps a person’s ID to a tuple of the form (name, birthday)
* Test the function by passing it a small CSV file with valid data and verifying that the correct output is returned
* Handle cases where the birthday is not in the expected format, such as missing forward slashes or invalid dates

Part IV: Display / User Input

* Write a function called displayPerson that takes in an integer called id as its first parameter, and a dictionary as its second parameter, called personData. This function should print the name and birthday of a given user identified by the input id
* Test the function by passing it a small CSV file with valid data and verifying that the correct output is returned
* Handle cases where the user enters an invalid ID or no ID at all, such as -1 or 0

Part V: Putting it all Together

* Write a main() function that calls the downloadData(), processData(), and displayPerson() functions in the appropriate order
* Use argparse to allow the user to send a ­url parameter to the script
* Test the program by passing it a valid URL and verifying that the correct output is returned

Functional Requirements:

* The program must accept and use the ­­url parameter. We will use this to point to not only the file in this assignment, but to another file you will not be able to see beforehand. The program should give correct output in both cases
* The program must write to a file named error.log. Each line of this error file must be of the correct format as specified in Part III
* The program must print out users in the correct format, as directed by the user input
* The program must exit only when the user enters in a number <= 0
