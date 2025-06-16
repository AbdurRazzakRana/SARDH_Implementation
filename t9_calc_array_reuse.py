from t0_separate_loop_blocks_from_refs import separate_loop_blocks_from_refs
def remove_duplicate_array_from_back_to_back_access(vec):
    
    # print(vec)
    current_list = []
    current_touple = []
    for i, temp in enumerate(vec):
        if vec[i].startswith('['):
            current_list = []
        elif vec[i] == ']':
            current_list = []
        elif "NESTEDLOOP" in vec[i]:
            current_list = []
        else:
            if 'arr' in vec[i]:
                if vec[i] not in current_list:
                    current_touple.append([vec[i], i])
                    current_list.append(vec[i])
                else:
                    # print("Delete")
                    for item in current_touple:
                        if item[0] == vec[i]:
                            del vec[item[1]]
                            item[1] = i
                            break
    # print(vec)
    return vec

def transform_nested_loops(tokens):
    result = []
    stack = []
    # loop_counter = 1

    def parse_block(index):
        # nonlocal loop_counter
        block = []
        while index < len(tokens):
            token = tokens[index]
            if token.startswith('['):
                # New nested block starts
                nested_index, nested_block = parse_block(index + 1)
                result.append(nested_block)  # Save the inner block
                # block.append(f'NESTEDLOOP{loop_counter}')
                block.append(f'NESTEDLOOP')
                # loop_counter += 1
                index = nested_index
            elif token == ']':
                block.append(']')
                return index + 1, [start_token] + block  # Return full block
            else:
                block.append(token)
                index += 1
        return index, block  # Should not hit here ideally

    index = 0
    while index < len(tokens):
        if tokens[index].startswith('['):
            start_token = tokens[index]
            index, parsed_block = parse_block(index + 1)
            result.append(parsed_block)
        else:
            index += 1

    return result[::-1]  # Reverse to get [3] at top

def get_unique_non_numeric_refs(data):
    def is_number(s):
        return s.isdigit()

    # Track last occurrence of cleaned non-numeric, non-empty items
    last_occurrence = {}
    for i, item in enumerate(data):
        cleaned = item.strip('[]')
        if cleaned and not cleaned.isdigit():
            last_occurrence[cleaned] = i

    # Build result list
    result = []
    for i, item in enumerate(data):
        cleaned = item.strip('[]')
        if cleaned and not cleaned.isdigit() and last_occurrence[cleaned] == i:
            result.append(cleaned)

    return result

def calc_array_reuse(separated_loop_blocks):
    array_reuse_rf = {}
    # step 1: only keep array variables and loop depth
    # ['[3', '[4', 'tmp_array-i-j', '[5', 'A_array-i-k', 'B_array-k-j', 'tmp_array-i-j', 'tmp_array-i-j', ']', ']', ']', '[3', '[4', 'D_array-i-j', 'D_array-i-j', '[5', 'tmp_array-i-k', 'C_array-k-j', 'D_array-i-j', 'D_array-i-j', ']', ']', ']']
    
    for index, value in enumerate(separated_loop_blocks):
        if value[0].startswith('['):
            loop_and_unique_refs = []
            each_loop_scn_updt = transform_nested_loops(value) # 1. Separate out each loop block
            for ind, value in enumerate(each_loop_scn_updt):
                value = remove_duplicate_array_from_back_to_back_access(value) # 2. remove repeating array reference that leads to a hit in near close
                unique_refs_per_loop = get_unique_non_numeric_refs(value) # 3. prepare a list of unique addresses in each loop/list
                loop_and_unique_refs.append([value, unique_refs_per_loop])
            # each_loop_scn_updt contains one nested loop, with NESTEDLOOP_coutn and removed the duplicate back to back reuse of array reference
            for i in range(len(loop_and_unique_refs) - 1, -1, -1):
                # loop_and_unique_refs[i][0] # each loop without duplicate array reference
                # loop_and_unique_refs[i][1] # unique references in an array
                print(loop_and_unique_refs[i][0])
                print(loop_and_unique_refs[i][1])
                print()
                mark_done_array_ref = []
                loopVar = ""
                for refInd, refVal in enumerate(loop_and_unique_refs[i][0]):
                    if refInd==1:
                        loopVar = refVal
                    if 'arr' in refVal and refVal not in mark_done_array_ref:
                        parts = refVal.split('-')
                        if loopVar not in parts:
                            mark_done_array_ref.append(refVal)
                            print("Case 1: When loop variable is NOT involved in the array reference. current execution * all upper bounds")
                            if "NESTEDLOOP" in loop_and_unique_refs[i][1]:
                                print("HANDLE NESTEDLOOP INIT SITUATION")
                            else:
                                reuse_of_that_refs = len(loop_and_unique_refs[i][1]) -1
                                occurance_of_that_refs = int(loop_and_unique_refs[i][0][0].strip("['"))
                                j = i
                                while j > 0:
                                    occurance_of_that_refs *= int(loop_and_unique_refs[j][0][0].strip("['"))
                                    j -= 1
                                # print(f"{reuse_of_that_refs}: {occurance_of_that_refs}")
                                if reuse_of_that_refs not in array_reuse_rf:
                                    array_reuse_rf[reuse_of_that_refs] = occurance_of_that_refs
                                else:
                                    array_reuse_rf[reuse_of_that_refs] += occurance_of_that_refs
                            # reuse_of_ref = 
    print(array_reuse_rf)
    return array_reuse_rf



vec_refs = ['retval', 'alpha', 'beta', 'i', '[3', 'i', 'j', '[4', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[5', 'k', 'alpha', 'i', 'k', 'A_array-i-k', 'k', 'j', 'B_array-k-j', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[3', 'i', 'j', '[4', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[5', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-k-j', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
separated_loop_blocks = separate_loop_blocks_from_refs(vec_refs)
calc_array_reuse(separated_loop_blocks)
# step 1: only keep array variables and loop depth
# ['[3', '[4', 'tmp_array-i-j', '[5', 'A_array-i-k', 'B_array-k-j', 'tmp_array-i-j', 'tmp_array-i-j', ']', ']', ']', '[3', '[4', 'D_array-i-j', 'D_array-i-j', '[5', 'tmp_array-i-k', 'C_array-k-j', 'D_array-i-j', 'D_array-i-j', ']', ']', ']']

# step 2: delete duplicates from the same level loop depth.
# ['[3', '[4', 'tmp_array-i-j', '[5', 'A_array-i-k', 'B_array-k-j', 'tmp_array-i-j', ']', ']', ']', '[3', '[4', 'D_array-i-j', '[5', 'tmp_array-i-k', 'C_array-k-j', 'D_array-i-j', ']', ']', ']']
