import sys
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
Lines_string = " ".join(Lines)
arrTerm = []

LinesStripped = []
for term in Lines:
        LinesStripped.append(term.strip())

LinesStrippedUniqed = set(LinesStripped)


for term in LinesStrippedUniqed:
        if len(term.strip())>1:
                count = Lines_string.count(term.strip())
                print(count,",",term)