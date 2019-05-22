#import matplotlib.pyplot as ply
import random
import sys

# A very ugly monty hall simulation
# makes for a fun probability toy
#
#
# probably

def switch(total_rounds, num_gates):

    winning_rounds = 0 
    for i in range(total_rounds):
        
        # Set up the gates
        gates = ["goat"] * num_gates
        gates[random.randint(0,num_gates - 1)] = "car"

        # Contestant chooses randomly
        contestant_pick = random.randint(0,num_gates - 1)

        # Monty chooses, but can't choose the car, or the contestant's pick
        montys_pick = random.randint(0,2)
        while montys_pick == contestant_pick or gates[montys_pick] == "car":
            montys_pick = (montys_pick + 1) % num_gates

        # To switch the gate, we pick the next element in the list, but skip it if it was chosen by monty
        contestant_pick = (contestant_pick + 1) % num_gates
        while contestant_pick == montys_pick:
            contestant_pick = (contestant_pick + 1) % num_gates

        if(gates[contestant_pick] == "car"):
            #print("winner")
            winning_rounds += 1

        else:
            5+5
            #print(" - ")

    return winning_rounds        


def stay(total_rounds, num_gates):

    winning_rounds = 0
    for i in range(total_rounds):
        
        # Set up the gates
        gates = ["goat"] * num_gates
        gates[random.randint(0,num_gates - 1)] = "car"

        # Contestant chooses randomly
        contestant_pick = random.randint(0,num_gates - 1)

        # Monty's choice doesn't matter, so we check the original guess
        if(gates[contestant_pick] == "car"):
           #print("winner")
            winning_rounds += 1

        else:
            5+5
            #print(" - ")

    return winning_rounds      

def random_policy(total_rounds, num_gates):

    winning_rounds = 0
    for i in range(total_rounds):
        
        # Set up the gates
        gates = ["goat"] * num_gates
        gates[random.randint(0, num_gates - 1)] = "car"

        # Contestant chooses randomly
        contestant_pick = random.randint(0, num_gates - 1)

        # Monty chooses, but can't choose the car, or the contestant's pick
        montys_pick = random.randint(0, num_gates - 1)
        while montys_pick == contestant_pick or gates[montys_pick] == "car":
            montys_pick = (montys_pick + 1) % num_gates

        # To switch the gate, we pick the next element in the list, but skip it if it was chosen by monty.
        if random.choice((True, False)):
            contestant_pick = (contestant_pick + 1) % num_gates
            while contestant_pick == montys_pick:
                contestant_pick = (contestant_pick + 1) % num_gates

        if(gates[contestant_pick] == "car"):
           #print("winner")
            winning_rounds += 1

        else:
            5+5
            #print(" - ")

    return winning_rounds  


def main(args):

    # Get the desired switching policy from the user, default to random.
    if len(args) <= 1:
        user_input = int(input("1. Switch every time\n2. Stay every time\n3. Random choice every time.\n\n>"))
    else:
        user_input = args[1]

    # Get total rounds if specified, otherwise default to 1000
    if len(args) <= 2:
        total_rounds = 1000
    else:
        total_rounds = int(args[2])

    # Get number of gates, if specified
    if len(args) <= 3:
        num_gates = 3
    else:
        num_gates = int(args[3])    

    # Yeah, yeah, these shouldn't be positional, I know. Maybe I'll rework this.    

    # Use the user input to decide switching policy
    if user_input in ["switch", 1]:
        winning_rounds = switch(total_rounds, num_gates)

    elif user_input in ["stay", 2]:
        winning_rounds = stay(total_rounds, num_gates)

    else:   # default to random
        winning_rounds = random_policy(total_rounds, num_gates)
           

    print("\nThe contestant won", winning_rounds/total_rounds, "percent of the time.\n")
    
    # Let's get plotting
    #labels = "Wins", "Losses"
    #sizes  = [winning_rounds, total_rounds - winning_rounds]
    #colors = ["green", "red"]
    #explode = (.2, 0)
    #
    #plt.pie(sizes, explode=(.2, 0), labels = labels, colors=colors)
    #plt.axis("equal")
    #plt.show()

if __name__ == "__main__":
    main(sys.argv)