import itertools
listo1 = ['a','b','c','d','e']
for i in range(len(listo1)):
    print(list(itertools.permutations(listo1,i+1)))