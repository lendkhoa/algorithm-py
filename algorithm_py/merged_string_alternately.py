class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            return helper(word1, word2)
        else:
            return helper(word2, word1)

    def helper(self, shorter: str, longer: str) -> str:
        merged = ''
        lastIndex = 0
        for i in range(0, len(shorter)):
            merged += shorter[i]
            merged += longer[i]
            lastIndex = i
        merged += longer[lastIndex, len(longer)]
        return merged

