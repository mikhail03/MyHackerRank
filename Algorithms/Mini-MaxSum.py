"""
Completed by: Mikhail Bself.

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

Each integer is in the inclusive range .
Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation
"""
#!/bin/python

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
# put the sum of the array into a variable
    x = sum(arr)

# print both the minimum and maximum using the max and min funcation
# Built in max and min function uses the largest and smallest number respectively
# Use the long build in function to use 64 bit integers
    print (long(x)-(max(arr))), (long(x) -(min(arr)))

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())
    miniMaxSum(arr)
