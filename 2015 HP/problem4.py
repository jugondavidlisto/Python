import sys
import math
import string


while True:
    n, m = map(lambda x: (str, int)[x.isdigit()](x) ,sys.stdin.readline().split(None, 2))
    if n == 0 and m == 0:
        break
    else:
        result = n * m
        print (result)
