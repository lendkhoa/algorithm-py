from typing import List

"""
n tasks: n-primary and n-secondary
limit (number of hours)
Each day must schedule 1 primary task.
If has time under limit, then can schedule a 2nd task
limit >= 1st + 2nd task

limit = 7
primary = [4, 5, 2,4]
secondary = [5, 6, 3, 4]
"""

def getMaxTasks(limit: int, primary: List[int], secondary: List[int]) -> int:
    max_count = 0
    diff = [limit - i for i in primary]
    diff.sort()
    secondary.sort()
    while secondary and diff:
        if diff[-1] < secondary[-1]:
            secondary.pop() # can't schedule this secondary task
        else:
            max_count += 1
            secondary.pop()
            diff.pop()
    return max_count



def getMaxTasks_test1():
    assert getMaxTasks(7, [4, 5, 2, 4], [5, 6, 3, 4]) == 2

def testGetMaxTasks():
    getMaxTasks_test1()
    print("All tests PASSED!")

testGetMaxTasks()
