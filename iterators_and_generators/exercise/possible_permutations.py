from itertools import permutations


def possible_permutations(nums):

    for result in permutations(nums):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]
