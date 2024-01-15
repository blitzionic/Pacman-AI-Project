# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Resource: https://www.cs.rpi.edu/~xial/Teaching/2020SAI/slides/IntroAI_2.pdf
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    # the goal is state can be checked using isGoalState()
    path = []
    visited = set()
    # stack as fringe
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    while not stack.isEmpty():
        curr, path = stack.pop()
        if problem.isGoalState(curr):
            return path
        if curr in visited:
            continue    
        visited.add(curr)
        # if not, expand v, insert resulting nodes into fringe, mark s as visited
        # Returns successor states, the actions they require, and a cost of 1.
        successors = problem.getSuccessors(curr)
        for new_state, action, cost in successors:
            if new_state not in visited:
                new_path = path + [action]
                stack.push((new_state, new_path))
    return []
    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    """Never expand a node whose state has been visited
    Fringe can be maintained as a First-In-First-Out (FIFO)
    queue (class Queue in util.py)
    Maintain a set of visited states
    fringe := {node corresponding to initial state}
    loop:
    • if fringe empty, declare failure
    • choose and remove the top node v from fringe
    • check if v’s state s is a goal state; if so, declare success
    • if v’s state has been visited before, skip
    • if not, expand v, insert resulting nodes into fringe, mark s as visited"""

    path = []
    visited = set()
    # queue as fringe 
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    while not queue.isEmpty():
        curr, path = queue.pop()
        if problem.isGoalState(curr):
            return path
        if curr in visited:
            continue
        visited.add(curr)
        successors = problem.getSuccessors(curr)
        for new_state, action, cost in successors:
            if new_state not in visited:
                new_path = path + [action]
                queue.push((new_state, new_path))
    return []


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visited = set()
    # def push(self, item, priority):
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(), []), 0)

    while not pq.isEmpty():
        curr, path = pq.pop()
        if problem.isGoalState(curr):
            return path
        if curr in visited: 
            continue
        visited.add(curr)
        successors = problem.getSuccessors(curr)
        for new_state, action, c in successors:
            if new_state not in visited:
                cost = problem.getCostOfActions(path + [action])
                pq.push((new_state, path + [action]), cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """



    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visited = set()
    pq = util.PriorityQueue()
    pq.push((problem.getStartState(), []), 0)
    
    while not pq.isEmpty():
        curr, path = pq.pop()
        if problem.isGoalState(curr): 
            return path
        if curr in visited:
            continue
        visited.add(curr)
        successors = problem.getSuccessors(curr)
        for new_state, action, c in successors:
            # insert resulting nodes with f(v)=g(v)+h(v) to fringe
            gv = problem.getCostOfActions(path + [action])
            hv = heuristic(new_state, problem)
            pq.push((new_state, path + [action]), gv + hv)
    return []
            
            


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
