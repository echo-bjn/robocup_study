import itertools
total=0
num_list=[1,2,3,4]
for i in itertools.permutations(num_list,3):
    print(i[0],i[1],i[2])
    total=total+1
print(total)