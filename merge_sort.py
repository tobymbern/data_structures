

import numpy as np



def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [None]*(n1+1)
    R = [None]*(n2+1)

    for i in range(n1+1):
        L[i] = A[p+i-1]
    for j in range(n2+1):
        R[j] = A[q+j]
    L[n1+1]  = np.Infinity
    R[n2+1] = np.Infinity
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j +
    return A



def merge_sort(A,p,r):


    if p < r:
        q = np.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return





A = [1,2,3,4,8,2,20,13,0]
print(A)
p = A[0]
r = A[-1]
merge_sort(A,p,r)
print(A)
