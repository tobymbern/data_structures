

import numpy as np

L = [0:10]
print(L)


def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [None]*(n1+1)


def merge_sort(A,p,r):

    if p < r:
        q = np.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return the_thing





