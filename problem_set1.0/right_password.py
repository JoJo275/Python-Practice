#!/usr/bin/env python3
"""right_password.py

In a file named right_password.py, implement a program that prompts the user
for a password and checks it against a stored password. The program should
have the following features:
- On call of program, the user in prompted to enter a password.
- The program checks the entered password against a stored password.
- If the password is correct, the program prints "Correct." and exits
with a status code of "good job".
- If the password is incorrect, the program prints "Incorrect." and
prints a hint to the user.
- If, after five incorrect attempts, the user still has not entered the
correct password, the program prints "Too many incorrect attempts. Exiting."
with the exit code "good try".

"""

def main():


def getpass():
    """
    Get password from user.
        
        
        Args:
            input_data (Any): The input data to process. Can be any type
                            depending on application needs (str, dict, list,
                            file path, etc.).
        
        Returns:
            Any: The processed result. Type depends on the implementation.
                 Default implementation returns a formatted string.
        
        Side Effects:
            - Logs an INFO message about processing
            - May modify internal state (in overridden versions)
        
        Example:
            >>> app = Application()
            >>> result = app.process("test data")
            >>> print(result)
            'Processed: test data'
        
        Override Example:
            class DataProcessor(Application):
                def process(self, input_data):
                    # Parse input
                    data = parse_csv(input_data)
                    # Transform data
                    transformed = transform_data(data)
                    # Return result
                    return transformed
    """





if __name__ == "__main__":
    main()
