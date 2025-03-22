from difflib import SequenceMatcher
import copy

def gen_2J_same_level_list(array_rfs_clean_up, given_loop_bound_j):
    #comparing two same level list and find the newly added items for 1 increse (2-2 to 2-3)
    list22 = array_rfs_clean_up[0]
    list23 = array_rfs_clean_up[1]
    new_items = [(i, val) for i, val in enumerate(list23) if val not in list22]

    half_length = len(new_items) // 2

    half_len_22 = len(list22)/2
    list_of_first_half_items_to_insert = []
    list_of_second_half_items_to_insert = []
    for i in range(half_length):
        index, value = new_items[i]
        # print(f"Index: {index}, Value: {value}")
        parts_var = value.split('-')
        count = int(half_len_22) -1
        # print(count)
        part1 = -1
        part2 = -2
        final_part = []
        while count >= 0:
            parts_origin = list22[count].split('-')
            if parts_var[0] == parts_origin[0]:
                final_part.append(parts_var[0])
                if parts_var[1] == parts_origin[1]:
                    part1 = int(parts_var[1])
                if len(parts_origin) >2 and len(parts_var) > 2:
                    part2 +=1
                    if parts_var[2] == parts_origin[2]:
                        part2 = int(parts_origin[2])
                break
            count -= 1
        if part1 >= 0:
            final_part.append(part1)
        else:
            final_part.append('x')
        if part2 == -1:
            final_part.append('x')
        elif part2 >=0:
            final_part.append(part2)
        # print(final_part)
        list_of_first_half_items_to_insert.append(final_part)

    for i in range(half_length, len(new_items)):
        index, value = new_items[i]
        # print(f"Index: {index}, Value: {value}")
        parts_var = value.split('-')
        count = len(list22) -1
        # print(count)
        part1 = -1
        part2 = -2
        final_part = []
        while count >= int(half_len_22):
            parts_origin = list22[count].split('-')
            # print(parts_var)
            # print(parts_origin)
            if parts_var[0] == parts_origin[0]:
                final_part.append(parts_var[0])
                if parts_var[1] == parts_origin[1]:
                    part1 = int(parts_var[1])
                if len(parts_origin) >2 and len(parts_var) > 2:
                    part2 +=1
                    if parts_var[2] == parts_origin[2]:
                        part2 = int(parts_origin[2])
                break
            count -= 1
        if part1 >= 0:
            final_part.append(part1)
        else:
            final_part.append('x')
        if part2 == -1:
            final_part.append('x')
        elif part2 >=0:
            final_part.append(part2)
        # print(final_part)
        list_of_second_half_items_to_insert.append(final_part)

    half = len(list22) // 2
    list221 = list22[:half]
    list222 = []
    list223 = list22[half:]
    list224 = []

    for i in range(2, given_loop_bound_j):
        for item in list_of_first_half_items_to_insert:
            deep_value = copy.deepcopy(item)
            for index, part in enumerate(deep_value):
                if part == 'x':
                    deep_value[index] = str(i)
            list222.append('-'.join(str(p) for p in deep_value))

        for item in list_of_second_half_items_to_insert:
            deep_value = copy.deepcopy(item)
            for index, part in enumerate(deep_value):
                if part == 'x':
                    deep_value[index] = str(i)
            list224.append('-'.join(str(p) for p in deep_value))
        
    list_2N = list221 + list222 + list223 + list224
    return list_2N
def gen_IJ_from_2N_list(list_2N, given_loop_bound_i):
    half = len(list_2N) // 2
    row_1 = list_2N[:half]
    row_2 = list_2N[half:]

    row_temp = []
    for index, value in enumerate(row_1):
        parts_1 = value.split('-')
        parts_2 = row_2[index].split('-')

        if(len(parts_1) == 2):
            final_part = []
            final_part.append(parts_1[0])
            if(parts_1[1] == parts_2[1]):
                final_part.append(parts_2[1])
            else:
                final_part.append('x')
            row_temp.append(final_part)

        elif(len(parts_1) == 3):
            final_part = []
            final_part.append(parts_1[0])
            if(parts_1[1] == parts_2[1]):
                final_part.append(parts_2[1])
            else:
                final_part.append('x')
            
            if(parts_1[2] == parts_2[2]):
                final_part.append(parts_2[2])
            else:
                final_part.append('x')
            row_temp.append(final_part)

    # print(row_temp)

    list_IJ  = list_2N

    for i in range(2, given_loop_bound_i):
        for item in row_temp:
            deep_value = copy.deepcopy(item)
            for index, part in enumerate(deep_value):
                if part == 'x':
                    deep_value[index] = str(i)
            list_IJ.append('-'.join(str(p) for p in deep_value))
    return list_IJ

def array_lookup_table(array_rfs_one_loop, given_loop_bound_i, given_loop_bound_j):
    # array_rfs_one_loop = [['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-1-0', 'brr-1', 'arr-1-1'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-2-0', 'brr-2', 'arr-2-1'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-3-0', 'brr-3', 'arr-3-1'], ['i', 'j', 'arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3', 'arr-3-0', 'brr-3', 'arr-3-1', 'arr-3-2', 'arr-3-3']]
    # list_of_small_bounds = [[2,2], [2,3], [3,2], [3,3], [2,4], [3,4],[4,2],[4,4]]
    # given_loop_bound_i = 4
    # given_loop_bound_j = 4
    array_rfs_clean_up = [[item for item in sublist if 'rr' in item] for sublist in array_rfs_one_loop]
    
    
    non_array_consts_nested = [[item for item in sublist if 'rr' not in item] for sublist in array_rfs_one_loop]
    non_array_consts = list(set(item for sublist in non_array_consts_nested for item in sublist))

    list_2J = gen_2J_same_level_list(array_rfs_clean_up, given_loop_bound_j)
    list_IJ = gen_IJ_from_2N_list(list_2J, given_loop_bound_i)

    # print(list_IJ)
    return list_IJ, non_array_consts
