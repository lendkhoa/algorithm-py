class SpiralTraverse:
    def spiral_travere(matrix):
        result = []
        if not matrix:
            return result

        top = 0;
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) -  1

        while top <= bottom and left <= right:
            # Traverse the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse the right side
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse the bottom row
            if top <= bottom:
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse the top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
