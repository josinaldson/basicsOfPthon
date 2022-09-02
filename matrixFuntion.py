matrix = []

m =  int(input("De number os lines in the matrix"))
n =  int(input("De number os collums in the matrix"))

def builtMatrix(m,n):

    for i in range (1, m+1):
        line = []
        for j in range (1, n+1):
            x =  int(input("De number os collums in the matrix"))
            line.append(x)
        matrix.append(line)

      
builtMatrix(m,n)

print(matrix)