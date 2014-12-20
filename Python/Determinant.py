import math
def Determinant(A,N):
    det=0.0
    if(N == 1):
        det = A[0][0]
    elif (N == 2):
        det = A[0][0]*A[1][1] - A[1][0]*A[0][1]
    else:
        for j1 in range(0,N):
            m = [[0 for x in range(N-1)] for x in range(N-1)]
            for k in range(0,N-1):
                m[k] = [0 for x in range(N-1)]
            i=1
            for i in range(1,N):
                j2=0
                for j in range(0,N):
                    if(j == j1):
                        continue
                    m[i-1][j2] = A[i][j]
                    j2+=1
            det += math.pow(-1.0,1.0+j1+1.0)* A[0][j1] * Determinant(m,N-1)
    return det

def basla():
    n = int(input("Matris boyutunu giriniz: "))
    print("Matrisin elemanlarini teker teker giriniz: ")
    mat = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(input())
    print("Matrisiniz: ",mat)
    print("Determinant sonucu: ",Determinant(mat, n))

basla()
