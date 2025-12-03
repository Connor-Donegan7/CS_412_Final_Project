#!/bin/bash

# run_nonopt_cases.sh
# Demonstrates a case where the greedy nearest-neighbor heuristic
# does NOT achieve the optimal TSP tour.

echo "==============================================="
echo "  TSP Greedy Heuristic - Suboptimal Case"
echo "==============================================="
echo ""

TEST_FILE="./test_cases/test_nonopt_greedy_fails.txt"
SCRIPT="./cs412_tsp_approx.py"

# Check if script exists
if [ ! -f "$SCRIPT" ]; then
    echo "Error: $SCRIPT not found!"
    exit 1
fi

# Check if test file exists
if [ ! -f "$TEST_FILE" ]; then
    echo "Error: $TEST_FILE not found!"
    exit 1
fi

echo "Test: Non-optimal Greedy Case"
echo "File: $TEST_FILE"
echo ""
echo "Optimal tour cost: 8"


if python "$SCRIPT" < "$TEST_FILE" > /tmp/nonopt_output.txt 2>&1; then
    echo "Output:"
    cat /tmp/nonopt_output.txt
    echo ""
    echo "Status: Test completed successfully"
else
    echo "Status: Error"
    cat /tmp/nonopt_output.txt
fi

echo ""
echo "==============================================="
