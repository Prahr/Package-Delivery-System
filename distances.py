import csv

#This file creates a graph with addresses as the vertices and the miles between each vertex as the weight for the edges. The edges are undirected.
class Graph:
    #Initializes the graph with 2 dictionaries. One for the locations and the other for the weights of all edges.
    #O(1)
    def __init__(self):
        self.dict = {}
        self.weight = {}
    #Adds a vertex to the graph
    #O(1)
    def add_vertex(self, vertex):
        self.dict[vertex] = []
    #Adds an undirected edge to the graph between two vertices and assigns a weight to the edge. The weight is miles between the two locations (vertices).
    #O(1)
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.weight[(vertex_a, vertex_b)] = weight
    #Associates packages to each vertex. Assigns each package in the hashtable to a location (vertex).
    #O(N^2)  
    def add_packages(self, h):
        for bucket in h.table:
            for value in bucket:
                self.dict[value[1]].append(value)
#Creates the graph and fills it with vertices and edges based on the given .csv file. Each vertex is an address and the edges are the distances between each vertex.
#O(N^2)
def graph():
    new_graph = Graph()
    distances = []
    with open('distances.csv') as csvFile:
        readCSV = csv.reader(csvFile, delimiter=',')
        for row in readCSV:
            distances.append(row)
        for row in distances:
            new_graph.add_vertex(row[1])
            for i in range(2, len(row)):
                new_graph.add_undirected_edge(row[1], distances[i-2][1], float(row[i]))
                print(row[1], distances[i-2][1], float(row[i]))
    return new_graph

graph = graph() #Creates the graph and stores all location and distance information into it

#Nearest neighbor algorithm. Takes in a list of addresses as a parameter and finds the shortest path between given vertices. Since all routes must start at the hub, the result path is initialized to start from the hub's address.
#The algorithm first finds the closest package address to the hub. Then the closest package address to that next location until all of the given path is sorted. As the algorithm sorts, it removes already visted locations from the given path and adds them, in order, to the sorted list.
#Since some locations have multiple packages, if the shortest path is already in the sorted list it is not added to the sorted list and just removed from the given path.
#O(N^2)
def nearest_neighbor(path):
    weight = graph.weight
    nnResult = ["4001 South 700 East"]           #The list eventually returned by the algorithm. Since we start at the hub, that is the first value placed in the sorted list.

    while len(path) != 0:
        shortest = [0, "4001 South 700 East"]    #Initializes the shortest path to be the hub, since that is where we will always start
        for index in path:                       #Finds the shortest distance between the last visited location and all other unvisited locations
            travel = weight[nnResult[-1], index] #travel is the distance between the last visted location and a potential new location (index)
            if  travel != 0 and travel < shortest[0]: #Checks if the travel distance is the shortest distance locally possible of values checked so far. If it is, that is the new shortest path
                shortest = [travel, index]
            if shortest[0] == 0:          #Needed so the algorithm doesn't break on the first iteration. Sets initial values for comparison.
                shortest = [travel, index]
        if shortest[1] not in nnResult:   #If the shortest possible path location has not already been visited, add it to the sorted list
            nnResult.append(shortest[1])
        path.remove(shortest[1])          #Since this location has now been visted, remove it from the list.
    return nnResult 


