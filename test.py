# https://www.geeksforgeeks.org/topological-sorting/
# no cycle
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices # No. of vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def dfs(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*6
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                print(visited)
                self.dfs(i, visited, stack)
        
        return stack[::-1]

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print(g.graph)
    print("Following is a Topological Sort of the given graph")
 
    # Function Call
    print(g.topologicalSort())