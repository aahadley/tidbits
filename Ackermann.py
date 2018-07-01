# The Ackermann function is a total computable function that is not primitive recursive.
# The Peter-Ackermann function is a two-variable variant of Ackermann's original function.
#
# First, define these terms.
# 
#  - Functions, partial functions, and total functions:
#
#      A function f: X --> Y is a mapping of each element of X to one and only one element of Y.
#          where X and Y are nonempty sets.
#
#      A partial function f: X' -/-> Y maaps each element of some subset of X, called X', to
#          an element in Y.
#
#      When X' is an improper subset, that is, when X' = X, we say that f is a total function.
#          This is equivalent to saying that f is a function, but the explicit distinction is useful
#          in fields where improper functions are common.
#
#  - Computable Funtions:
#       
#       A computable function is simply a function that can be solved using an algorithm.
#           This is an informal, but sufficient definition.
# 
#  - Primitive Recursive Functions:
#       
#       This is a long definition, so get ready
#
#       Consider a function f(x1, x2, ... , xn), and the abbreviation f(...) to be equivalent.
#       f is primitive recursive if it belongs to one of the following categories.
#
#           - The zero function:
#               f always returns zero.
#               f(...) = 0.
#
#           - The successor function:
#               f always returns its argument's successor.
#               f(...) = xi + 1.
#
#           - The projection function:
#               f always returns its argument.
#               f(...) = xi
#
#           - Composition:
#               f is composed of some number of the aforementioned primitive recursive functions.
#               f(...) = h(g1 + g2 + ... + gn). where h and gi are primitive recursive functions.
#
#           - Primitive recursion:
#               f is defined by the recursion of two primitive recursive functions.
#
#       If f can be obtained by applying these rules a finite number of times, f is primitive recursive.
#
#====================================================================================
#
#   The Ackermann function:
#       
#       Originally published in 1928 by Wilhelm Ackermann, the Ackermann function is a three-argument function
#           that is total, computable, but not primitive recursive. 
#
#       It is defined as follows:
#       
#       P(m, n, p):     P(m, n, 0) = m + n
#                       P(m, 0, 1) = 0
#                       P(m, 0, 2) = 1
#                       P(m, 0, p) = m for p > 2
#                       P(m, n, p) = P(m, P(m, (n - 1), p), p - 1) for n > 0 and p > 0.
#       where, m, n, and p are nonnegative integers.
#
#       The commonly preferred variant, developed by Rozsa Peter and Raphael Robinson, is shown below.
#
#       P(m, n):        n + 1                       if m = 0
#                       P((m - 1), 1)               if m > 0 and n = 0
#                       P((M - 1), P(m, (n - 1)))   if m > 0 and n > 0.
#                      
#===================================================================================
#
#   To run this program, type Ackermann.py followed by two integers.
#   
#   Runtime analysis and proof of non-primitive recursion to follow.


import sys

# Here we recursively define the Peter-Ackermann function.
def ack(m, n):

    if m == 0:
        return n + 1

    elif m > 0 and n == 0:
        return ack((m - 1), 1)

    elif m > 0 and n > 0:
        return ack((m - 1), ack(m,(n - 1)))

# Get input and check for errors.
def main(argv):
    
    #ncomment the following line ONLY if
    sys.setrecursionlimit(70000)
    print(sys.getrecursionlimit())

    try:
        m = int(sys.argv[1])
        n = int(sys.argv[2])
    
    except ValueError:
        print("Please enter two nonnegative integers.")
        return

    if m < 0 or n < 0:
        print("Please enter two nonnegative integers.")
        return

    result = ack(m, n)
    print(result)

if len(sys.argv) != 3:
    print("Please enter two nonnegative integers.")

elif __name__ == "__main__":
    main(sys.argv[1:])