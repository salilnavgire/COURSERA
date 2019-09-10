class Sort:
    def __init__(self, A, l=0, r=None):
        self.A = A
        self.l = l
        self.r = r
        self.count = 0


    def ChoosePivot0(A, l, r):
        return l

    def Partition(A, l, r):
        p = A[l]
        i = l + 1
        for j in range(l + 1, r):
            if A[j] < p:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[i - 1], A[l] = A[l], A[i - 1]
        return i - 1


    def QuickSort(A, l=0, r=None):
        if r is None:
            r = len(A)
        print(A, l, r)
        if l >= r:
            return
        i = ChoosePivot0(A, l, r)
        A[i], A[l] = A[l], A[i]
        j = Partition(A, l, r)

        QuickSort(A, l, j - 1)
        QuickSort(A, j + 1, r)


if __name__ == '__main__':
    A = [3, 1, 2]
    QuickSort(A)
