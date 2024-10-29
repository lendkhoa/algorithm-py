"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""
from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    # Counter array to store the frequency of each task
    counter = [0] * 26
    max_val = 0
    max_count = 0

    # Traverse through tasks to calculate task frequencies
    for task in tasks:
        counter[ord(task) - ord('A')] += 1
        print(f'task: {task} {counter[ord(task) - ord("A")]}')
        if max_val == counter[ord(task) - ord('A')]:
            max_count += 1
            print(f'> max_count: {max_count} max_val: {max_val}')
        elif max_val < counter[ord(task) - ord('A')]:
            max_val = counter[ord(task) - ord('A')]
            max_count = 1
            print(f'>> max_count: {max_count} max_val: {max_val}')

    # Calculate empty slots, available tasks, and idles needed
    part_count = max_val - 1
    part_length = n - (max_count - 1)
    empty_slots = part_count * part_length
    available_tasks = len(tasks) - max_val * max_count
    idles = max(0, empty_slots - available_tasks)

    # Return the total time required
    return len(tasks) + idles

leastInterval(["A","A","A","B","B","B"], 2)
