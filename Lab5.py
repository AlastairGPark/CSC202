from typing import List
import math
import timeit
import random

def randomize(size:int) -> List[int]:
    list10:list[int] = []
    for i in range(0, size):
        x = random.randint(1, 10000000)
        list10.append(x)
    list10.sort()
    return list10

def main(args:List[str]) -> int:
    for size in [10, 100, 1000]:
        setup: str = 'randomlist = randomize({0})'.format(size)
        cmd: str = 'randomlist.sort()'
        t: float = timeit.timeit(stmt=cmd, setup = setup, globals=globals())
        print('The length of the list is: ', size)
        print('The time to sort the list is: ', t)
    return()

if __name__ == '__main__':
    import sys
    main(sys.argv)

# Time to sort list of 10: 0.1764912220005499
# TIme to sort list of 100: 2.905904765999992
# Time to sort list of 1000: 11.338722427999997

# Computer specs:
# CPU: Intel(R) Celeron(R) N4020
# Clock Speed: 2.7GHz
# OS: Version 110.0.5481.181 (Official Build) (64-bit)
# Python version 3.9.2 64-bit