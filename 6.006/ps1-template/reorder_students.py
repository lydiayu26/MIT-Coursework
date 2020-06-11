def reorder_students(L):
    '''
    Input:  L    | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    #find the middle node (the last node in the first line)
    middle = L.head
    idx = 0
    while idx < L.size/2 - 1:
        middle = middle.next
        idx += 1
    
    #create temporary vars that represent the next three nodes to be "modified"
    a = middle.next
    if a.next != None:      #check to make sure there is another node after a
        b = a.next
        a.next = None
        if b.next != None:  #check to make sure there is another node after b
            c = b.next
            while b.next != None and c.next != None:       #loop until you run out of nodes
                b.next = a      #reverse the direction of the current node 
                a = b           #shift down the nodes in focus
                tempC = c
                c = c.next
                b = tempC
            b.next = a
            c.next = b
            middle.next = c
        else:           #if there is no other node after b, reverse b's pointer and point middle to b
            b.next = a
            middle.next = b
    return
