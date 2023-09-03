if __name__ == "__main__":
    l=list(range(1000))
    for idx in range(len(l)-1,-1,-1):
        if l[idx]%2==1: 
            l.pop(idx)
    print(l)