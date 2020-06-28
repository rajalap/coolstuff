graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.
found = False

def dfs(visited, graph, startNode, finishNode):
    if startNode == finishNode:
        found = True
        return
    if startNode not in visited:
        print (startNode)
        visited.add(startNode)
        for neighbour in graph[startNode]:
            dfs(visited, graph, neighbour, finishNode)

# Driver Code
dfs(visited, graph, 'A', 'F')
if found == False:
    print ("Could not find a path to", 'F')
else:
    print ("Found the path!")