

graph = {
      "A" : ["B","C"],
      "B" : ["A","C","D"],
      "C" : ["A","B","E"],
      "D" : ["A","B","F"],
      "E" : ["C","G"],
      "F" : ["D","H"],
      "G" : ["E","I","H"],
      "H" : ["G","F"],
      "I" : ["G"]
 }

#
visited = []
queue = [] 

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m,end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

