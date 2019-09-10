'''

def sort_and_countSplitInv(b, c, n):
    d = [0] * n
    i, j, inv = 0, 0, 0
    #print('bcn', b, c, n)
    for k in range(n):
        #print('splitinv', i, j, d)
        if i >= len(b):
            d[k] = c[j]
            j += 1
        elif j >= len(c):
            d[k] = b[i]
            i += 1
        elif b[i] < c[j]:
            d[k] = b[i]
            i += 1
        else:
            d[k] = c[j]
            j += 1
            inv += len(b[i:])
    return d, inv



while i < len(a) and j < len(b):
    if b[i] < c[j]:
        d[k] = b[i]
        i += 1
    else:
        d[k] = c[j]
        j+=1
        inv += len(b[i:])
d.extend(b[i:])
d.extend(c[j:])




def sort_and_count(a, n):
    if n == 1:
        return a, 0
    else:
        m = n // 2
        b, x = sort_and_count(a[:m], len(a[:m]))
        #print(b, x)
        c, y = sort_and_count(a[m:], len(a[m:]))
        #print(c, y)
        d, z = sort_and_countSplitInv(b, c, n)
        #print("D", d, z)
    return d, x + y + z


#l = [6, 5, 4, 3, 2, 1]
with open('IntegerArray.txt') as f:
    l = [int(x) for x in f]
print(sort_and_count(l, len(l)))
# print(sort_and_countSplitInv([1, 2], [3, 4], 4))

'''





def strDist(a, b, i=0, j=None):
    if j is None:
        j = len(a)
    n = len(b)
    print(a, b, i, j, a[i:i+n], a[j:j+n])
    if a[i:i+n] != b:
        d = strDist(a, b, i+1, j)
    elif a[j:j+n] != b:
        d = strDist(a, b, i, j-1)
    elif a[i:i+n] == b and a[j:j+n] == b:
        return j - i + n
    elif j < i:
        return None
    return d




print(strDist("cccatcowcatxx", "cow"))









