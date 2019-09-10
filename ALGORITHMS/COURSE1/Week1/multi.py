from math import ceil, floor
'''
In this programming assignment you will implement one or more of the integer
multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to
multiplying only pairs of single-digit numbers. You can implement the
grade-school algorithm if you want, but to get the most out of the assignment
you'll want to implement recursive integer multiplication and/or Karatsuba's
algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some
small test cases of your own devising. Then post your best test cases to the
discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2.
Does this make your life easier? Does it depend on which algorithm you're
implementing?]

The numeric answer should be typed in the space below. So if your answer is
1198233847, then just type 1198233847 in the space provided without any space
/ commas / any other punctuation marks.

(We do not require you to submit your code, so feel free to use any programming
language you want --- just type the final numeric answer in the following
space.)
'''


def multiply_naive(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))

        # a = int(str(x)[:n // 2])
        # b = int(str(x)[n // 2:])
        # c = int(str(y)[:n // 2])
        # d = int(str(y)[n // 2:])
        '''
        a = int(str(x)[:math.ceil(n / 2)])
        b = int(str(x)[math.ceil(n / 2):])
        c = int(str(y)[:math.ceil(n / 2)])
        d = int(str(y)[math.ceil(n / 2):])
        '''
        power = ceil(n / 2)

        a = x // (10**power)
        b = x % (10**power)
        c = y // (10**power)
        d = y % (10**power)


        print(x, y, a, b, c, d)

        ac = multiply_naive(a, c)
        ad = multiply_naive(a, d)
        bc = multiply_naive(b, c)
        bd = multiply_naive(b, d)

        print(ac, ad, bc, bd)
        print(x*y, ac * (10 ** (n)) + (ad + bc) * (10 ** power) + bd)
        print()
        return ac * (10 ** (n)) + (ad + bc) * (10 ** power) + bd




def multiply_karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        power = ceil(n / 2)

        a = x // (10**power)
        b = x % (10**power)
        c = y // (10**power)
        d = y % (10**power)


        print(x, y, a, b, c, d)

        ac = multiply_karatsuba(a, c)
        bd = multiply_karatsuba(b, d)
        abcd = multiply_karatsuba((a+b), (c+d))

        print(ac, bd)
        print()
        return ac * (10 ** (n)) + (abcd - ac - bd) * (10 ** power) + bd




x = 1234
y = 5678
#x = 1234567812345678123456781234567812345678123456781234567812345678
#y = 91011121123456789101112112345678
print(multiply_karatsuba(x, y))
print()
print(x*y)


# 3000 + 730 + 92
