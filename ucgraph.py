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
    col_loc = 0 
    cost = 0
    status = 0

    def __init__(self, row_loc, col_loc, cost, status):
        self.row_loc = row_loc
        self.col_loc = col_loc
        self.cost = cost
        self.status = status

# check if node is in closed list
def in_closed(row_closed, col_closed, list_closed):
    for node_closed in list_closed:
        if node_closed.row_loc == row_closed and node_closed.col_loc == col_closed:
            return True
    return False


if __name__ == '__main__':
    print('Uniform Cost Graph Search')
    # case1 for instance 1 || case2 for instance 2
    input_file = open('cases.json')
    matricies = json.load(input_file)['case1']
   #  matricies = json.load(input_file)['case2']
    row_start = 0 
    col_start = 0
    action_cost = 0

    row_num = 0
    col_num = 0

    # loop to find starting point
    for row in matricies:
        for col in row:
            if col == 2:
                col_start = col_num
                row_start = row_num
                matricies[row_num][col_num] = 0
            col_num += 1
        row_num += 1
        col_num = 0

    fringe = [Node(row_start, col_start, 0, 0)] # set room size, initial fringe node
    closed = []

    row_num = len(matricies)
    col_num = len(matricies[0])
    curr_row = 0
    curr_col = 0
    expanded = 0

    while len(fringe) > 0: # while the fringe is not empty
        i = 0
        lowest = 0 
        prev = fringe[0]
        for node in fringe: # find the lowest cost node
            if node.cost < fringe[lowest].cost:
                lowest = i
            prev = node
            i += 1
        curr_node = fringe.pop(lowest)
        closed.append(curr_node)
        expanded += 1

        print('Expanded Node: ' + '(' + str(curr_node.row_loc + 1)+ ','+ str(curr_node.col_loc + 1) +')')
        print('Cost: '  + str(curr_node.cost))
        print('Status: ' + str(curr_node.status))
        print("----------------------------")

        if curr_node.status == 1: # if current room is dirty 
            matricies[curr_node.row_loc][curr_node.col_loc] = 0 # clean the room 
            for row in matricies:
               print(row)
            if not any(1 in matrix for matrix in matricies): # if all rooms are clean, end and print information
               end = time.time()
               print('Expanded Nodes: ' + str(expanded))
               print('Generated Nodes: ' + str(len(fringe) + expanded))
               print('Execution Time: ' + str(end - start) + ' seconds')
               exit(0)
            # Add a node for the suck operation
            fringe.append(Node(curr_node.row_loc, curr_node.col_loc, curr_node.cost + suck, 0))
        if curr_node.row_loc + 1 < row_num and not in_closed(curr_node.row_loc + 1, curr_node.col_loc, closed): # if not in closed list, add down action node (lowest cost)
            fringe.append(Node(curr_node.row_loc + 1, curr_node.col_loc, curr_node.cost + down, matricies[curr_node.row_loc + 1][curr_node.col_loc]))
        if curr_node.row_loc - 1 > -1 and not in_closed(curr_node.row_loc - 1, curr_node.col_loc, closed): # if not in closed list, add up action node (second lowest cost)
            fringe.append(Node(curr_node.row_loc - 1, curr_node.col_loc, curr_node.cost + up, matricies[curr_node.row_loc - 1][curr_node.col_loc]))
        if curr_node.col_loc + 1 < col_num and not in_closed(curr_node.row_loc, curr_node.col_loc + 1, closed): # if not in closed list, add right action node (third lowest cost)
            fringe.append(Node(curr_node.row_loc, curr_node.col_loc + 1, curr_node.cost + right,matricies[curr_node.row_loc][curr_node.col_loc + 1]))
        if curr_node.col_loc - 1 > -1 and not in_closed(curr_node.row_loc, curr_node.col_loc - 1, closed): # if not in closed list, add left action node (highest cost)
            fringe.append(Node(curr_node.row_loc, curr_node.col_loc - 1, curr_node.cost + left, matricies[curr_node.row_loc][curr_node.col_loc - 1]))
    
    exit(1)