from Binary_Tree_Set import BST_Node, Binary_Tree_Set
# ----------------------------------- #
# DO NOT REMOVE THIS IMPORT STATEMENT # 
# DO NOT MODIFY IMPORTED CODE         #
# ----------------------------------- #


class Temperature_DB_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #check to find min_date
        
        left = None
        right = None
        root = None
        if A.left:
            left = A.left.max_date
        if A.right:
            right = A.right.max_date
        root = A.item.key
        x = [thing for thing in (left, right, root) if thing is not None]
        A.max_date = max(x)
        
        left = None
        right = None
        root = None
        if A.left:
            left = A.left.min_date
        if A.right:
            right = A.right.min_date
        root = A.item.key
        x = [thing for thing in (left, right, root) if thing is not None]
        A.min_date = min(x)
        
        
        #if A.left is None:
         #   A.min_date = A.item.key
        #else: #A.left:
         #   A.min_date = A.left.min_date
        
        #check to find max_date
        #if A.right is None:
         #   A.max_date = A.item.key
        #else:# A.right:
         #   A.max_date = A.right.max_date
       
        
        left = None
        right = None
        root = None
        if A.left:
            left = A.left.max_temp
        if A.right:
            right = A.right.max_temp
        root = A.item.temp
        x = [thing for thing in (left, right, root) if thing is not None]
        A.max_temp = max(x)
        #check to find max_temp
        #if A.left is None and A.right is None:
         #   A.max_temp = A.item.temp
        #elif A.left is None and A.right:
         #   A.max_temp = max(A.item.temp, A.right.max_temp)
        #elif A.left and A.right is None:
         #   A.max_temp = max(A.item.temp, A.left.max_temp)
        #else: #A.left and A.right:
         #   A.max_temp = max(A.item.temp, A.left.max_temp, A.right.max_temp)

    def subtree_max_in_range(A, d1, d2):
        max_temp = None
        if d1>A.max_date or d2 < A.min_date:
            return None
        elif d1<= A.min_date and d2>= A.max_date:
            return A.max_temp
       
        else:
            if A.item.key >= d1 and A.item.key <= d2:
                max_temp = A.item.temp
            #max_temp = A.item.temp
            if A.left:
                left_maxtemp = A.left.subtree_max_in_range(d1, d2)
                if left_maxtemp:
                    if (not max_temp or left_maxtemp > max_temp):
                        max_temp = left_maxtemp
            if A.right:
                right_maxtemp = A.right.subtree_max_in_range(d1, d2)
                if right_maxtemp:
                    if (not max_temp or right_maxtemp > max_temp):
                        max_temp = right_maxtemp
        return max_temp
        
        """
        left = None
        right = None
        root = None
        if A.left:
            left = A.left.subtree_max_in_range(d1,d2)
        if A.right:
            right = A.right.subtree_max_in_range(d1,d2)
        if A.item.key <=d2 and A.item.key >= d1:
            root = A.item.temp
        x = [thing for thing in (left, right, root) if thing is not None]
        if len(x)== 0:
            return None
        return max(x)
        """
        
       
    

# ----------------------------------- #
# DO NOT MODIFY CODE BELOW HERE       # 
# ----------------------------------- #
class Measurement:
    def __init__(self, temp, date):
        self.key  = date
        self.temp = temp

    def __str__(self): 
        return "%s,%s" % (self.key, self.temp)

class Temperature_DB(Binary_Tree_Set):
    def __init__(self): 
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
