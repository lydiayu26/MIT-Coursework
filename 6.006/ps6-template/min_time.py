class Vertex:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.child = []
        self.parent = []
        self.shortestPath = -9999999999
        self.visited = False
        
    def addChild(self, child):
        self.child.append(child)
        
    def addParent(self, parent):
        self.parent.append(parent)
    
    def updateShortestPath(self, newtime):
        self.shortestPath = newtime        


def min_time(C, D):
    '''
    Input:  C | a list of code pairs
            D | a list of dependency pairs
    Output: t | the minimum time to complete the job, 
                or None if the job cannot be completed
    '''
    t = None
    
    #CREATE GRAPH
    supernode = Vertex("super", 0)
    endnode = Vertex("end", 0)
    vertices = dict()

    for i in range(len(C)):  #initialize all vertexes as filenames
        vertices[C[i][0]] = Vertex(C[i][0], C[i][1])
    for i in range(len(D)):  #for each dependency pair, add first file as parent of second and second as child of first
        vertices[D[i][0]].addChild(vertices[D[i][1]])
        vertices[D[i][1]].addParent(vertices[D[i][0]])
    for key in vertices:
        #connect all filenames without parents to supernode and filenames without children to endnode
        if len(vertices[key].child) == 0:
            endnode.addParent(vertices[key])
            vertices[key].addChild(endnode)
        if len(vertices[key].parent) == 0:
            supernode.addChild(vertices[key])
            vertices[key].addParent(supernode)
    vertices["super"] = supernode
    vertices["end"] = endnode
    
    #run dfs to get topological order or to see if job not possible
    respond = dfs(supernode, vertices)
    if respond is None:
        return None
    order = topOrder[::-1]
    
    supernode.updateShortestPath(0)
    
    #relax all edges of graph in topological order
    updateTime(order)
    t = vertices["end"].shortestPath
    
    return t

topOrder = []
def dfs(s, graph, visited = None, respond = True):
    if visited is None:
        visited = []
    if s in visited:
        return None
    else:
        visited.append(s)
    for ch in s.child:
        if not ch.visited:
            respond = dfs(ch, graph, visited, respond)
    s.visited = True
    topOrder.append(s)
    return respond


def updateTime(graph):
    for vertex in graph:
        for child in vertex.child:
            relax(vertex,child)

def relax(v1, v2):
    if v2.shortestPath < v1.shortestPath + v1.time:
        v2.updateShortestPath(v1.shortestPath + v1.time)

