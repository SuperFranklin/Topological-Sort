import time
graph = {0: set([1,3,6]),
         1: set([2,3]),
         2: set([3,4,5]),
         3: set([4,5]),
         4: set([5]),
         5: set(),
         6: set([5])}

#start - start vertex, with outgoing degree equal to 0
def topoSort(graph):
    #number of in edges for every vertex in graph
    in_degree = dict()
    result = []
    queue = []
    for v in graph.keys():
        in_degree[v] = 0
    
    for key, value in graph.items():
        for v in value:
            in_degree[v]+=1        
    
    print(in_degree)
    
    for key, value in in_degree.items():
        if value ==0:
            queue.append(key)
    
    while queue:
        vertex = queue.pop()
        result.append(vertex)
        for child in graph[vertex]:
            if child not in result:
                in_degree[child]-=1
                if in_degree[child] == 0:
                    queue.append(child)
    return result
            
start = time.time()
for x in range (0,10000):
    r = topoSort(graph)
end = time.time()
print(end-start)
print(r)   
 