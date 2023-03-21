#put your the required matrix in 2-D array form as given below (make sure it is a square matrix):
#dummy matrix 1
mat = [[1,2,3],
       [5,4,6],
       [7,8,9]]
#dummy matrix 2
mat1 = [
    [2,2,1,5,2,8],
    [7,8,9,1,1,2],
    [1,4,5,1,7,8],
    [9,0,2,2,3,2],
    [5,6,7,8,9,3],
    [1,2,3,3,5,1]
]
n = len(mat)        #order of matrix

#printing the matrix

for i in range(0,n):
    for j in range(0,n):
            print(mat[i][j], end=' ')
    print()

def det(mat):       #creating a recursive function to calculate the determinant using Laplace expansion
    n=len(mat)
    if n==1:
        return mat[0][0]
    # elif n==2:
    #     return (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
    else:
        sum = 0
        for o in range(n): #expanding along first row
            A = []
            for i in range(1,n): #using nested loop to create minors and cofactors & i started form 1 instead of zero because we are expanding along first row i.e. i = 0, so it will deleted in every iteration.
                r=[]
                for j in range(n):
                    if (i!=0) and (j!=o): #making condition to delete cofactor'row and column 
                        r.append(mat[i][j])    
                A.append(r)
            # A.pop(0)
            # print(A)
            sum+=((-1)**o) * mat[0][o] * det(A)
        return sum
f = det(mat)
print("Determinant of give matirx is {}.".format(f))