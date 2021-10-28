""" This script may recognise and reporta de current users logged in """

# function to get the events and dates
def get_event_date(event):
    return event.date

# function that recognises the current users logged in
def current_users(events):
    events.sort(key=get_event_date) # sort the events by date
    machines = {} # create a dictionary to store the machines and users logged in at each machine
    for event in events: # iterate through the events
        if event.machine not in machines:
            machines[event.machine] = set() # create a new entry in the dictionary for the machine
        if event.type == "login":
            machines[event.machine].add(event.user) # add the user to the set of users logged in at the machine
        elif event.type=="logout" and event.user not in machines[event.machine]:
            continue # if user appears in the logout event but not in the login event, ignore the event
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user) # remove the user from the set of users logged in at the machine
    return machines

# this function generates the report for the current users logged in
def generate_report(machines):
    for machine, users in machines.items(): # iterate through the machines and users logged in at each machine
        if len(users) > 0: # verify if there are users logged in at the machine
            user_list = ", ".join(users) # create a list of users logged in at the machine
            print("{}: {}".format(machine, user_list)) # print the machine and the list of users logged in at the machine

