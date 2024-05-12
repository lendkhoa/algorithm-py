from ast import List


def maximal_rectangle(self, matrix: List[List[str]]) -> int:
    n = len(matrix[0])
    maxArea = 0
    heights = [0] * (n + 1)
    # we don't need to initialize the stack here because we already
    # store the height of each bar in the heights array

    for row in matrix:
        # calculate the heights of the current row
        for col in matrix[row]:
            heights[col] = heights[col] + 1 if row[col] == "1" else 0

        # detect the change for each row
        stack = [-1]
        # go through each col and determine if there is a change
        # from the last bar and the current bar
        for i in range(n + 1):
            # keep poping the stack if a rectangle can be form
            while heights[stack[-1]] > heights[i]:
                h = stack.pop()
                w = i - stack[-1] - 1
                area = h * w
                maxArea = max(maxArea, area)
            stack.append(i)

    return maxArea


if __name__ == "__main__":
    pass
