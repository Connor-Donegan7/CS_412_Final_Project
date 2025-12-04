#!/bin/bash

# run_test_cases.sh
# Runs cs_412_approx.py on all test cases in the test_cases folder

echo "==============================================="
echo "  TSP Approximate Solver - Test Suite"
echo "==============================================="
echo ""

TEST_DIR="./test_cases"
SCRIPT="./cs412_tsp_exact.py"

# Check if script exists
if [ ! -f "$SCRIPT" ]; then
    echo "Error: $SCRIPT not found!"
    exit 1
fi

# Check if test directory exists
if [ ! -d "$TEST_DIR" ]; then
    echo "Error: $TEST_DIR directory not found!"
    exit 1
fi

TEST_COUNT=0
PASS_COUNT=0

# Run all test cases
for test_file in "$TEST_DIR"/test_*.txt; do
    if [ -f "$test_file" ]; then
        TEST_COUNT=$((TEST_COUNT + 1))
        TEST_NAME=$(basename "$test_file" .txt)
        
        echo "-------------------------------------------"
        echo "Test: $TEST_NAME"
        echo "Input file: $test_file"
        echo ""
        
        # Run the test !!! test_long.txt will run for longer than 20 minutes !!!
        if python "$SCRIPT" < "$test_file" > /tmp/test_output.txt 2>&1; then
            PASS_COUNT=$((PASS_COUNT + 1))
            echo "Status: PASS"
            echo ""
            echo "Output:"
            cat /tmp/test_output.txt
        else
            echo "Status: FAIL"
            cat /tmp/test_output.txt
        fi
        echo ""
    fi
done

echo "==============================================="
echo "Summary: $PASS_COUNT / $TEST_COUNT tests passed"
echo "==============================================="
