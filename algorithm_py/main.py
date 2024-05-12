def num_of_bits(num: int) -> int:
    num_of_bits = 0
    while num:
        num_of_bits += num & 1
        num >>= 1
    return num_of_bits


print(num_of_bits(12323432))


def get_number_of_islands(binaryMatrix):
    count = 0
    for row in range(len(binaryMatrix)):
        for col in range(len(binaryMatrix[0])):
            if binaryMatrix[row][col] == 0:
                continue

            if binaryMatrix[row][col] == 1:
                count += 1
                # mark all the neighbor as 1
                neighbors = []

                left_is_land = (
                    True if col - 1 >= 0 and binaryMatrix[row][col - 1] == 1 else False
                )
                top_is_land = (
                    True if row - 1 >= 0 and binaryMatrix[row - 1][col] == 1 else False
                )
                right_is_land = (
                    True
                    if col + 1 < len(binaryMatrix[0])
                    and binaryMatrix[row][col + 1] == 1
                    else False
                )
                bottom_is_land = (
                    True
                    if row + 1 < len(binaryMatrix) and binaryMatrix[row + 1][col] == 1
                    else False
                )

                if left_is_land:
                    neighbors.append([row, col - 1])
                if right_is_land:
                    neighbors.append([row, col + 1])
                if top_is_land:
                    neighbors.append([row - 1, col])
                if bottom_is_land:
                    neighbors.append([row + 1, col])

                while neighbors:
                    current = neighbors.pop(0)
                    binaryMatrix[current[0]][current[1]] = 0
                    if (
                        current[1] - 1 >= 0
                        and binaryMatrix[current[0]][current[1] - 1] == 1
                    ):
                        neighbors.append([current[0], current[1] - 1])  # left
                    if (
                        current[1] + 1 < len(binaryMatrix[0])
                        and binaryMatrix[current[0]][current[1] + 1] == 1
                    ):
                        neighbors.append([current[0], current[1] + 1])  # right
                    if (
                        current[0] - 1 >= 0
                        and binaryMatrix[current[0] - 1][current[1]] == 1
                    ):
                        neighbors.append([current[0] - 1, current[1]])  # top
                    if (
                        current[0] + 1 < len(binaryMatrix)
                        and binaryMatrix[current[0] + 1][current[1]] == 1
                    ):
                        neighbors.append([current[0] + 1, current[1]])  # bottom

    return count


# map = [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]
# print(get_number_of_islands(map))
