def get_col_array (board, i, last=False):
    """
    Will return the col as an array
    :param board: board representation
    :param i: column you want to get
    :return: array
    """
    col = ''
    if not last:
        for j in range(len(board)):
            col+= board[j][i]
    else:
        for j in range(len(board)):
            col += 'b'
    return col

def find_first_empty (col):
    """
    Finds the first empty block we have
    :param col: array rep of the col
    :return: index number or False if does not exist
    """
    for i in range(len(col)-1, -1, -1):
        if col[i] == '.':
            # print(i)
            return i
    return -1

def place_block (col,i,j=None):
    """
    Places a block in the given index
    :param col: array rep of the col
    :param i: index we want to place a block at
    :return: new col representation
    """
    col = col[:i] + 'd' + col[i+1:]
    if j is not None:
        col = col[:j] + 'd' + col[j + 1:]
    return col


min_dict = {}


def build_the_fucking_wall(col1,col2,i,k, B, sol=None):
    if sol is None:
        sol = set()

    if (i,col1,col2) in min_dict:
        min_val, tosend =  min_dict[(i,col1,col2)]

        return tosend.copy(), min_val

    if i > k and find_first_empty(col1) >=0:
        # If we off bounds and have more to solve
        return sol, 9999999

    if i > k and find_first_empty(col1) < 0:

        return sol, 0

    free_place_in_col1 = find_first_empty(col1)

    if free_place_in_col1 < 0:
        col1 = col2
        i += 1
        if i < k:
            col2 = get_col_array(B, i+1)
        if i == k:
            col2 = get_col_array(B, i, True)

        return build_the_fucking_wall(col1, col2, i, k, B,sol.copy())

    number_of_blocks_for_D = number_of_blocks_for_R = 99999

    if free_place_in_col1-1 >= 0 and col1[free_place_in_col1-1] == '.':
        sol_d, number_of_blocks_for_D = build_the_fucking_wall(
            place_block(col1,free_place_in_col1, free_place_in_col1-1),
            col2,
            i,
            k,
            B,
            sol.copy()
        )
    if col2[free_place_in_col1] == '.' and col1[free_place_in_col1] == '.':
        sol_r, number_of_blocks_for_R = build_the_fucking_wall(
            place_block(col1, free_place_in_col1),
            place_block(col2, free_place_in_col1),
            i,
            k,
            B,
            sol.copy()
        )
    if col1[free_place_in_col1] == '.':
        sol_s, number_of_blocks_for_single = build_the_fucking_wall(
            place_block(col1,free_place_in_col1),
            col2,
            i,
            k,
            B,
            sol.copy()
        )
        number_of_blocks_for_single += 1
    solution_dict = {
        'R': number_of_blocks_for_R,
        'D': number_of_blocks_for_D,
        '1': number_of_blocks_for_single
    }
    min_value = min(solution_dict.values())
    for name, sol in solution_dict.items():

        if sol == min_value:
            if name == '1':
                sol_s.add((i, free_place_in_col1, name))
                to_send = sol_s
            elif name == 'R':
                sol_r.add((i, free_place_in_col1, name))
                to_send = sol_r
            else:
                sol_d.add((i, free_place_in_col1-1, name))
                to_send = sol_d
            break
    min_dict[(i,col1, col2)] = (min_value, to_send.copy())
    return to_send, min_value




def build_wall(B):
    '''
    Input:  B | a border plan corresponding to
              | a length-5 array of length-n strings
    Output: P | a complete non-overlapping placement for B
              | that minimizes the number of cube stones used
    '''
    col1 = get_col_array(B,0)
    col2 = get_col_array(B,1)
    final, min = build_the_fucking_wall(col1, col2, 0, len(B[0])-1, B)
    return final

