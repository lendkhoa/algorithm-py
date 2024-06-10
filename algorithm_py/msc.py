from typing import List

def iterate_cyclic(arr: List[int], k: int) -> None:
    n = len(arr) - 1
    it = 0
    direction = -1
    while k > 0:
        if it == n or it == 0:
            direction *= -1
        k -= 1
        print(f'{arr[it]}: {arr[it]}')
        it += direction * 1


iterate_cyclic([1,2,3,4,5], 15)