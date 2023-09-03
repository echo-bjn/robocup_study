listnum=[0,1,1]
for x in range(4,21):
    listnum.append(listnum[x-2]+listnum[x-3])
print(listnum)