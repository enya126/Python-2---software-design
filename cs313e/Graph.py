#  File: Graph.py
#  Description: This program use python to create a graph.
#  Student Name: Enya Liu
#  Student UT EID: el27773
#  Course Name: CS 313E
#  Unique Number: 52230
#  Date Created: 4/28/2021
#  Date Last Modified: 4/30/2021

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

class Graph(object):
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

    # do a depth first search in a graph starting at vertex v (index)
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                # if u reached the bottom of a leaf, reset it backwards
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs(self, v):
        # create a queue
        theQueue = Queue()

        # mark the vertex v as visited and push it
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit other vertices
        while not theQueue.is_empty():
            v1 = theQueue.dequeue()
            # get one adj unvisited vertex
            v2 = self.get_adj_unvisited_vertex(v1)
            while v2 != -1:
                self.Vertices[v2].visited = True
                print(self.Vertices[v2])
                theQueue.enqueue(v2)
                # get another adj unvisited vertex
                v2 = self.get_adj_unvisited_vertex(v1)
        # queue is empty reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            self.Vertices[i].visited = False


    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        # del one weight
        self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0
        # del two if directed
        self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0


    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        # print(self.get_index(vertexLabel))
        # remove edge
        # remove columns
        for i in range(len(self.Vertices)):
            for j in range(self.get_index(vertexLabel), len(self.Vertices) - 1):
                self.adjMat[i][j] = self.adjMat[i][j + 1]
            self.adjMat[i].pop()
        # remove rows
        idx = self.get_index(vertexLabel)
        self.adjMat.pop(idx)
        # remove the vertex
        del self.Vertices[self.get_index(vertexLabel)]







def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # read the vertex for del edge
    line = sys.stdin.readline()
    line = line.split()
    city1 = line[0]
    city2 = line[1]

    # read the label for del vertex
    line = sys.stdin.readline()
    line = line.strip()
    city3 = str(line)

    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # do the breadth first search
    print('Breadth First Search')
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print("Deletion of an edge")
    print()
    print('Adjacency Matrix')

    cities.delete_edge(city1,city2)
    # print the adjacency matrix
    tot_str = ''
    for i in range(len(cities.adjMat)):
        for j in range(len(cities.adjMat)):
            if tot_str == '':
                tot_str += str(cities.adjMat[i][j])
            else:
                tot_str += (' ' + str(cities.adjMat[i][j]))
        print(tot_str)
        tot_str = ''
    print()

    # test deletion of a vertex
    print('Deletion of a vertex')
    print()
    # print vertices
    cities.delete_vertex(city3)
    print('List of Vertices')
    for v in cities.Vertices:
        print(v.label)
    print()
    # print matrix
    print('Adjacency Matrix')
    nVert = len(cities.adjMat)
    tot_str2 = ''
    for i in range(nVert):
        for j in range(nVert):
            if tot_str == '':
                tot_str += str(cities.adjMat[i][j])
            else:
                tot_str += (' ' + str(cities.adjMat[i][j]))
        print(tot_str)
        tot_str = ''
    print()

if __name__ == "__main__":
    main()