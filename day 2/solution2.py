'''
Exercise 2 of Advent of Code 2017
Author: NatzJB
'''
from fractions import gcd


def getOnlyDivisor(arr):
    ''' Finds the first occurance of the division between two elements that evenly divide '''
    arr = sorted(arr, reverse=True)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] % arr[j] == 0:
                return int(arr[i] / arr[j])
    if True:
        print 'Could not find any divisor for array {}'.format(arr)
        return None


def checkSum(st):
    ''' Sum of the difference between max and min value of each row '''
    sum = 0
    for rowstring in st:
        elts = rowstring.split()
        elts = map(int, elts)
        sum += getOnlyDivisor(elts)
    return sum

inputfilename = 'input'
with open(inputfilename) as f:
    rows = f.readlines()

cs = checkSum(rows)
print 'Checksum:', cs
