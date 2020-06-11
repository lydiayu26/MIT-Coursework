# 6.0002 Problem Set 2
# Graph optimization
# Name: Lydia Yu
# Collaborators: Wilson Spearman
# Time: 5 hrs

#
# Finding shortest paths through the Boston t
#


import unittest
from graph import Digraph, Node, WeightedEdge


# PROBLEM 2: Building up the Boston t Map
#
# PROBLEM 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the times
# represented?
#
# ANSWER: the nodes are the T stops, the edges represent the connections between the stops, and the times are the weights of each edge



# PROBLEM 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following format, separated by blank spaces:
            From To TotalTime LineColor
        e.g.
            green_st forest_hills 3 orange
        This entry would become an edge from green_st to forest_hills on the orange line. There should also be
        another edge from forest_hills to green_st on the orange line with time travelled = 3

    Returns:
        a directed graph representing the map
    """
    graph = Digraph()
    
    f = open(map_filename, "r")
    for line in f:
        entry = line.split()
        source = Node(entry[0])
        dest = Node(entry[1])
        time = entry[2]
        color = entry[3]
        
        #add the source and dest nodes to the graph as long as they don't already exist
        if not graph.has_node(source):
            graph.add_node(source)
        if not graph.has_node(dest):
            graph.add_node(dest)
        
        #run add_edge on the values in this line in the doc, which automatically adds the reverse edge as well
        graph.add_edge(WeightedEdge(source, dest, time, color))

    return graph

# PROBLEM 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
#f = "testfile.txt"    
#g = load_map(f)
#print(g)

# PROBLEM 3: Finding the Shortest Path using Optimized Search Method
#
# PROBLEM 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# ANSWER: The objective function is get to the destination in the shortest time possible. The constraints are the certain color lines of the T you are not allowed to go on.

# PROBLEM 3b: Implement add_node_to_path
    

def add_node_to_path(node, path):
    """
    Parameters:
        path: list composed of [[list of nodes], int]
            Represents the current path of nodes being traversed. Contains
            a list of nodes (Node) and total time traveled
    
        node: Node object 
            Node of t stop being added to the path
            
    Returns:
        [[list of nodes], int] - A safely COPIED version of path with the Node added to the end of 
        a COPY of the first element of path.
        
        This method should not mutate path or path[0]
        
    """
    path_copy = path[:]
    nodes = path_copy[0][:]
    nodes.append(node)
    
    return [nodes, path_copy[1]] 


# PROBLEM 3c: Implement get_best_path
def get_best_path(digraph, start, end, path, restricted_colors, best_time,
                  best_path):
    """
    Finds the shortest path between t stops subject to constraints.

    Parameters:
        digraph: Digraph
            The graph on which to carry out the search
        start: Node
            t stop at which to start
        end: Node
            t stop at which to end
        path: list composed of [[list of Nodes], int]
            Represents the current path of nodes being traversed. Contains
            a list of Nodes and total time traveled.
        restricted_colors: list[strings]
            Colors of lines not allowed on path
        best_time: int
            The shortest time between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of Nodes
            The path with the shortest total time found so far between the original start
            and end node.

    Returns:
        A tuple of the form (best_path, best_time).
        The first item is the shortest-path from start to end, represented by
        a list of t stops (Nodes).
        The second item is an integer, the length (time traveled)
        of the best path.
        

        If there exists no path that satisfies restricted_colors constraints, then return None.
    """
    #ValueError if nodes not on map
    if not digraph.has_node(start) or not digraph.has_node(end):
        raise ValueError
    
    #base case - if start and end nodes are the same, you've found a path and return the list of nodes and time it took to get there
    elif start == end:
        return tuple(path)
    
    #loops through children nodes of the start node by getting dest note from edges leading away from start
    for edge in digraph.get_edges_for_node(start):
        node = edge.get_destination()
        #makes sure the color of the edge is not restricted
        #and avoids cycles - don't want nodes that you've already traversed
        if edge.get_color() not in restricted_colors and node not in path[0]:
            #creates a new path to follow with the dest node added to the list of nodes already travelled to in the current path
            #newPath is the original path plus the child node of start and the time it takes to get to that node
            newPath = add_node_to_path(node, path)
            #adds the time it takes to get to the dest node to the total time of the new path
            newPath[1] += edge.get_total_time()
            
            #if the time to traverse the new path is less than
            if newPath[1] < best_time:
                #finds optimal path from the new node to the end given newPath as the path already traversed with the new node added
                nextPath = get_best_path(digraph, node, end, newPath, restricted_colors, best_time, best_path)
                #if the next path exists and its time is less than the existing best time, change the old best time and path to the ones for the next path
                if nextPath != None and nextPath[1] < best_time:
                    best_time = nextPath[1]
                    best_path = nextPath[0]                    
                    
    if best_path == None:
        return None
   
    return (best_path, best_time)

### USED FOR TESTING. PLEASE DO NOT CHANGE THIS FUNCTION.
def directed_dfs(digraph, start, end, restricted_colors):
    """
    Finds the shortest time path from start to end using a directed depth-first
    search. Minimize the total time and do not use the color lines in colors_not_used.

    Parameters:
        digraph: instance of Digraph
            The graph on which to carry out the search
        start: Node
            t-stop at which to start
        end: Node
            t-stop at which to end
        restricted_colors: list[string]
            Colors of lines not allowed in path

    Returns:
        The shortest-path from start to end, represented by
        a list of t stops (Nodes).

        If there exists no path that satisfies restricted_colors constraints, then raises a ValueError.
    """
    path = [[start], 0]  # begin at start node with 0 distance
    result = get_best_path(digraph, start, end, path, restricted_colors, 99999, None)
    
    if result is None:
        raise ValueError("No path from {} to {}".format(start, end))
    
    return result[0]


#UNCOMMENT THE FOLLOWING LINES TO DEBUG IF YOU WOULD LIKE TO    

#digr = load_map('t_map.txt')
#
#start = Node('central')
#end = Node('boylston')
#restricted_colors = ["green", "gray"]
#
#print(directed_dfs(digr, start, end, restricted_colors))


