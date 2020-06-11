def get_damages(H):
    '''
    Input:  H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    def make_tuples(h):
        tuple_list = []
        for index, item in enumerate(h):
            tuple_list.append((item,index))
        return tuple_list

    def merge_sort(A, counter, a=0, b=None):
        if b is None:
            b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, counter, a, c)
            merge_sort(A, counter, c, b)
            L, R = A[a:c], A[c:b]
            merge(A, L, R, len(L), len(R), a, b, counter)

    def merge(A, L, R, i, j, a, b, counter):
        if a < b:
            if (j <= 0) or (i > 0 and L[i - 1][0] > R[j - 1][0]):
                A[b - 1] = L[i - 1]
                i = i - 1
                counter[L[i][1]] += j
            elif i > 0 and L[i - 1][0] == R[j - 1][0]:
                A[b - 1] = R[j - 1]
                j -= 1
            else:
                A[b - 1] = R[j - 1]
                j -= 1
            merge(A, L, R, i, j, a, b - 1, counter)

    counter = [1 for _ in H]
    H = make_tuples(H)
    merge_sort(H, counter)
    return counter