import math
import random


class Sort:
    def __init__(self):
        self.n = 0

    def Median(self, a, b, c):
        # print(a, b, c)
        x = a - b
        y = b - c
        z = a - c
        if x * y >= 0:
            return b
        elif x * z >= 0:
            return c
        else:
            return a

    def ChoosePivotMedian(self, A, l, r):
        if r - l < 2:
            return l
        median = (math.ceil(len(A[l:r]) / 2) - 1) + l
        m = self.Median(A[l], A[median], A[r - 1])
        # print(A[l], A[median], A[r - 1])
        # print("median", m, A.index(m))
        return A.index(m)

    def ChoosePivotFirst(self, A, l, r):
        return l

    def ChoosePivotLast(self, A, l, r):
        return r - 1

    def ChoosePivotRandom(self, A, l, r):
        return random.choice(range(l, r))

    def Partition(self, A):
        l = 0
        r = len(A)
        p = A[l]
        i = l + 1
        for j in range(l + 1, r):
            # self.n += 1
            if A[j] < p:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[i - 1], A[l] = A[l], A[i - 1]
        return A, i - 1

    def QuickSort(self, A, l=0, r=None):
        if r is None:
            r = len(A)
        # print(A, l, r)
        if l >= r or r < 1:
            return A
        else:
            # print(r - l)
            pass
        i = self.ChoosePivotRandom(A, l, r)
        A[i], A[l] = A[l], A[i]
        # j = self.Partition(A, l, r)
        # self.n += (r - l - 1)
        # self.QuickSort(A, l, j - 1)
        # self.QuickSort(A, j + 1, r)
        A, j = self.Partition(A)
        self.n += (r - l - 1)
        A[:j] = self.QuickSort(A[:j])
        A[j + 1:] = self.QuickSort(A[j + 1:])
        return A

    def PartitionOld(self, A, l, r):
        p = A[l]
        i = l + 1
        for j in range(l + 1, r):
            self.n += 1
            if A[j] < p:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[i - 1], A[l] = A[l], A[i - 1]
        return i - 1

    def QuickSortOld(self, A, l=0, r=None):
        if r is None:
            r = len(A)
        if l >= r:
            return
        # print(A, l, r)
        i = self.ChoosePivotLast(A, l, r)
        A[i], A[l] = A[l], A[i]
        j = self.PartitionOld(A, i, r)
        print(j, A[l:j], A[j:r])
        # self.n += (r - l - 1)
        self.QuickSortOld(A, l, j)
        self.QuickSortOld(A, j + 1, r)
        return A[l:r]


if __name__ == '__main__':
    # A = [2, 4, 3, 5, 6, 8]
    A = [5, 4, 3, 2, 1]
    with open('QuickSort.txt') as f:
        A = [int(x) for x in f]
    s = Sort()
    # A = s.QuickSortOld(A)
    A = s.QuickSort(A)
    # print(A)
    print(s.n)
