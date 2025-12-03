================================================================================
                    approx_solution - TSP Approximate Solver
================================================================================

OVERVIEW
--------
This folder contains `cs_412_approx.py`, a simple heuristic for solving the
Traveling Salesman Problem (TSP) using a nearest-neighbor greedy approach.
The solver takes an undirected, weighted graph as input and outputs:
  1. The total tour cost (sum of edge weights)
  2. The nodes in tour order (starting and ending at the same node)

REQUIREMENTS
------------
- Python 3.7 or later
- No external dependencies

RUNNING THE SCRIPT
------------------
From PowerShell or Command Prompt in the `approx_solution` directory:

    python cs_412_approx.py

The script will interactively prompt for input (see section below).

INPUT FORMAT
------------
The script uses interactive input with two stages:

1. First line: "n m" (two space-separated integers)
   - n: number of nodes in the graph
   - m: number of edges in the graph
   
   Example: 4 6
   
2. Next m lines: edge definitions
   For each edge, enter: NODE1 NODE2 WEIGHT
   
   Where:
   - NODE1, NODE2: Node identifiers (any string without spaces, e.g., A, B, city_1)
   - WEIGHT: Edge cost (integer or float, e.g., 10, 3.5)
   - Direction: Edges are bidirectional; entering "A B 10" also creates "B A 10"

EXAMPLE SESSION
---------------
Command:
    python cs_412_approx.py

Input:
    4 6
    A B 4
    B C 3
    C D 5
    A D 6
    A C 7
    B D 2

Output:
    18.0
    A B D C A

Explanation:
  - First output (18.0): Total cost of the tour
  - Second output (A B D C A): Nodes in visit order (starts and ends at A)

ALGORITHM
---------
The solver uses the Nearest Neighbor heuristic:

1. Start at an arbitrary node (the first node in the graph dictionary)
2. Repeat until all nodes are visited:
   a. Find the unvisited node with minimum edge weight from current node
   b. Move to that node
   c. Mark it as visited
3. Return to the starting node to complete the tour

This is a greedy, O(n²) approximation that does NOT guarantee an optimal tour,
but runs very quickly even for moderately large graphs.

OUTPUT FORMAT
-------------
Line 1: Total weight of the complete tour (sum of all edge costs)
Line 2: Space-separated list of nodes in tour order

Important: The tour CLOSES on itself (returns to the start node at the end).

ERROR HANDLING
--------------
Input Parsing Errors:
  • First line does not have exactly 2 integers
    → ValueError during input parsing
  
  • Edge line does not have exactly 3 fields
    → ValueError during input parsing
  
  • Weight is not a valid number
    → ValueError: "could not convert string to float"

Graph Structure Issues:
  • Missing edges: If an edge is referenced but doesn't exist in the graph
    → The algorithm will fail with ValueError when trying to look up edge weight
  
  • Self-loops: Allowed by the parser, but will cause issues if a node only
    connects to itself
  
  • Duplicate edges: If you enter "A B 10" twice, only the last one is kept
    (previous one is overwritten in the adjacency list)

GRAPH REQUIREMENTS
------------------
• Undirected: Edges are treated as bidirectional.
  Entering "A B 10" creates both A→B and B→A edges with the same weight.
  
• Connected: All nodes must be reachable from the starting node.
  If the graph is disconnected, the algorithm will still run but the tour
  will only visit nodes reachable from the start node.
  
• Numeric Weights: All edge costs must be valid numbers (int or float).
  Negative weights are allowed but may produce unintuitive results.

TESTING
-------
Try this minimal complete graph:

    2 1
    A B 10

Expected output:
    20.0
    A B A

(Starts at A, goes to B, returns to A; total cost 10 + 10 = 20)

Try a 4-node complete graph:

    4 6
    A B 1
    B C 1
    C D 1
    A D 1
    A C 10
    B D 10

Expected output:
    4.0
    A B C D A

(Greedy path: start at A, nearest is B (weight 1), then C (weight 1),
 then D (weight 1), then return to A (weight 1); total = 4)
