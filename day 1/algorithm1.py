
def christmasSummation(st, distance=1):
    ''' sum of int string if neighbour characters 
    (using distance) are the same '''
    n = len(st)
    sum = 0
    for i in range(0, len(st)):
        if st[i] == st[(i+distance) % n]:
            sum += int(st[i])
    return sum

inputfilename = 'input'
with open(inputfilename) as f:
    content = f.readlines()
content = ''.join(content)

sum = christmasSummation(content, len(content)/2)
print sum
