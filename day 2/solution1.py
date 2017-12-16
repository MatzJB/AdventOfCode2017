
def checkSum(st):
    ''' sum of difference between max and min value of each row '''
    sum = 0
    for rowstring in st:
        elts = rowstring.split()
        elts = map(int, elts)
        sum += max(elts) - min(elts)

    return sum

inputfilename = 'input'
with open(inputfilename) as f:
    rows = f.readlines()

cs = checkSum(rows)
print 'sum:', cs
