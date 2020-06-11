def ship_server_stats(R, s, t):
    '''
    Input:  R | a list of route tuples
            s | string name of origin city
            t | string name of destination city
    Output: w | maximum weight shippable from s to t
            c | minimum cost to ship weight w from s to t
    '''
    w, c = 0, 0
    #create graph dictionary {vertex name:vertex object}
    vertices = dict()
    for route in R:
        if route[0] not in vertices:
            vertices[route[0]] = Vertex(route[0])
        if route[1] not in vertices:
            vertices[route[1]] = Vertex(route[1])
        vertices[route[0]].addChild(vertices[route[1]], route[2], route[3])
        
    #run modified dijkstra's from s to get w*
    bottlenecks = dijkstra1(s, vertices)
    w = bottlenecks[t].bottleneck
    #go through graph. remove edges w weight less than w* (go through every vertex, look at children, remove children with weight less than w*)
    copyofVert = vertices.copy()
    for node in copyofVert:
        childCopy = copyofVert[node].child.copy()
        for ch in childCopy:
            if vertices[node].child[ch][0] < w:
                vertices[node].child.pop(ch)
    #run dijkstra2 from s on modified graph to get minimum cost to ship w* to t
    cheapestPaths = dijkstra2(s, vertices)
    c = cheapestPaths[t]
    return w, c


class Vertex:
    def __init__(self, name):
        self.name = name
        #self.weight = weight
        #self.cost = cost
        self.child = dict()
        self.cheapestPath = 9999999999
        #self.visited = False
        self.bottleneck = 0
        
    def addChild(self, child, weight, cost):
        #dictionary of child nodes with key=child Vertex object and value as (weight,cost) tuple
        self.child[child] = (weight,cost)

    def updateCheapestPath(self, newcost):
        self.cheapestPath = newcost
    
    def updateBottleneck(self, newBottleneck):
        self.bottleneck = newBottleneck  
    
    
def relax1(v1, v2):
    if v2.bottleneck < min(v1.bottleneck, v1.child[v2][0]):
        v2.updateBottleneck(min(v1.bottleneck, v1.child[v2][0]))
     
        
def relax2(v1, v2):
    if v2.cheapestPath > v1.cheapestPath + v1.child[v2][1]:
        v2.updateCheapestPath(v1.cheapestPath + v1.child[v2][1])


def dijkstra1(start, graph):
    #make the queue from which we will pop out nodes with max bottlenecks
    q = graph.copy()
    #set the starting bottleneck to inf
    q[start].updateBottleneck(9999999999)
    #d is dictionary of nodes with their max bottleneck, key=Vertex name, value = max bottleneck
    d = dict()
    #loop through all of the vertices
    for node in graph:
        #find the vertex with the highest bottleneck in the queue
        maxBottle = max(q.keys(), key=(lambda k: q[k].bottleneck))
        for c in q[maxBottle].child:
            #modified relaxation (get max bottleneck for each child of current node w/max bottleneck)
            relax1(q[maxBottle], c)
        #remove node w/max bottleneck from q and add it to d
        d[maxBottle] = q.pop(maxBottle)
    return d

    
def dijkstra2(start, graph):
    #make the queue from which we will pop out nodes with cheapest paths
    q = graph.copy()
    #set the starting path to 0
    q[start].updateCheapestPath(0)
    #d is dictionary of nodes with their cheapest path, key=Vertex name, value = total cost of cheapest path
    d = dict()
    #loop through all of the vertices
    for node in graph:
        #find the vertex with the cheapest total cost in the queue
        cheapest = min(q.keys(), key=(lambda k: q[k].cheapestPath))
        for c in q[cheapest].child:
            #relaxation (get cheapest path total cost for each child of current node w/cheapest total cost)
            relax2(q[cheapest], c)
        #remove node w/max bottleneck from q and add it to d
        d[cheapest] = q.pop(cheapest).cheapestPath
    return d
        