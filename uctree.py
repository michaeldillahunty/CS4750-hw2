import json
import time

start = time.time()

# cost of actions 
left = 1.0
right = 0.9
up = 0.8
down = 0.7
suck = 0.6


# node definition for keeping track of cost, cleanliness, and location of the node 
class Node(object):
    row_loc = 0
    col_loc = 0
    cost = 0
    status = 0

    def __init__(self, row_loc, col_loc, cost, status):
        self.row_loc = row_loc
        self.col_loc = col_loc
        self.cost = cost
        self.status = status


if __name__ == '__main__':

    print('Uniform Cost Tree')
    inputFile = open('cases.json')  #gets our cases from the json file 
    # case1 for instance 1 || case2 for instance 2
   #  matricies = json.load(inputFile)['case1']
    matricies = json.load(inputFile)['case2']

    # declarations 
    row_start = 0
    col_start = 0
    action_cost = 0

    row_num = 0
    col_num = 0

    # loop to find the given starting point in the matrix 
    for row in matricies:

        for col in row:

            if col == 2:   # if we have found our starting position 
                col_start = col_num
                row_start = row_num
                matricies[row_num][col_num] = 0
            col_num += 1
        row_num += 1
        col_num= 0

    # intialize our fringe node and size of room 
    fringe = [Node(row_start, col_start, 0, 0)]
    col_num = len(matricies[0])
    row_num = len(matricies)
    
    #declarations 
    curr_row = 0
    curr_col = 0
    expanded_nodes = 0

    # loop until the fringe is empty 
    while len(fringe) > 0:
        
        k = 1
        i = 0
        low = 0
        prev = fringe[0]
        for node in fringe:
            if node.cost < fringe[low].cost: #finds the cheapest node to expand next
                low = i
            prev = node
            i = i+1 
        curr_node = fringe.pop(low)
        expanded_nodes = expanded_nodes+1 


         # Prints informationa of node that is being visited 
        print('Expanded Node: ' + '(' + str(curr_node.row_loc+1) + ', '+ str(curr_node.col_loc+1) + ')') 
        print('Cost: ' + str(curr_node.cost))
        print('Status: ' + str(curr_node.status))

        #check if we have to suck and if we have to go suck another location
        if curr_node.status == 1:
            matricies[curr_node.row_loc][curr_node.col_loc] = 0
            for row in matricies:
                print(row)
            if not any(1 in matrix for matrix in matricies):
                end = time.time()
                print('Expanded Nodes: ' + str(expanded_nodes))
                print('Generated Nodes: ' + str(len(fringe) + expanded_nodes))
                print('Execution time: ' + str(end-start)+' seconds')
                exit(0)
            # suck operation 
            fringe.append(Node(curr_node.row_loc,curr_node.col_loc,curr_node.cost + suck,0))
            #down operation

        if curr_node.row_loc + 1 < row_num:
            fringe.append(Node(curr_node.row_loc+1,curr_node.col_loc,curr_node.cost + down,matricies[curr_node.row_loc + 1][curr_node.col_loc]))
        # up operation 
        if curr_node.row_loc - 1 > -1:
            fringe.append(Node(curr_node.row_loc - 1,curr_node.col_loc,curr_node.cost + up,matricies[curr_node.row_loc - 1][curr_node.col_loc]))
        
        # right operation 
        if curr_node.col_loc + 1 < col_num:
            fringe.append(Node(curr_node.row_loc,curr_node.col_loc + 1,curr_node.cost + right,matricies[curr_node.row_loc][curr_node.col_loc + 1]))
            
        # left operation
        if curr_node.col_loc - 1 > -1:
            fringe.append(Node(curr_node.row_loc,curr_node.col_loc - 1,curr_node.cost + left,matricies[curr_node.row_loc][curr_node.col_loc - 1]))

    exit(1)