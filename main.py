from hashtable import packages_table
from packages import deliver_packages

#The entire program runs at a space-time and big-O of O(N^2)

#Takes input from user to output all package's status at the given time
selection = input("Type the time in a HH:MM:SS format to view status of all packages at that time.\nOr type 0 to exit: ")

#Passes the user input to the deliver_packages function. Packages are delivered up until the time input by the user.
#The entire hashtable containing all package's status at the input time is then output to the user. Input errors are also handled.
#O(N)
while selection != "0":
    try:
        (hours, minutes, seconds) = selection.split(':')
        if int(hours) >= 8:
            deliver_packages(int(hours), int(minutes), int(seconds))
            for i in range(1, 41):
                print(packages_table.get(i))
            exit()
        else:                        #If a time before 08:00:00 is given, no trucks have left the hub, so the hashtable with all packages still at the hub is output
            for i in range(1, 41):
                print(packages_table.get(i))
            exit()
    except ValueError: #Catches invalid inputs
        print("Input must be a time in the format of HH:MM:SS")
        selection = input("Type the time in a HH:MM:SS format to view status of all packages at that time.\nOr type 0 to exit: ")
exit()
