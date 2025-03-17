from t3_create_setn_vector_n_rf import calc_rd
def unresolved_refs_solve(unresolved_list):
    sz = len(unresolved_list)
    rd = 0
    found_at = sz-1
    ref_rd = {}
    

    for i in range(sz - 1, -1, -1):  # Start from the last index, end at -1, step -1
        if i != sz -1:
            prev_list = unresolved_list[i][0]
            # print(prev_list)
            mainStreamListOnly = False
            if unresolved_list[i][1]:
                most_recent_access = unresolved_list[i][1]
                # print(most_recent_access)
                
            else:
                most_recent_access = prev_list
                mainStreamListOnly = True
            
            list_to_match = unresolved_list[i+1][0]
            # print(list_to_match)

            for item in list_to_match:
                if item not in most_recent_access:
                    most_recent_access.append(item)
                    if not mainStreamListOnly:
                        prev_list.append(item)
                else:
                    rd, most_recent_access = calc_rd(item, most_recent_access)
                    if rd in ref_rd:
                        ref_rd[rd] += 1
                    else:
                        ref_rd[rd] = 1
            unresolved_list[i][0] = prev_list
    return ref_rd, unresolved_list[0][0]