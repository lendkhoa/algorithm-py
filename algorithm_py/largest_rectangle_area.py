class LargestRectangleArea:
    def largestRectArea(self, heights: List[Int]) -> int:
        maxArea = 0
        # We use stack here because it allows us to
        # process the trend in LIFO order
        memory = [] # Pair of index, height of the histogram

        for i, h in enumerate(heights):
            # Start processing when the trend changes (increasing -> decreasing)
            start = i
            while memory and memory[-1][1] > h:
                # The last bar with the tallest height
                index, heightOfLastBar = memory.pop()
                maxArea = max(maxArea, heightOfLastBar * (i - index))
                start = index
            memory.append(start, h)

        # Memory has the increasing bar
        for i, h in memory:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
