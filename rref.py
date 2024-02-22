import random


def switch_rows(matrix,row_a,row_b): # elementary row operation to switch two rows in a matrix
    if row_a == row_b:
        return
    hold = matrix[row_a]
    matrix[row_a] = matrix[row_b]
    matrix[row_b] = hold

def scale_row(matrix,row,scalar): # elementary row operation to multiply each element of a row in a matrix by a scalar 
    matrix[row] = [i*scalar for i in matrix[row]]
    for i in range(len(matrix[row])):
        matrix[row][i] = round(matrix[row][i],4)

def add_scaled_rows(matrix,changed_row,scalar_row,scalar): # elementary row operation to add a scalar multiple of one row to another row
    for i in range(len(matrix[changed_row])):
        matrix[changed_row][i] += matrix[scalar_row][i]*scalar
        matrix[changed_row][i] = round(matrix[changed_row][i],4)


def format(m): # function to format a matrix nicely
    length = len(m)

    for row in range(len(m)):
        for col in range(len(m[0])):
            m[row][col]+=0
            m[row][col] /= 1
            m[row][col] = round(m[row][col],4)


    return m
 
def RREF(matrix): # function to get the reduced row echelon form of a matrix
    REF = Row_Echelon_Form(matrix)

    for row in range(-1, -len(REF), -1): # looping through backwords, the pivots eliminate elements above in the matrix
        for col in range(len(REF[0])):
            if REF[row][col] == 1:
                piv = col

                for remove in range(row-1,-len(REF)-1,-1):
                    
                    add_scaled_rows(REF,remove,row, -(REF[remove][piv]))
                break

            else:
                continue

    for row in range(len(REF)):
        for col in range(len(REF[0])):
            REF[row][col]+=0
            REF[row][col] /= 1
            REF[row][col] = round(REF[row][col],3)

    return REF


def Row_Echelon_Form(matrix): # function to put a matrix in row echelon form 
    final = matrix.copy()

    if final == []: # if the matrix is empty, it is already in RREF
        final = format(final)
        return final

    elif len(final) == 1: # if the matrix is 1 x n , then it is already in RREF 
        final = format(final)
        return final 
    
    elif len(final[0]) == 1: # for a vector, determine where the first value takes place, then all values below will become 0
        halt = False
        for i in range(len(final)):
            if final[i] == [0]:
                continue
            elif halt:
                final[i] = [0]
                continue
            else:
                final[i] = [1]
                halt = True

        final = format(final)
        return final

    else:
        row = 0
        col = 0        
        row_min = 0
        col_min = 0

        row_cap = len(final)-1

        while True:

            if row > row_cap or col > len(final[0])-1: # if we keep going too far, return the final list
                final = format(final)
                return final
    
            else:
                for i in range(len(final[row_min])): # checks if first row is a zero row. If yes, swaps with last row 
                    if final[row_min][i] != 0:
                        break
                    else:
                        
                        if i == len(final[0]) - 1: 
          
                            switch_rows(final,row_min,row_cap) # move the zero row to the last row, then reduce the row cap by 1
                            row_cap -= 1 
                            if row_cap == 0:
                                final = format(final)
                                return final

                if final[row][col] != 0:

                    switch_rows(final,row,row_min)


                    if final[row_min][col_min] != 1:
                        scale_row(final,row_min,(1/final[row_min][col_min]))

                    for r in range(row_min+1,row_cap+1):
                        if final[r][col_min] != 0:
                            add_scaled_rows(final,r,row_min,-final[r][col_min])
                        else:
                            continue
                    
                    row_min += 1 
                    col_min += 1 
                    row = row_min
                    col = col_min

                else:
                    if row == len(final)-1:
                        col_min += 1
                        col = col_min
                        row = row_min

                    else:
                        row += 1 


def mul_matrices(matrix_a,matrix_b): # function to multiply matrices together using list comprehension

    if not matrix_b or not matrix_a:
        return None
    elif len(matrix_a[0]) != len(matrix_b): # in order to multiply 2 matrices, the number of columns in the first must be the same as the number of rows in the second
        return None
    
    rows = len(matrix_a)
    cols = len(matrix_b[0]) 
    
    return [[sum([matrix_a[i][k]*matrix_b[k][j] for k in range(len(matrix_b))]) for j in range(cols)] for i in range(rows)]


def add_matrices(matrix_a,matrix_b):
    if not matrix_b or not matrix_a:
        return None
    elif len(matrix_a) != len(matrix_b):
        return None
    elif len(matrix_a[0]) != len(matrix_b[0]):
        return None
    else:
        return [[matrix_a[j][i] + matrix_b[j][i] for i in range(len(matrix_a[0]))] for j in range(len(matrix_a))]
    

                    
  






















