import csv

#This file creates a Hashtable class and loads all packages into it from the given .csv file
class HashTable:
    #Initializes the hashtable and creates 10 empty buckets.
    #O(N)
    def __init__(self, initial_capacity=10) :
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    #Adds an element to the hashtable with a given key and value. The key will be the package ID and the value will be all of the package information.
    #O(1)
    def add(self, key, value):
        bucket = key % len(self.table)
        self.table[bucket].append(value)
    #Searches the hashtable for a given key. Returns the value if found, otherwise returns None.
    #O(N)
    def get(self, key):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        for index in bucket_list:
            if index[0] == key:
                return index
        return None
#Loads the hashtable with all of the packages and package information from the given .csv file. The package ID is used as the key and the package information is used as the value. Returns a filled hashtable.
#O(N)
def load_packages():
    h=HashTable()
    with open('packagefile.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            package_ID = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_note = row[7]
            if "9:05" not in row[7]:
                status = "Hub"
            else:
                status = "Delayed on flight"
            truck = row[8]    
            total = [package_ID, address, city, state, zip_code, deadline, weight, special_note, truck, status]
            h.add(package_ID, total)
    return h

#Gives a filled hashtable for other files to import.
packages_table = load_packages()
