from typing import List


def four_number_sum(array: List[int], target) -> List[List[int]]:
    # Brute force: 4 four loop to find all the possible combination O(n^4)
    # x, y, z, k = P (x + y) + know Q (z, k) => quadruplets
    # We don't want to double count [[x, y, z, k], [y, z, x, k]]
    #  |_ iterate left to right: the value is added twice
    #  |_ iterate from the perspective of each index
    # .  |_ ith left, right of ith. So that we don't double count i-th
    pairSums = {}
    quadruplets = []

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = target - currentSum
            # diff is the key of hashMap
            if diff in pairSums:
                for pair in pairSums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])

        # process from the left of i-th
        # we only add to memory (pairSums) at this stage
        # to avoid double couting the results
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in pairSums:
                pairSums[currentSum] = [[array[i], array[k]]]
            else:
                pairSums[currentSum].append([array[i], array[k]])

    return quadruplets


if __name__ == "__main__":
    print(four_number_sum(array=[7, 6, 4, -1, 1, 2], target=16))
