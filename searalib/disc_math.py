import math


def combinations(n, k):
    """
    Unordered, w / o repetitions
    From n choose k
    """
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def combinations_with_repetitions(n, k):
    """
    Unordered, w / repetitions
    Вспомни задачу со спичками, это просто распределение delimiters
    """
    return combinations(k + n - 1, n - 1)


def permutations(n, k):
    """
    Ordered, w / o repetitions
    K-permutations
    """
    return math.factorial(n) / math.factorial(n - k)


def tuples(n, k):
    """
    Ordered, w / repetitions
    """
    return n ** k


def probability(A, omega):
    return A / omega
