# LCSMatrix.py (Corrected again for matrix test compatibility)

class LCSMatrix:
    """
    Computes the Longest Common Subsequence (LCS) matrix for two strings,
    storing both the length and the set of all LCS strings ending at each position.
    Includes helper methods adjusted for compatibility with the provided test framework.
    """
    def __init__(self, string1, string2):
        """
        Initializes and builds the LCS matrix, storing both lengths and sets
        of subsequences in each cell.
        """
        self.row_count = len(string1) # Number of rows corresponding to string1
        self.column_count = len(string2) # Number of columns corresponding to string2
        self._string1 = string1
        self._string2 = string2

        # Internal matrix dimensions are +1 for base cases
        self._matrix_rows = self.row_count + 1
        self._matrix_cols = self.column_count + 1

        # Initialize the matrix data structure
        self._matrix = [[(0, set()) for _ in range(self._matrix_cols)]
                        for _ in range(self._matrix_rows)]

        # Fill the matrix using dynamic programming rules (Same as before)
        for r in range(1, self._matrix_rows):
            for c in range(1, self._matrix_cols):
                char1 = self._string1[r - 1]
                char2 = self._string2[c - 1]
                if char1 == char2:
                    prev_len, prev_set = self._matrix[r - 1][c - 1]
                    new_len = prev_len + 1
                    if not prev_set: new_set = {char1}
                    else: new_set = {s + char1 for s in prev_set}
                    self._matrix[r][c] = (new_len, new_set)
                else:
                    up_len, up_set = self._matrix[r - 1][c]
                    left_len, left_set = self._matrix[r][c - 1]
                    if up_len > left_len: self._matrix[r][c] = (up_len, up_set)
                    elif left_len > up_len: self._matrix[r][c] = (left_len, left_set)
                    else: self._matrix[r][c] = (up_len, up_set.union(left_set))

    def get_entry(self, row, column):
        """
        Returns the numerical length of the LCS for string1[:row+1] and string2[:column+1].
        Indices are 0-based relative to strings. Returns 0 if out of bounds.
        """
        # This implementation remains correct based on the initial prompt.
        if 0 <= row < self.row_count and 0 <= column < self.column_count:
            length, _ = self._matrix[row + 1][column + 1]
            return length
        else:
            return 0

    def get_longest_common_subsequences(self):
        """
        Returns the set of all longest common subsequences for the full strings.
        """
        # This implementation remains correct.
        lcs_len, lcs_set = self._matrix[self.row_count][self.column_count]
        if lcs_len == 0:
            return set()
        else:
            return lcs_set

    # --- Adjusted methods for compatibility with LCSTestCase ---

    def get_row_count(self):
        """
        Returns the number of rows corresponding to string1's length.
        Adjusted to match the dimensions of the expected matrix in tests.
        """
        return self.row_count # Returns len(string1)

    def get_column_count(self):
        """
        Returns the number of columns corresponding to string2's length.
        Adjusted to match the dimensions of the expected matrix in tests.
        """
        return self.column_count # Returns len(string2)

    def get_lcs_matrix(self):
         """
         Returns the numerical part of the LCS matrix (lengths only),
         excluding the 0th row and 0th column. Dimensions: row_count x column_count.
         This should align with the expected matrix format.
         """
         # This implementation remains correct for producing the expected data block.
         numerical_matrix = []
         for r in range(1, self.row_count + 1):
             row_lengths = [self._matrix[r][c][0] for c in range(1, self.column_count + 1)]
             numerical_matrix.append(row_lengths)
         return numerical_matrix

    # --- End of adjusted methods ---
