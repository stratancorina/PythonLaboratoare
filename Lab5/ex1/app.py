__doc__ = """
1
b) Write a module named app.py. When this module is run, it will run in an infinite loop, waiting for inputs from the 
user. The program will convert the input to a number and process it using the function process_item implented in 
utils.py. You will have to import this function in your module. The program stops when the user enters the message "q".
"""

from utils import find_special_prime

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number: \n")
        if user_input == "q":
            exit()

        try:
            x = int(user_input)
            print(find_special_prime(x))
        except TypeError as e:
            print("Input is not integer", e)
        except Exception as e:
            print("Other error", e)