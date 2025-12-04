================================================================================
                    exact_solution - TSP Approximate Solver
================================================================================

OVERVIEW
--------
This folder pertains to "cs412_tsp_exact.py". The program finds the correct
answer to the traveling salesman problem for a given graph, via backtracking.

The program takes an undirected, weighted graph, and produces the following:

1. The nodes which should be traversed (in order)
2. The total cost of the traversal.

WHY THIS IS IMPORTANT
---------------------
- People put things up, place them down, and do it all over again.
    From unloading a dishwasher, to flying passengers around the world (airline route planning),
    we see instances of this problem all the time.

REQUIREMENTS
------------
- Python 3.7 or later
- No external dependencies

RUNNING THE SCRIPT
------------------
From PowerShell or Command Prompt in the `exact_solution` directory:

    python cs412_tsp_exact.py

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
    python cs412_tsp_exact.py

Input:
    5 6
    A B 1
    A C 5
    B C 6
    B E 2
    E D 3
    C D 4


Output:
    15.0000
    A C D E B A

Explanation:
  - First output (A -> C -> D -> E -> B -> A): Order of complete traversal.
  - Second output (15): Cost of traversal.

ALGORITHM
---------
This problem uses a brute-force approach

1. Start at an arbitrary node (the first node in the graph dictionary).
2. Traverse blindly, checking for full vertex inclusion with every addition.
3. Keep a running best cost for found solutions AND the best solution so far.
    - Use the above best cost for memoization.

Note:
    This version is implemented using a stack and iteration. 

This solution guarantees a correct solution but runs in O(n!) time. This can make
usage tedious for large or highly-connected graphs (see test_long.txt)

OUTPUT FORMAT
-------------
Line 1: Order of the tour (order could vary and still be valid).
Line 2: Cost of tour.

Important: The tour CLOSES on itself (returns to the start node at the end).

ERROR HANDLING
--------------
Input Parsing Errors:
  • First line does not have an Integer
    → ValueError during input parsing
  
  • Edge line does not have exactly 3 fields
    → ValueError during traversal
  
  • Weight is not a valid number
    → ValueError: "could not convert string to float"

Graph Structure Issues:
  • Missing edges: If an edge is referenced but doesn't exist in the graph
    → The algorithm will fail with ValueError when trying to look up edge weight

GRAPH REQUIREMENTS
------------------
• Undirected: Edges are treated as bidirectional.
  Entering "A B 10" creates both A→B and B→A edges with the same weight.
  
• Connected: All nodes must be reachable from the starting node.
  If the graph is disconnected, the algorithm will run indefinitely.
  
• Numeric Weights: All edge costs must be valid numbers (int or float).
  Negative weights are allowed but may produce unintuitive results.

TESTING
-------
Try this simple complete graph:

    6 5
    A B 1
    A C 2
    A D 3
    A E 4
    A F 5



Expected output:
    30.0000
    A F A E A D A C A B A

(Goes from A to an extremity, back; total cost 15 * 2 = 30)

Try one a little more complecated:
    5 6
    A B 1
    A C 5
    B C 6
    B E 2
    E D 3
    C D 4

Expected output:
    15.0000
    A C D E B A

