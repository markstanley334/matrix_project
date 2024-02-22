from interface import * # import the python files for input and calculation
from rref import *

def main():
 
    print(" ")
    print("_________________________________________________________________")
    print("Welcome! Please select which operation you would like to perform: ") # introduction messages 
    print("_________________________________________________________________")

    while True: # input validation
        print("-------------------------------")
        print("1: Create/generate a new matrix")
        print("-------------------------------")
        print("2: Display a matrix (by itself or reduced)")
        print("-------------------------------")
        print("3: Add two matrices together")
        print("-------------------------------")
        print("4: Multiply two matrices together")
        print("-------------------------------")
        print("5: Exit program")
        print("-------------------------------")
        print(" ")

        key = input("input: ")
        print("-------------------------------")
        match key:
            case "1":
                generate_matrix() # creates or generates a matrix based on user input
            
            case "2": 
                display_matrix() # displays any of the created matrices in several different forms (after recieving user input)

            case "3":
                add()

            case "4":
                mul()

            case "5": 
                print("Thank you for using this program") # program ends 
                print("-------------------------------")
                break
        
        print("-------------------------------")
        print("Press any key to continue.") 
        inp = input("")

main() # run the main() function 