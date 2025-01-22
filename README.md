This program takes as input three numbers:
- the first one sets the matrix size "N"
- the second one sets the scalar "c" value
- the third one sets the number of threads "T"
    
The program is then able to calulate a set of 10 random "A" matrices of size N (A1, A2, ..., A10) and a set of matrices "B" calculated from this first set (calculated as B1=cA1, B2=cA2, ..., B10=cA10).
After the two sets have been computed it tests if the equality AiBi = BiAi; for i = 1, 2, 3, ..., 10 is true.

The program has two functions: 
- the first one (called test_1_no_multiprocessing) performs the algorithm without using multiprocessing;
- the second one (called test_2_multiprocessing) exploits multiprocessing by splitting the work among "T" threads (where "T" is a value bigger than 10 specified by the user).
