from datetime import datetime, timedelta
from distances import graph, nearest_neighbor
from hashtable import packages_table

#This files handles all of the loading of packages onto trucks and delivering of packages. Time is kept track of based on the distances between locations and the speed of 18mph of each truck.
first_time = datetime(2021, 5, 16, 8) #Time the first truck leaves the hub.
second_time = datetime(2021, 5, 16, 9, 5) #Time the second truck leaves the hub.
third_time = datetime(2021, 5, 16, 10) #Time the third truck leaves the hub.
graph.add_packages(packages_table) #Associates all packages in the hashtable to locations on the graph.
holder = graph.dict #Holds the location dictionary from the graph.

#Loads the first truck with all packages assigned to it. Reads from the dictionary list in the graph.
#O(N^2)
def load_first_truck():
    first_truck = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "1":
                first_truck.append(index)
    return first_truck
#Creates the route that the first truck will follow based on its assigned packages. It then sorts the route based on the nearest neighbor algorithm and returns the sorted list.
#The address of the hub is added to the end of this list as the truck must return to the hub for this driver to drive the third truck.
#O(N^2)
def first_truck_route():
    first_route = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "1":
                first_route.append(index[1])
    first_route = nearest_neighbor(first_route)
    first_route.append("4001 South 700 East")
    return first_route
#Loads the second truck with all packages assigned to it. Reads from the dictionary list in the graph.
#O(N^2)
def load_second_truck():
    second_truck = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "2":
                second_truck.append(index)
    return second_truck
#Creates the route that the second truck will follow based on its assigned packages. It then sorts the route based on the nearest neighbor algorithm and returns the sorted list.
#O(N^2)
def second_truck_route():
    second_route = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "2":
                second_route.append(index[1])
    second_route = nearest_neighbor(second_route)
    return second_route
#Loads the third truck with all packages assigned to it. Reads from the dictionary list in the graph.
#O(N^2)
def load_third_truck():
    third_truck = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "3":
                third_truck.append(index)
    return third_truck
#Creates the route that the third truck will follow based on its assigned packages. It then sorts the route based on the nearest neighbor algorithm and returns the sorted list.
#O(N^2)
def third_truck_route():
    third_route = []
    for index in holder:
        for index in graph.dict[index]:
            if index[8] == "3":
                third_route.append(index[1])
    third_route = nearest_neighbor(third_route)
    return third_route
#Allows the manipulation of time to pass based on the distance traveled and the speed of the truck. Distance and the current time are passed as parameters. The truck moves at a constant 18mph. 
#Timedelta is used to add the increase in time to the current time. The new time is then returned.
#O(1)
def add_time(distance, time):
    minutes = ((distance/18)*60)//1
    seconds = int(((distance/18)*60 - minutes)*60)
    time = time + timedelta(minutes=minutes, seconds=seconds)
    return time
#Delivers the packages and keeps track of time and distance traveled by all trucks. Takes in the user submitted time as parameters in hours, minutes, and seconds and simulates the delivering of packages up until the given time. Updates package status accordingly.
#At the end, the sum of the distance driven by each truck is printed to the console. No values are returned, but the hashtable is updated as each package is delivered. The full hashtable is then output to the user in the main function.
#O(N^2)
def deliver_packages(hours, minutes, seconds):
    time = datetime(2021, 5, 16, hour=hours, minute=minutes, second=seconds) #Time input by the user
    weight = graph.weight #The edge weights of the graph
    first_route = first_truck_route() #The sorted route the first truck will take
    second_route = second_truck_route() #The sorted route the second truck will take
    third_route = third_truck_route() #The sorted route the third truck will take
    first_truck = load_first_truck() #The list of all packages on the first truck
    second_truck = load_second_truck() #The list of all packages on the second truck
    third_truck = load_third_truck() #The list of all packages on the third truck
    time_holder = first_time #Holds the time as it passes. Initialized to the time the first truck leaves the hub
    distance_sum = 0 #The sum of the distance traveled by all trucks

    for index in first_truck:
        index[9] = "en route on truck 1"
    for index in range(0, len(first_route)-1):
        distance = weight[first_route[index], first_route[index+1]]
        distance_sum += distance
        new_time = add_time(distance, time_holder)
        time_holder = new_time
        if time < time_holder:
            break
        for i in first_truck:
            if first_route[index+1] == i[1]:
                i[9] = "Delivered by truck 1 at: " + str(time_holder)

    if time >= second_time:
        time_holder = second_time
        for index in second_truck:
            index[9] = "en route on truck 2"
        for index in range(0, len(second_route)-1):
            distance = weight[second_route[index], second_route[index+1]]
            distance_sum += distance
            new_time = add_time(distance, time_holder)
            time_holder = new_time
            if time < time_holder:
                break
            for i in second_truck:
                if second_route[index+1] == i[1]:
                    i[9] = "Delivered by truck 2 at: " + str(time_holder)

    if time >= third_time:
        time_holder = third_time
        for index in third_truck:
            index[9] = "en route on truck 3"
        for index in range(0, len(third_route)-1):
            distance = weight[third_route[index], third_route[index+1]]
            distance_sum += distance
            new_time = add_time(distance, time_holder)
            time_holder = new_time
            if time < time_holder:
                break
            for i in third_truck:
                if third_route[index+1] == i[1]:
                    i[9] = "Delivered by truck 3 at: " + str(time_holder)
    print("Total distance driven by trucks so far: " + str(round(distance_sum, 2)) + " miles.")
    
        

    
