# This method will take a complete sequence and then convert into unique address of set and ordered vector

def calc_rd(item, ref_vector):
    sz = len(ref_vector)
    rd = 0
    found_at = sz-1
    for i in range(sz - 1, -1, -1):  # Start from the last index, end at -1, step -1
        if item == ref_vector[i]:
            found_at = i
            break
        else:
            rd += 1
    if rd != 0:
        ref_vector.append(ref_vector.pop(found_at))
    return rd, ref_vector



def create_set_n_vector_n_rf(final_sequence):
    # print("Here--------")
    # print(expanded_trace)
    ref_set = set()
    ref_vector = []
    ref_vector_for_in_order = []
    ref_rd = {}
    # print(final_sequence)
    for item in final_sequence:
        if item not in ref_set:
            ref_set.add(item)
            ref_vector.append(item)
            ref_vector_for_in_order.append(item)
        else:
            rd, ref_vector = calc_rd(item, ref_vector)
            if rd in ref_rd:
                ref_rd[rd] += 1
            else:
                ref_rd[rd] = 1
    # print(ref_rd)
    # print(ref_vector)
    return ref_set, ref_vector, ref_vector_for_in_order, ref_rd