from ast import List


class Cube:
    def __init__(self, x, y, z, value=None):
        self.x = x
        self.y = y
        self.z = z
        self.value = value


def build_larger_cube(x_prime, y_prime, z_prime, n) -> List[Cube]:
    smaller_cubes = []

    cube_root_n = round(n ** (1 / 3))
    for i in range(cube_root_n):
        for j in range(cube_root_n):
            for k in range(cube_root_n):
                if len(smaller_cubes) < n:  # Ensure we only create n cubes
                    x = i * (x_prime / cube_root_n)
                    y = j * (y_prime / cube_root_n)
                    z = k * (z_prime / cube_root_n)

                    smaller_cubes.append(Cube(x, y, z))
                else:
                    break  # Stop if we've already placed n cubes

    return smaller_cubes


if __name__ == "__main__":
    # Example usage
    x_prime, y_prime, z_prime = 9, 9, 9  # Dimensions of the larger cube
    n = 27
    larger_cube = build_larger_cube(x_prime, y_prime, z_prime, n)

    # Print positions of the smaller cubes
    for id, value in enumerate(larger_cube):
        cube = larger_cube[id]
        print(f"Smaller Cube Position: x={cube.x}, y={cube.y}, z={cube.z}")
