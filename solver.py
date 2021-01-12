"""
Solver.py solves the puzzle using A* Search
"""
import copy
import time

class Node:
    def __init__(self, board, parent, action, moves, accuracy):
        self.board = board
        self.parent = parent
        self.action = action
        self.moves = moves
        self.accuracy = accuracy

class PriorityQueue():
    def __init__(self):
        self.list = []
    def contains_board(self, board):
        for node in self.list:
            if node.board == board:
                return True
        return False
    def add(self, node):
        self.list.append(node)
    def empty(self):
        return len(self.list) < 1
    def remove(self):
        best_node = self.list[0]
        for test_node in self.list:
            if test_node.moves + test_node.accuracy < best_node.moves + best_node.accuracy:
                best_node = test_node
        self.list.remove(best_node)
        return best_node

def find_solution(starting_board):
    """
    Returns solution after applying A* Search
    """
    queue = PriorityQueue()
    node = Node(starting_board, None, None, 0, get_accuracy(starting_board))
    queue.add(node)
    explored = []
    while True:
        if queue.empty():
            print("No solution")
            return None

        node = queue.remove()
        explored.append(node.board)


        potential_actions = get_actions(node.board)

        for action in potential_actions:
            new_board = apply_action(node.board, action)

            if not queue.contains_board(new_board) and not new_board in explored:

                if is_terminal(new_board):
                    new_node = Node(new_board, node, action, node.moves+1, get_accuracy(new_board))
                    return get_solution(new_node)

                new_node = Node(new_board, node, action, node.moves+1, get_accuracy(new_board))
                queue.add(new_node)
            
            
            
        
def apply_action(board, action):
    """
    Returns the resulting board from an action on a board
    """
    new_board = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "0":
                new_board[i][j] = action
            if board[i][j] == action:
                new_board[i][j] = "0"
    return new_board

def get_accuracy(board):
    """
    A Heuristic which returns a point value of a board based on the location of each number
    Lower is better
    """
    score = 18

    columns = []
    for i in range(3):
        columns.append([])
    for i in range(3):
        for j in range(3):
            columns[j].append(board[i][j])

    for i in range(3):
        for j in range(3):
            number = (i*3) + j+1
            if number == 9:
                number = 0
            if str(number) in columns[j]:
                score -= 1
            if str(number) in board[i]:
                score -= 1

    return score




def get_solution(final_node):
    """
    Returns a list of actions made to get to the solution
    """
    solution = []
    node = final_node
    while node.action:
        solution.append(node.action)
        node = node.parent
    solution.reverse()
    return solution

def get_actions(board):
    """
    Returns all actions the AI can make
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "0":
                if i + 1 < 3:
                    actions.append(board[i+1][j])
                if i - 1 > -1:
                    actions.append(board[i-1][j])
                if j + 1 < 3:
                    actions.append(board[i][j+1])
                if j - 1 > -1:
                    actions.append(board[i][j-1])
                return actions


def is_terminal(board):
    """
    Determines if the board is a winning board or not
    """
    terminal_board = [['1', '2', '3'], ['4','5','6'],['7','8','0']]

    if board == terminal_board:
        return True
    else:
        return False




