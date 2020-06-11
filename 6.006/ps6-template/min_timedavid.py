class Node:
    def __init__(self, name, parent = None):
        self.name = name
        self.time = 0
        self.child = set()
        self.parent = parent
        self.node_value = -9999999999999
        self.visited = False

    def update_time(self, time):
        self.time = time

    def add_child(self, child):
        self.child.add(child)

    def update_parent(self, parent):
        self.parent = parent

    def update_node_value(self, time):
        self.node_value = time

TopSort = []


def DFS(node, G, currently_in_recursion = None, respond = True):
    if currently_in_recursion is None:
        currently_in_recursion = set()
    if node in currently_in_recursion:
        return None
    else:
        currently_in_recursion.add(node)
    for child in node.child:
        if not child.visited:
            child.parent = node
            respond = DFS(child, G, currently_in_recursion, respond)
    node.visited = True
    TopSort.append(node)
    return respond



def relax(u, v):
    if v.node_value < u.node_value + u.time:
        v.update_node_value(u.node_value + u.time)
        v.update_parent(u)


def update_time(G):
    for node in G:
        for child in node.child:
            relax(node, child)


def min_time(C, D):
    '''
    Input:  C | a list of code pairs
            D | a list of dependency pairs
    Output: t | the minimum time to complete the job, 
                or None if the job cannot be completed
    '''
    node_dict = dict()
    for parent, child in D:
        if parent not in node_dict:
            node_dict[parent] = Node(parent)
        if child not in node_dict:
            node_dict[child] = Node(child, node_dict[parent])
        node_dict[parent].add_child(node_dict[child])
        node_dict[child].update_parent(node_dict[parent])

    initial_node = Node('initial')
    last_node = Node('last')
    for node in node_dict.values():
        if node.parent is None:
            node.update_parent(initial_node)
            initial_node.add_child(node)
        if not node.child:
            node.add_child(last_node)
    node_dict['initial'] = initial_node
    initial_node.update_node_value(0)
    node_dict['last'] = last_node

    for file, time in C:
        node_dict[file].update_time(time)
    respond = DFS(initial_node, node_dict)
    if respond is None:
        return None
    topological = TopSort[::-1]
    update_time(topological)
    return node_dict['last'].node_value