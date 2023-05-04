import math


def water_jug_problem(m, n, d):
    """
    Solves the Water Jug Problem and returns the steps to measure d liters of water using two jugs with capacities
    of m and n liters, respectively, where d is less than n.

    :param m: the capacity of the first jug (in liters)
    :param n: the capacity of the second jug (in liters)
    :param d: the desired amount of water to measure (in liters)
    :return: the steps to measure d liters of water
    """

    if d % math.gcd(m, n) != 0 or d > n:
        return None

    # Initialize the state of the jugs
    jug_a = 0
    jug_b = 0
    steps = []

    # Keep pouring water between the jugs until we get d liters of water in one of them
    while jug_a != d and jug_b != d:
        # Fill jug A if it is empty
        if jug_a == 0:
            jug_a = m
            steps.append(f"Fill jug A ({m}L)")

        # Pour the water from jug A into jug B until jug B is full or jug A is empty
        while jug_b < n and jug_a > 0:
            amount = min(jug_a, n - jug_b)
            jug_a -= amount
            jug_b += amount
            steps.append(f"Pour {amount}L from jug A to jug B")

        # Empty jug B if it is full
        if jug_b == n:
            jug_b = 0
            steps.append("Empty jug B")

        # Repeat the process until we get d liters of water in one of the jugs
    return steps

solution = water_jug_problem(4,7,5)

for i in range(0,len(solution)):
    print(solution[i])
    

