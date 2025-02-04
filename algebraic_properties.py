"""

AlgebraicProperties


"""


import numpy as np
import multiprocessing as mp
import sys

#check if the input numbers were given correctly and save them in their variables
if len(sys.argv) != 4:
    raise ValueError("Input exactly three numbers")
    
try:

    N = int(sys.argv[1])
    c = float(sys.argv[2])
    T = int(sys.argv[3])
except:
    raise ValueError("At least one of the input values was not a number")

if N < 1:
    raise ValueError("The first number must be bigger than 0")
if T < 11:
    raise ValueError("The third number must be bigger than 10")


#function number 1: simple algorith with no multiprocessing involved

def test_1_no_multiprocessing():

    #generate 10 random matrices N*N: A1, A2, ..., A10
    matrices = []
    for i in range(10):
        m = np.random.randint(100, size=(N, N))
        matrices.append(m)

    #generate 10 matrices as: B1=cA1, B2=cA2, ..., B10=cA10
    matrices_b = []
    for matrix in matrices:
        b = matrix * c
        matrices_b.append(b)

    #test the equality that AiBi = BiAi; for i = 1, 2, 3, ..., 10
    check = 0
    for i in range(10):
        a = np.dot(matrices[i], matrices_b[i])
        b = np.dot(matrices_b[i], matrices[i])

        if np.array_equal(a, b):
            check += 1
            
#if all the checks have been passed, the equality is true
    if check == 10:
        print("The equality is true")
    else:
        print("The equality is false")

#this function contains instrucions about the job of each thread
def worker_function(pair):
    #pair will contain the values that are being passed
    c = pair

    #generate 10 random matrices N*N: A1, A2, ..., A10
    m = np.random.randint(100, size=(N,))

    #genrate 10 matrices as: B1=cA1, B2=cA2, ..., B10=cA10
    m_b = c * m

    return m, m_b

#function number 2: algorithm with multiprocessing involved

def test_2_multiprocessing():
    pairs = []
    for i in range(N * 10):
        pairs.append(c)

    matrix_a = np.zeros((10, N, N))
    matrix_b = np.zeros((10, N, N))

    with mp.Pool(T) as pool:
        result = pool.map(worker_function, pairs)

        i = 0
        r = 0
        for m, m_b in result:
            #i put the rows in matrix and matrix_b
            matrix_a[i][r][:] = m
            matrix_b[i][r][:] = m_b

            r += 1
            if r == N:
                i += 1
                r = 0

        check = 0
        for i in range(10):
            a = np.dot(matrix_a[i], matrix_b[i])
            b = np.dot(matrix_b[i], matrix_a[i])

            if np.array_equal(a, b):
                check += 1

        if check == 10:
            print("The equality is true")
        else:
            print("The equality is false")


if __name__ == "__main__":
    print("Exectution of the first test without multiprocessing")
    test_1_no_multiprocessing()
    print()

    print(f"Execution of the second test with multiprocessing (T = {T})")
    test_2_multiprocessing()
    print()
    pass
