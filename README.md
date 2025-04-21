# Longest-common-subsequence
Overview
The longest common substring algorithm is presented elsewhere in this book. The longest common subsequence algorithm is similar. Unlike a substring, a subsequence need not be continuous. Ex: "ARTS" is a subsequence of ALGORITHMS, but is not a substring.

A dynamic programming matrix can be used to solve the longest common subsequence (LCS) problem. Rules for populating the matrix differ slightly from the longest common substring algorithm. Both algorithms populate rows from top to bottom, and left to right across a row. Each entry matrix[R][C] is computed as follows:

If characters match, both algorithms assign matrix[R][C] with 1 + matrix[R - 1][C - 1].
If characters do not match, the longest common _____.
substring algorithm assigns matrix[R][C] with 0
subsequence algorithm assigns matrix[R][C] with max(matrix[R - 1][C], matrix[R][C - 1])
Each algorithm uses 0 for out of bounds entries. Ex: When computing matrix[0][0] for a character match, 0 is used instead of trying to access matrix[-1][-1].


Sample matrix
The image below shows the longest common subsequence matrix for strings "ALASKAN" and "BANANAS". Entries corresponding to a character match are highlighted.

7x7 matrix with the following numerical entries: Row 0: 0, 1, 1, 1, 1, 1, 1. Row 1: 0, 1, 1, 1, 1, 1, 1. Row 2: 0, 1, 1, 2, 2, 2, 2. Row 3: 0, 1, 1, 2, 2, 2, 3. Row 4: 0, 1, 1, 2, 2, 2, 3. Row 5: 0, 1, 1, 2, 2, 3, 3. Row 6: 0, 1, 2, 2, 3, 3, 3. Entries for matching characters are highlighted.

The largest number in the matrix indicates the length of the longest common subsequence. Ex: The largest entry in the matrix above is 3, so the longest common subsequence between "ALASKAN" and "BANANAS" is 3 characters long.


Multiple longest common subsequences
A pair of strings may have more than one longest common subsequence. Ex: "ALASKAN" and "BANANAS" have three longest common subsequences: "AAA", "AAN", and "AAS".


Step 1: Determine how to make the LCS set from the matrix
The matrix can be used to build a set of all longest common subsequences. Before writing any code, consider two options for building the LCS set:

Build the entire numerical matrix, then traverse the matrix to build the LCS set.
Build a matrix of structures that include the numerical entry plus the LCS set.
The figure below illustrates approach #2.

4x4 LCS matrix for strings BAAB and ABBA. Each entry has both a number and a string set. Entries: Row0: (0, {}), (1, {B}), (1, {B}), (1, {B}). Row1: (1, {A}), (1, {A,B}), (1, {A,B}), (2, {BA}). Row2: (1, {A}), (1, {A,B}), (1, {A,B}), (2, {AA,BA}). Row3: (1, {A}), (2, {AB}), (2, {AB,BB}), (2, {AB,BB,AA,BA}). Entries for matching characters are highlighted.
Step 2: Implement the LCSMatrix class
The LCSMatrix class is declared in the LCSMatrix.py file. The __init__(), get_entry(), and get_longest_common_subsequences() methods must be completed. An attribute must also be added for the matrix data. Each matrix entry may be an integer or a more complex object, depending on the choice made in step 1.

After adding an attribute for the matrix, complete the methods to satisfy the requirements below.

__init__(): Two lines of code are given to assign the row_count and column_count attributes with string1's length and string2's length, respectively. The remainder of the method must be implemented to build the longest common subsequence matrix.
Use case-sensitive character comparisons. Ex: 'a' and 'A' are not equal.
get_entry(): Returns the numerical entry at the given row and column indices, or 0 if either index is out of bounds.
get_longest_common_subsequences(): Returns a Python set object of strings indicating all longest common subsequences for the two strings passed to the constructor.

Step 3: Test code, then submit
Code in main.py runs several test cases. Each tests the set returned from get_longest_common_subsequences(). Some test cases also check matrix entries returned from get_entry(). Ensure that all tests in main.py pass before submitting code for grading.
