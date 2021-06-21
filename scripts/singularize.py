import sys
from dutch_pluralizer import singularize
file1 = open(sys.argv[1], 'r')
exceptions = ["as", "open", "faas", "less"]
Lines = file1.readlines()
for term in Lines:
    splited = term.replace("\n","").split(" ")
    new_term = []
    for word in splited:
        word = word.strip()
        res = singularize(word)
        if res and word not in exceptions:
            new_term.append(res)
        else:
            new_term.append(word)
    string_term = ' '.join(new_term)
    if len(string_term)>0:
        print(string_term)
        