import numpy as np
import random

def trial(parent_a, parent_b):
    n = 20

    point_1 = random.randint(1, 19)
    point_2 = point_1 + random.randint(1, 20 - point_1)

    kid_a = random.sample(parent_a, 20)
    kid_b = random.sample(parent_b, 20)

    kid_a[point_1 : point_2] = parent_b[point_1 : point_2]
    kid_b[point_1 : point_2] = parent_a[point_1 : point_2]

    string_a = parent_b[point_1 : point_2]
    string_b = parent_a[point_1 : point_2]

    t_1 = point_2
    t_2 = point_2

    for i in range(20):
        if t_1 >= 20:
            t_1 = t_1 % 20

        if parent_a[i] in string_a:
            pass
        else:
            kid_a[t_1] = parent_a[i]
            t_1 = t_1 + 1

        if t_2 >= 20:
            t_2 = t_2 % 20

        if parent_b[i] in string_b:
            pass
        else:
            kid_b[t_2] = parent_b[i]
            t_2 = t_2 + 1

    return kid_a, kid_b

if __name__ == "__main__":
    n = 20

    nums = range(n)

    parent_a = random.sample(nums, n)
    parent_b = random.sample(nums, n)

    for i in range(1000):
        ohh_1, ohh_2 = trial(parent_a, parent_b)

    print(ohh_1, ohh_2)