"""
Given an array A of n objects with keys that takes one of four values, 
reorder the array so that all objects 
that have the same key appear together. Use O(1) additional space and O(n) time.
A = [
  { key: 0, value: 'a' },
  { key: 0, value: 'c' },
  { key: 0, value: 'h' },
  { key: 1, value: 'b' },
  { key: 1, value: 'e' },
  { key: 2, value: 'd' },
  { key: 2, value: 'g' },
  { key: 3, value: 'f' }
]
"""
def reorder(A):
    """
    Reorder the array A so that all objects with the same key appear together.
    
    Args:
        A (list): A list of dictionaries, where each dictionary has a 'key' and a 'value'.
    
    Returns:
        list: The reordered list of dictionaries.
    """
    # Create a dictionary to store the objects grouped by key
    groups = {}
    
    # Group the objects by key
    for obj in A:
        key = obj['key']
        if key not in groups:
            groups[key] = []
        groups[key].append(obj)
    
    # Reorder the objects
    reordered = []
    for key in sorted(groups.keys()):
        reordered.extend(groups[key])
    
    return reordered

# Example usage
A = [
    { 'key': 0, 'value': 'a' },
    { 'key': 0, 'value': 'c' },
    { 'key': 0, 'value': 'h' },
    { 'key': 1, 'value': 'b' },
    { 'key': 1, 'value': 'e' },
    { 'key': 2, 'value': 'd' },
    { 'key': 2, 'value': 'g' },
    { 'key': 3, 'value': 'f' }
]

"""
Given an array <1,2,9> as input. Implement plus on
"""
from typing import List
def plus_one(nums: List[int]) -> None:
  carry = 0
  for i in range(len(nums)-1,-1, -1):
    if i == len(nums)-1:
      nums[i] += 1
    else:
      nums[i] += carry
    if nums[i] >= 10:
      carry = 1
      nums[i] -= 10
    else:
      carry = 0
  if carry == 1:
    nums.insert(0, 1) 
	
  print(nums)
    
plus_one([1,2,9])   

 
 
 
 
