import random
from rref import *

matrix_storage = {} # global dictionary that holds copies of the created matrices with keys based on the name provided by the user

def print_matrix(matrix): # function that prints a matrix nicely with each row corresponding to one line of text
        print('[', end = "")
        for i in range(len(matrix)):
            if i == len(matrix)-1:
                print(matrix[i], end = "")
            else:
                print(matrix[i])
        print(']')      

def get_integer_input(prompt): # function that ensures input is an integer
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt): # function that ensures input is a float 
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid float.")


def generate_matrix(): # function that creates a matrix, with either automatic generation or full user input

    while True: 
        print("How do you want to create the matrix: ")
        print("-------------------------------------")
        print("1: Manual input")
        print("------------------")
        print("2: Automatic Generation")
        print("-------------------")
        manual_or_automatic = input("Input: ")


        if manual_or_automatic == "1": # if manual, program asks for validated row and column values, as well as a name for the matrix. The user then inputs each value of the matrix
            name = input("Give a name for your matrix: ")
            rows = get_integer_input("Number of rows: ")
            rows = int(rows)          
            columns = get_integer_input("Number of columns: ")
            columns = int(columns)
            generated = []
            for r in range(rows):
                generated.append([])
                for c in range(columns):
                    item = get_float_input(f"Give the value for r{r+1}c{c+1}: ")
                    generated[r].append(float(item))
            matrix_storage[name] = generated # the matrix is added to matrix_storage
            break

        elif manual_or_automatic == "2": # for automatic generation, the user is still prompted for row, column values and a name, only now they are asked for a range of integers for the random numbers generated
            name = input("Give a name for your matrix: ")
            rows = get_integer_input("Number of rows: ")
            rows = int(rows)          
            columns = get_integer_input("Number of columns: ")
            columns = int(columns)
            start = get_integer_input("Lowest integer in the matrix: ")
            start = int(start)
            end = get_integer_input("Highest integer in the matrix: ")
            end = int(end)
            generated = []
            for i in range(rows):
                generated.append([])
                for j in range(columns):
                    generated[i].append(random.randint(start,end))

            matrix_storage[name] = generated # the matrix is added to matrix_storage
            break

        else:
            print("Invalid input. Please enter a valid selection. ")

    print(f"Matrix {name}: ") # the matrix name is printed, along with the matrix after the user is done
    print_matrix(matrix_storage[name])

def display_matrix(): # function that prints a matrix from matrix_storage in several different ways depending on user input
    print("Which matrix would you like to display?")
    for name in matrix_storage.keys(): # display all existing matrices
        print(name)

    printer = input("Input: ")

    if printer in matrix_storage:
        print("-------")
        print("Matrix form ")
        print("-------")
        print("1: Unchanged") # the matrix itself
        print("-------")
        print("2: Equation form") # the matrix if represented as a system of linear equations
        print("-------")
        print("3: Row Echelon Form") # the matrix in row echelon form 
        print("-------")
        print("4: Reduced Row Echelon Form") # the matrix in reduced* row echelon form
        
        form = input("input: ")

        match form:

            case "1": # the matrix by itself can just be called from the dictionary 
                print("---------")

                print(f"Here is \"{printer}\" in matrix form: ")

                print_matrix(matrix_storage[printer])

            case "2": # the matrix in equation form can be printed by using a nested for loop (must access each value)
                for row,value in enumerate(matrix_storage[printer]):
                    print(f"Equation {row+1}: ")
                    for col,k in enumerate(value):
                        if  col == len(matrix_storage[printer][row])-1:
                            print(f"= {k}")

                        elif col == len(matrix_storage[printer][row]) - 2:
                            print(f"{k}(x{col+1})", end = " ")

                        else:
                            print(f"{k}(x{col+1}) + ", end = " ")

            case "3": # calls the Row_Echelon_Form function to perform the necessary calculations
                if f"{printer}"[:-4] in matrix_storage:
                    print_matrix(matrix_storage[f"{printer}"]) # edgecase if _REF is already in the dictionary (operation has already been performed)
                else:
                    matrix_storage[f"{printer}_REF"] = Row_Echelon_Form(matrix_storage[printer]) # adds the row echelon form matrix to the dictionary with the tag _REF  
                    print_matrix(matrix_storage[f"{printer}_REF"])
                
            case "4": # calls the RREF function to perform the necessary calculations
                if f"{printer}"[:-5] in matrix_storage: 
                    print_matrix(matrix_storage[f"{printer}"]) # edgecase if _RREF is already in the dictionary (operation has already been performed)
                else:
                    matrix_storage[f"{printer}_RREF"] = RREF(matrix_storage[printer])
                    print_matrix(matrix_storage[f"{printer}_RREF"])

            # note: The edgecases assume that the user would not tag the end of a non reduced matrix with _REF or _RREF which is a very fair assumption
    else:
        print(f"There is no matrix with the name \"{printer}\".") # in this case the matrix does not exist in matrix_storage


def add():
    print("-------------------------------")
    if len(matrix_storage) < 2:
        print("There are not enough matrices stored, try creating some first. ")
        print("-------------------------------")

    else:
        
        print("Which matrices would you like to add? ")
    
        for name in matrix_storage.keys():
            print(name)


        print("Matrix 1")
        while True:
            m1 = input(":")
            if m1 in matrix_storage:
                break
            else:
                print(f"{m1} is not a stored matrix")
        print("Matrix 2" )
        while True:
            m2 = input(":")
            if m2 in matrix_storage:
                break
            else:
                print(f"{m2} is not a stored matrix")

        matrix_storage[f"{m1}_PLUS_{m2}"] = add_matrices(matrix_storage[m1],matrix_storage[m2])
        print("The resulting matrix is: ")

        print_matrix(matrix_storage[f"{m1}_PLUS_{m2}"])


def mul():
    print("-------------------------------")
    if len(matrix_storage) < 2:
        print("There are not enough matrices stored, try creating some first. ")
        print("-------------------------------")

    else:
        
        print("Which matrices would you like to multiply? Remember that matrix multiplication is NOT commutative")
    
        for name in matrix_storage.keys():
            print(name)


        print("Matrix 1")
        while True:
            m1 = input(":")
            if m1 in matrix_storage:
                break
            else:
                print(f"{m1} is not a stored matrix")
        print("Matrix 2" )
        while True:
            m2 = input(":")
            if m2 in matrix_storage:
                break
            else:
                print(f"{m2} is not a stored matrix")

        matrix_storage[f"{m1}_TIMES_{m2}"] = mul_matrices(matrix_storage[m1],matrix_storage[m2])
        print("The resulting matrix is: ")

        print_matrix(matrix_storage[f"{m1}_TIMES_{m2}"])









