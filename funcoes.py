from queue import Queue


graph = {
      "A" : ["B","C","D","F"],
      "B" : ["A","C","D"],
      "C" : ["A","B","E"],
      "D" : ["A","B","F","H"],
      "E" : ["C","G"],
      "F" : ["A","D","H","I"],
      "G" : ["E","I","H"],
      "H" : ["D","F","G"],
      "I" : ["F","G"]
 }
#
#visited = []
#queue = []

#def bfs(visited, graph, node):
 #   visited.append(node)
  #  queue.append(node)

   # while queue:
    #    m = queue.pop(0)
     #   print(m,end = " ")

      #  for neighbour in graph[m]:
       #     if neighbour not in visited:
        #        visited.append(neighbour)
         #       queue.append(neighbour)


def bfs(graph, inicial, final):
    visited = {}
    level = {}
    parent = {}
    bfs_transversal_output = []
    queue = Queue()

    for no in graph.keys():
        visited[no] = False
        parent[no] = None
        level[no] = -1
    s = inicial
    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        bfs_transversal_output.append(u)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u]+1
                queue.put(v)
    print("bfs",bfs_transversal_output)

    f = final
    path = []
    while f is not None:
        path.append(f)
        f = parent[f]
    path.reverse()
    print('menor caminho',path)
    return path
