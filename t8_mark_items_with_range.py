
def findBound(loop_bound_map, var):
    value = loop_bound_map.get(var)
    return value

def mark_items_with_range_structure(vec_refs):
    
    structure = {
        "variables": set(),
        "arrays": []
    }

    loop_bound_map = {
    }

    for index, item in enumerate(vec_refs):
        if item.startswith('['):
            loop_bound_map[vec_refs[index+1]] = item[1:]
        elif ']' not in item:
            if 'rr' not in item:
                structure["variables"].add(item)
            else:
                # structure["arrays"].add(item)
                parts = item.split('-')
                if len(parts) == 3:
                    # 2d array
                    name = parts[0]
                    start2 = int(findBound(loop_bound_map, parts[1]))-1
                    print(item)
                    print(loop_bound_map)
                    print(parts)
                    print(findBound(loop_bound_map, parts[2]))
                    end2 = int(findBound(loop_bound_map, parts[2]))-1
                    array_2d = {"name": name, "start1": 0, "end1": 0, "start2": start2, "end2": end2}
                    structure["arrays"].append(array_2d)

                if len(parts) == 2:
                    name = parts[0]
                    # start = int(findBound(loop_bound_map, parts[1]))-1
                    end = int(findBound(loop_bound_map, parts[1]))-1
                    array_1d = {"name": name, "start": 0, "end": end}
                    structure["arrays"].append(array_1d)

    return structure