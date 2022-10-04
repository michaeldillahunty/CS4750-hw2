from distutils.util import copydir_run_2to3
import json
import time
start = time.time()

# action costs
left = 1.0
right = 0.9
up = 0.8
down = 0.7
suck = 0.6

# class that has information about the nodes
class Node(object):
    row_loc = 0
    row_loc = 0
    cost = 0
    status = 0

    def __init__(self, row_loc, col_loc, cost, status):
        self.row_loc = row_loc
        self.col_loc = col_loc
        self.cost = cost
        self.status = status


if __name__ == '__main__':
    print('Iterative Deepening Search')
    input_file = open('cases.json')
    # case1 for instance 1 || case2 for instance 2
    # matricies = json.load(input_file)['case1']
    matricies = json.load(input_file)['case2']
    print(matricies)
    row_start = 0
    col_start = 0
    depth = 0

    row_num = 0
    col_num = 0

    for row in matricies: # loop through graph to find starting point 
        for col in row:
            if col == 2:
                col_start = col_num
                row_start = row_num
                matricies[row_num][col_num] = 0
            col_num += 1
        row_num += 1
        col_num = 0

    row_num = len(matricies) # set length of rooms by row
    col_num = len(matricies[0]) # set length of rooms by column
    fringe = [Node(row_start, col_start, 0, 0)]
    expansions = 1 # number of expansions
    expanded = 0 # number of expanded nodes
    generated = 0 # number of generated nodes

    while any(1 in matrix for matrix in matricies): # check for dirty rooms, if found continue into loop
        i = 0

        # loop to expand each fringe node and increase depth
        while i < expansions:
            curr_node = fringe.pop(0) # pop node from front of fringe
            expanded += 1
            print('Expanded Node: ' + '(' +str(curr_node.row_loc)+', '+str(curr_node.col_loc)+')')
            print('Cost: '+ str(curr_node.cost)) 
            print('Status: ' + str(curr_node.status))
            print("------------------------------------")

            if curr_node.status == 1: # if room is dirty
                matricies[curr_node.row_loc][curr_node.col_loc] = 0 # clean room
                for row in matricies:
                    print(row)
                if not any(1 in matrix for matrix in matricies): # else if all clean end and print results
                    end = time.time()
                    print('Expanded Nodes: ' + str(expanded))
                    print('Generated Nodes: ' + str(generated + expanded)) 
                    print('Depth Searched: ' + str(depth))
                    print('Execution Time: ' + str(end - start) + ' seconds')
                    exit(0)
                fringe.append(Node(curr_node.row_loc, curr_node.col_loc, curr_node.cost + suck, 0)) # create a 'suck' action node
            if curr_node.row_loc - 1 > -1: # add a 'up' action node
                fringe.append(Node(curr_node.row_loc - 1, curr_node.col_loc, curr_node.cost + up, matricies[curr_node.row_loc - 1][curr_node.col_loc]))
            if curr_node.col_loc - 1 > -1: # add a 'left' action node
                fringe.append(Node(curr_node.row_loc, curr_node.col_loc - 1, curr_node.cost + left, matricies[curr_node.row_loc][curr_node.col_loc - 1]))
            if curr_node.col_loc + 1 < col_num: # add a 'right' action node 
                fringe.append(Node(curr_node.row_loc, curr_node.col_loc + 1, curr_node.cost + right, matricies[curr_node.row_loc][curr_node.col_loc + 1]))
            if curr_node.row_loc + 1 < row_num: # add a 'down' action node 
                fringe.append(Node(curr_node.row_loc + 1, curr_node.col_loc, curr_node.cost + down, matricies[curr_node.row_loc + 1][curr_node.col_loc]))
            i = i+1 
        depth = depth + 1 # increase depth
        expansions = len(fringe) + 1 # how many nodes to expand next
        generated = generated + len(fringe) 
        fringe = [Node(row_start, col_start, 0, 0)] # clear fringe to reset nodes

    exit(1)