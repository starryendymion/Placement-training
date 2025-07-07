class Solution:
    def celebrity(self, M, n):
        a, b = 0, n - 1
        while a < b:
            if M[a][b] == 1:
                a += 1
            else:
                b -= 1
        for i in range(n):
            if i != a and (M[a][i] == 1 or M[i][a] == 0):
                return -1
        return a
