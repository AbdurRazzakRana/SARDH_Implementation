array_refs_total = [['j', 'i'], ['arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3', 'arr-3-0', 'brr-3', 'arr-3-1', 'arr-3-2', 'arr-3-3']]

array_references = ['arr-0-0', 'brr-0', 'arr-0-1', 'arr-0-2', 'arr-0-3', 'arr-0-4', 'arr-0-5', 'arr-1-0', 'brr-1', 'arr-1-1', 'arr-1-2', 'arr-1-3', 'arr-1-4', 'arr-1-5', 'arr-2-0', 'brr-2', 'arr-2-1', 'arr-2-2', 'arr-2-3', 'arr-2-4', 'arr-2-5', 'arr-3-0', 'brr-3', 'arr-3-1', 'arr-3-2', 'arr-3-3', 'arr-3-4', 'arr-3-5', 'arr-4-0', 'brr-4', 'arr-4-1', 'arr-4-2', 'arr-4-3', 'arr-4-4', 'arr-4-5']

const_refs = ['j', 'i']

array_references_prev = array_refs_total[1]
const_refs_prev = array_refs_total[0]

for item in const_refs:
    if item not in const_refs_prev:
        const_refs_prev.append(item)

const_vars = len(const_refs_prev)

rf = {}
array_refs_total = []
rf.setdefault(-1, 0)

i_max = 4
j_max = 4

possible_arrays = ['brr', 'arr']
max_array_rfs =[]
for item in reversed(array_references_prev):
    if not possible_arrays:
        break
    else:
        parts = item.split('-')
        if parts[0] in possible_arrays:
            if (len(parts) > 2):
                max_array_rfs.append([parts[0], int(parts[1]), int(parts[2])])
            elif(len(parts) > 1):
                max_array_rfs.append([parts[0], int(parts[1])])
            possible_arrays.remove(parts[0])

print(max_array_rfs)

