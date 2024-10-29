"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking
 7 and 109, both and 7109 are prime. The sum of these four primes, 792 , represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import itertools
import math

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 1. Generate prime numbers to certain limit
# 2. Create pairs checking the pairs
# 3. Use a graph data structure to represent the primes as nodes and the concatenation relationships as edges.
# 4. Find a clique of size 5

def concatenate_primes(prime1, prime2):
    concat1 = int(str(prime2) + str(prime1))
    concat2 = int(str(prime1) + str(prime2))
    return is_prime(concat1) and is_prime(concat2)

def find_clique(graph, size):
    nodes = list(graph.keys())
    for combination in itertools.combinations(nodes, size):
        if all(concatenate_primes(u, v) for u, v in itertools.combinations(combination, 2)):
            return combination
    return None

def lowest_sum_of_five_primes(limit):
    primes = [i for i in range(2, limit) if is_prime(i)]
    graph = {prime: [] for prime in primes}

    # populate the graph
    for prime1 in primes:
        for prime2 in primes:
            if prime1 < prime2 and concatenate_primes(prime1, prime2):
                graph[prime1].append(prime2)

    result = find_clique(graph, 5)
    print(result)
    return sum(result)

print(lowest_sum_of_five_primes(1000))
