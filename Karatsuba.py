from elice_utils import EliceUtils
import sys

elice_utils = EliceUtils()

# Implement here. Input is given as a single string, made of integers a and b separated by a comma, which may be of different length. Return multiplication of the two numbers as string using Karatsuba's multiplication algorithm.


def karatsuba(x):

    var1, var2 = x.split(",")

    if len(var1) == 1 or len(var2) == 1:
        return int(var1) * int(var2)

    if len(var1) < len(var2):
        var1 = var1.zfill(len(var2))

    if len(var1) > len(var2):
        var2 = var2.zfill(len(var1))

    n = len(var1)

    ceiling = (n + 1) // 2
    floor = n // 2

    A = var1[:ceiling]
    B = var1[-floor:]
    C = var2[:ceiling]
    D = var2[-floor:]

    variable1 = A + "," + C
    variable2 = str(int(A) + int(B)) + "," + str(int(C) + int(D))
    variable3 = B + "," + D

    ##return variable1, variable2, variable3

    ##return karatsuba(variable1), karatsuba(variable2), karatsuba(variable3)

    if n % 2 == 0:
        return (10 ** n - 10 ** (n // 2)) * karatsuba(variable1) + (10 ** (n // 2)) * karatsuba(variable2) + (1 - 10 ** (n // 2)) * karatsuba(variable3)

    else:
        return (10 ** (n - 1) - 10 ** ((n - 1) // 2)) * karatsuba(variable1) + (10 ** ((n - 1) // 2)) * karatsuba(variable2) + (1 - 10 ** ((n - 1) // 2)) * karatsuba(variable3)


# Do not change this part of the code. You may enter value of x in the terminal in form of a,b to test your algorithm.
def main():
    x = input()
    print(karatsuba(x))


if __name__ == "__main__":
    main()
