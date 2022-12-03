from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.v = vertices
    self.graph = defaultdict(list)


  def add_edge(self, v, w):
    self.graph[v].append(w)
    self.graph[w].append(v)


  def remove_edge(self, v, w):
    for index, key in enumerate(self.graph[v]):
      if key == w:
        self.graph[v].pop(index)
    
    for index, key in enumerate(self.graph[w]):
      if key == v:
        self.graph[w].pop(index)


  def print_euler_tour(self):
    v = 0
    for i in range(self.v):
      if len(self.graph[i]) % 2 != 0:
        v = i
        break
    
    self.print_euler_util(v)


  def print_euler_util(self, v):
    for w in self.graph[v]:
      if self.is_valid_next_edge(v, w):
        #print(f"{v}-{w}")
        self.remove_edge(v, w)
        self.print_euler_util(w)


  def is_valid_next_edge(self, v, w):
    if len(self.graph[v]) == 1:
      return True
    else:
      visited = [False]*(self.v)
      count1 = self.dfs_count(v, visited)

      self.remove_edge(v, w)
      visited = [False]*(self.v)
      count2 = self.dfs_count(v, visited)

      self.add_edge(v, w)

      return False if count1 > count2 else True


  def dfs_count(self, v, visited):
    count = 1
    visited[v] = True

    for w in self.graph[v]:
      if visited[w] == False:
        count = count + self.dfs_count(w, visited)
    
    return count


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_euler_tour()
