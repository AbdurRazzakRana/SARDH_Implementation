def calc_array_reference_rd(array_refs_total, array_references, const_refs):


# array_refs_total = [['j', 'i'], ['arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3', 'arr-3-0', 'brr-3', 'arr-3-1', 'arr-3-2', 'arr-3-3']]
# array_references = ['arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-0-4', 'arr-0-5', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-1-4', 'arr-1-5', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3', 'arr-2-4', 'arr-2-5', 'arr-3-0', 'brr-3', 'arr-3-1', 'arr-3-2', 'arr-3-3', 'arr-3-4', 'arr-3-5', 'arr-4-0', 'brr-4', 'arr-4-1', 'arr-4-2', 'arr-4-3', 'arr-4-4', 'arr-4-5']

# const_refs = ['j', 'i']

    const_refs_prev = array_refs_total[0]
    array_references_prev = array_refs_total[1]
    unique_Set = array_refs_total[2]

    for item in const_refs:
        if item not in const_refs_prev:
            const_refs_prev.append(item)

    const_vars = len(const_refs_prev)

    rf = {}
    rf.setdefault(-1, 0)

    # unique_Set = set(array_references_prev)
    cold_misses = 0
    for item in array_references:
        if item in unique_Set:
            seen = set()
            for ref in reversed(array_references_prev):
                if ref == item:
                    break
                else:
                    seen.add(ref)
            rd = len(seen)

            if rd+const_vars in rf:
                rf[rd+const_vars] += 1
            else:
                rf[rd+const_vars] = 1
            array_references_prev.remove(item)
            array_references_prev.append(item)
            # print(array_references_prev)
        else:
            cold_misses+=1
            unique_Set.add(item)
            array_references_prev.append(item)
    rf[-1] +=cold_misses
    # print(rf)
    return rf, const_vars, array_references_prev, unique_Set

