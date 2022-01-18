#  File: TopoSort.py
#  Description: This program use python to do Topo sort.
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 5/2/2021
#  Date Last Modified: 5/3/2021

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine visited or not
    def was_visited(self):
        return self.visited

    # determine label of vertex
    def get_label(self):
        return self.label

    # str representation
    def __str__(self):
        return str(self.label)

class Graph (object):
  def __init__(self):
      self.Vertices = []
      self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex(self, label):
      nVert = len(self.Vertices)
      for i in range(nVert):
          if (label == (self.Vertices[i]).get_label()):
              return True
      return False

  # get the index from the vertex label
  def get_index(self, label):
      nVert = len(self.Vertices)
      for i in range(nVert):
          if (label == (self.Vertices[i]).get_label()):
              return i
      return -1

  # add a Vertex object with a given label to the graph
  def add_vertex(self, label):
      if (self.has_vertex(label)):
          return

      # add vertex to the list of vertices
      self.Vertices.append(Vertex(label))

      # add a new column in the adjacency matrix
      nVert = len(self.Vertices)
      for i in range(nVert - 1):
          (self.adjMat[i]).append(0)

      # add a new row for the new vertex
      new_row = []
      for i in range(nVert):
          new_row.append(0)
      self.adjMat.append(new_row)

  # add weighted directed edge to graph
  def add_directed_edge(self, start, finish, weight=1):
      self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge(self, start, finish, weight=1):
      self.adjMat[start][finish] = weight
      self.adjMat[finish][start] = weight

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight(self, fromVertexLabel, toVertexLabel):
      # weight = adjMat[start][finish]
      weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
      # if weight does not exist
      if weight == 0:
          return -1
      else:
          return weight

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors(self, vertexLabel):
      neighbors = []
      idx = self.get_index(vertexLabel)
      for i in range(len(self.Vertices)):
          # search edges that weight greater than 0
          if self.adjMat[idx][i] > 0:
              neighbors.append(self.Vertices[i])
      return neighbors

  # return an index to an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex(self, v):
      nVert = len(self.Vertices)
      for i in range(nVert):
          if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
              return i
      return -1

  # get a copy of the list of Vertex objects
  def get_vertices(self):
      copy_lst = []
      for i in self.Vertices:
          copy_lst.append(i)
      return copy_lst

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
      for v in self.Vertices:
          if self.has_cycle_helper(previous=None, vertex = v):
              return True
          # Reset the flags
          for i in range(len(self.Vertices)):
              self.Vertices[i].visited = False
      return False

  def has_cycle_helper(self, previous, vertex):
    # suggest dfs algorithm for has_cycle
    if vertex.was_visited() is True:
        return True
    # mark the vertex as visited
    vertex.visited = True
    neighbors = self.get_neighbors(vertex.label)

    if previous in neighbors:
        neighbors.remove(previous)
    if len(neighbors) == 0:
        return False

    # recursively go through all of the statement above
    for neighbor in neighbors:
        return self.has_cycle_helper(vertex, neighbor)

  # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    # modify bfs for toposort
    v_lst = []
    tot_lst = []
    # make a copy
    copy_graph = Graph()
    copy_graph.Vertices = self.Vertices
    copy_graph.adjMat = self.adjMat
    # check if there is a cycle or not
    if self.has_cycle():
        return []
    else:
        while len(copy_graph.Vertices) > 0:
            row = 0
            # clear v_lst
            v_lst = []
            # find the vertex with no indegree
            while row < len(copy_graph.Vertices):
                for j in range(len(copy_graph.Vertices)):
                    if copy_graph.adjMat[j][row] != 0:
                        row += 1
                        break
                # If the row has all zeros, then it is added to topo list
                if j == len(copy_graph.Vertices) - 1:
                    # sort vertices before put into lst
                    v_lst.append(copy_graph.Vertices[row].label)
                    # move to next row
                    row += 1
            # sort the same level vertices
            sorted(v_lst)
            # append all this level to the lst
            for i in v_lst:
                tot_lst.append(i)
                # delete all the appended vertices
                copy_graph.delete_vertex(i)



        return tot_lst

  # write a helper function to delete vertex and edge
  def delete_vertex (self, vertexLabel):
    idx = self.get_index(vertexLabel)
    for i in range(len(self.adjMat)):
      del(self.adjMat[i][idx])
    del(self.adjMat[idx])
    del(self.Vertices[idx])

def main():
  # create a Graph object
  theGraph = Graph()

  # read input
  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int(line)

  # read the vertices to the list of Vertices
  for i in range(num_vertices):
      line = sys.stdin.readline()
      city = line.strip()
      theGraph.add_vertex(city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int(line)

  # read each edge and place it in the adjacency matrix
  for i in range(num_edges):
      line = sys.stdin.readline()
      edge = line.strip()
      edge = edge.split()
      start = theGraph.get_index(edge[0])
      finish = theGraph.get_index(edge[1])

      theGraph.add_directed_edge(start, finish, weight=1)

  # test if a directed graph has a cycle
  if (theGraph.has_cycle()):
    print ("The Graph has a cycle.")
  else:
    print ("The Graph does not have a cycle.")

  # test topological sort
  if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print ("\nList of vertices after toposort")
    print (vertex_list)

main()