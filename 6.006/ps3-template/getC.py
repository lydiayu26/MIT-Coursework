A = [67, 13, 49, 24, 40, 33, 58]
for c in range(1,20):
    B = set()
    for x in A:
        B.add(((11*x+4)%c)%9)
    print("c="i, ",", len(B))