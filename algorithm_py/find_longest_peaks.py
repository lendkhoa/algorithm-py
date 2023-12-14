# Longest peak
# Given an array of integers
# a peak is defined as adjacent numbers that are strictly increasing
# until they reach the tip, at which point they become strictly decreasing

# Approach
# Find the peaks
# - A number that is strictly larger than its neighbors
# Comparing the peaks
# - keeping a local max

class LongestPeak:
    def findLongestPeak(array):
        longestPeakLength = 0
        i = 1
        while i < len(array) - 1:
            isPeak = array[i-1] < array[i] and array[i] > array[i+1]
            if not isPeak:
                i += 1
                continue
            # we found the peak
            # expand it all the way to the left
            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1
            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1

            currentPeakLength = rightIdx - leftIdx - 1
            longestPeakLength = max(longestPeakLength, currentPeakLength)
            i = rightIdx

        return longestPeakLength
