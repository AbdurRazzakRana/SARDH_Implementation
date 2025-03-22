from itertools import product
import copy

smaller_examples_3_nested = [[2, 2, 2], [2, 2, 3], [2, 3, 2], [2, 3, 3],[3, 2, 2],[3, 2, 3], [3, 3, 2], [3, 3, 3]]
# smaller_examples_2_nested = [[2,2], [2,3], [3,2], [3,3]]
smaller_examples_2_nested = [[2,2], [2,3], [3,2], [3,3], [2,4], [3,4],[4,2],[4,4]]
def generate_combinations(n, start=2, end=4):
    return list(product(range(start, end+1), repeat=n))

def create_smaller_loop_bounds(loop_refs):
    loop_bounds =[]
    for index, item in enumerate(loop_refs):
        if item.startswith('['):
            loop_count = int(item[1:])
            # print(loop_count)
            loop_bounds.append((loop_count, index))

    if len(loop_bounds) == 2:
        list_of_small_bounds = smaller_examples_2_nested
    else:
        list_of_small_bounds = smaller_examples_3_nested
    # list_of_small_bounds = generate_combinations(len(loop_bounds))
    list_of_smaller_problems = []
    for item in list_of_small_bounds:
        small_prob = copy.deepcopy(loop_refs)
        index = 0
        # print(item)
        for val in item:
            small_prob[loop_bounds[index][1]] = f'[{val}'
            index+=1
        # print(small_prob)
        list_of_smaller_problems.append(small_prob)
    # print(list_of_smaller_problems)
    return list_of_smaller_problems, loop_bounds, list_of_small_bounds
