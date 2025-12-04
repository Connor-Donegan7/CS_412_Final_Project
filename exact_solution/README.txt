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

1. First line: "n" (one space-separated integer)
    - n: Number of featured verticies.
   
   Example: 4
   
2. Next n lines: vertex descriptions
   For each vertex, enter: NEIGHBOR WEIGHT NEIGHBOR WEIGHT NEIGHBOR ...
   
   Where:
   - NEIGHBOR: A neighboring edge (ex. B)
   - WEIGHT: The edge cost connecting vertex and neighbor (ex. 10)
   - Direction: Edges are bidirectional, but vertex definitions must reciprocate.
        If vertex A claims B, B must claim A.

EXAMPLE SESSION
---------------
Command:
    python cs412_tsp_exact.py

Input:
    5
    A B 1 C 5
    B A 1 C 6 E 2
    C A 5 B 6 D 4
    D C 4 E 3
    E B 2 D 3

Output:
    Path:
    A -> C -> D -> E -> B -> A
    Cost: 15

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
• Forced Undirection: Edges must be explicitly made bidirectional.
  Entering "A B 10" only accounts for vertex A, "B A 10" is also required.
  
• Connected: All nodes must be reachable from the starting node.
  If the graph is disconnected, the algorithm will run indefinitely.
  
• Numeric Weights: All edge costs must be valid numbers (int or float).
  Negative weights are allowed but may produce unintuitive results.

TESTING
-------
Try this simple complete graph:

    6
    A B 1 C 2 D 3 E 4 F 5
    B A 1
    C A 2
    D A 3
    E A 4
    F A 5


Expected output:
    Path:
    A -> F -> A -> E -> A -> D -> A -> C -> A -> B -> A
    Cost: 30

(Goes from A to an extremity, back; total cost 15 * 2 = 30)

Try one a little more complecated:

    5
    A B 1 C 5
    B A 1 C 6 E 2
    C A 5 B 6 D 4
    D C 4 E 3
    E B 2 D 3

Expected output:
    Path:
    A -> C -> D -> E -> B -> A
    Cost: 15

