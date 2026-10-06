class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = []
        columns = []

        for i in range(len(matrix)): 

            for j in range(len(matrix[0])): 

                if matrix[i][j] == 0: 
                    row.append(i)
                    columns.append(j)


        for i in range(len(row)): 
            matrix[row[i]] = [0] * len(matrix[0])

        for j in range(len(columns)): 
            for i in range(len(matrix)):
                matrix[i][columns[j]] = 0
