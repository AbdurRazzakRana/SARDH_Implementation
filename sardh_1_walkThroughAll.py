from t0_separate_loop_blocks_from_refs import separate_loop_blocks_from_refs
from t1_create_smaller_loop_bounds import create_smaller_loop_bounds
from t2_expand_loop_from_annotated_trace import expend_loop_form_annotated_trace
from t3_create_setn_vector_n_rf import create_set_n_vector_n_rf
from t4_unresolved_refs_solve import unresolved_refs_solve
from t5_equation_n_predict_actual_bound import predict_2_nested, predict_3_nested
from t6_array_lookup_table import array_lookup_table
from t7_calc_array_reference_rd import calc_array_reference_rd
from t8_mark_items_with_range import mark_items_with_range_structure
from t9_calc_array_reuse import calc_array_reuse
from t10_calc_position_wise_array_index import calc_position_wise_tree_based, print_loopnode

import time
import math
import json

def add_rd_to_rf(final_rf, rd, refs):
    if new_array_refs not in final_rf:
        final_rf[rd] = refs
    else:
        final_rf[rd] += refs

# 1 = completely static prediction
# 2 = set an avg to the later arrays
# 3 = generating the array sequence
mood = 1
start_time = time.time()

# vec_refs = ['retval', 'i', '[100', 'i', 'j', '[200', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[300', 'i', 'j', '[400', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
# vec_refs = ['retval', 'alpha', 'beta', 'i', '[3', 'i', 'j', '[4', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[5', 'k', 'alpha', 'i', 'k', 'A_array-i-k', 'k', 'j', 'B_array-j-k', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[3', 'i', 'j', '[4', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[5', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-j-k', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
# vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', '[16', 'i', 'j', '[18', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[22', 'k', 'alpha', 'i', 'k', 'A_array-i-j', 'k', 'j', 'B_array-k-j', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[16', 'i', 'j', '[24', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[18', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-k-j', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
# vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', '[40', 'i', 'j', '[50', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[70', 'k', 'alpha', 'i', 'k', 'A_array-i-j', 'k', 'j', 'B_array-k-j', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[40', 'i', 'j', '[80', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[50', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-k-j', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
# vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', '[180', 'i', 'j', '[190', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[210', 'k', 'alpha', 'i', 'k', 'A_array-i-j', 'k', 'j', 'B_array-k-j', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[180', 'i', 'j', '[220', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[190', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-k-j', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
# vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', '[300', 'i', 'j', '[320', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[400', 'k', 'alpha', 'i', 'k', 'A_array-i-j', 'k', 'j', 'B_array-k-j', 'i', 'j', 'tmp_array-i-j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[300', 'i', 'j', '[420', 'j', 'beta', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', '[320', 'k', 'i', 'k', 'tmp_array-i-k', 'k', 'j', 'C_array-k-j', 'i', 'j', 'D_array-i-j', 'D_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', 
            '[40', 'i', 'ni', 'j', '[50', 'j', 'nj', 'i', 'j', 'tmp-i-j', 'k', '[70', 'k', 'nk', 'alpha', 'i', 'k', 'A-i-k', 'k', 'j', 'B-k-j', 'i', 'j', 'tmp-i-j', 'tmp-i-j', 'k', 'k', ']', 'k', 'nk', 'j', 'j', ']', 'j', 'nj', 'i', 'i', ']', 'i', 'ni', 'i', 
            '[40', 'i', 'ni', 'j', '[80', 'j', 'nl', 'beta', 'i', 'j', 'D-i-j', 'D-i-j', 'k', '[50', 'k', 'nj', 'i', 'k', 'tmp-i-k', 'k', 'j', 'C-k-j', 'i', 'j', 'D-i-j', 'D-i-j', 'k', 'k', ']', 'k', 'nj', 'j', 'j', ']', 'j', 'nl', 'i', 'i', ']', 'i', 'ni']
# 3mm
# vec_refs = ['retval', 'ni', 'nj', 'nk', 'nl', 'i', '[40', 'i', 'j', '[50', 'j', 'i', 'j', 'E_array-i-j', 'k', '[70', 'k', 'i', 'k', 'A_array-i-k', 'k', 'j', 'B_array-k-j', 'i', 'j', 'E_array-i-j', 'E_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[50', 'i', 'j', '[80', 'j', 'i', 'j', 'F_array-i-j', 'k', '[80', 'k', 'i', 'k', 'C_array-i-k', 'k', 'j', 'D_array-k-j', 'i', 'j', 'F_array-i-j', 'F_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[40', 'i', 'j', '[80', 'j', 'i', 'j', 'G_array-i-j', 'k', '[50', 'k', 'i', 'k', 'E_array-i-k', 'k', 'j', 'F_array-k-j', 'i', 'j', 'G_array-i-j', 'G_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'retval']


# vec_refs = ['i', '[10', 'i', 'j',
#          '[20', 'j', 'i', 'j', "'T-i-j'", 'k',
#              '[30', 'k', "'alpha'", 'i', 'k', "'A-i-k'", 'k', 'j', "'B-j-k'", 'i', 'j', "'T-i-j'", "'T-i-j'", 'k', 'k', ']',
#          'k', 'j', 'j', ']',
#         'j', 'i', 'i', ']', 'i']

# vec_refs = ['retval', 'argc.addr', 'argv.addr', 'ni', 'nj', 'nk', 'nl', 'i', '[10', 'i', 'j', '[20', 'j', 'i', 'j', 'tmp-i-j', 'k', '[30', 'k', 'alpha', 'i', 'k', 'A-i-k', 'k', 'j', 'B-k-j', 'i', 'j', 'tmp-i-j', 'tmp-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']

# atax
# vec_refs = ['retval', 'i', '[40', 'i', 'j', '[50', 'j', 'i', 'j', 'tmp_array-i-j', 'k', '[70', 'k', 'i', 'j', 'tmp_array-i-j', 'i', 'k', 'A_array-i-k', 'i', 'k', 'x_array-i-k', 'i', 'j', 'tmp_array-i-j', 'k', 'k', ']', 'k', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'retval']

# bicg
# vec_refs =['retval', 'i', '[50', 'i', 'i', 'q_array-i', 'j', '[70', 'j', 'j', 's_array-j', 'i', 'r_array-i', 'i', 'j', 'A_array-i-j', 'j', 's_array-j', 'i', 'q_array-i', 'i', 'j', 'A_array-i-j', 'j', 'p_array-j', 'i', 'q_array-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'retval']

#mvt
# vec_refs =['retval', 'i', '[80', 'i', 'j', '[80', 'j', 'i', 'x1_array-i', 'i', 'j', 'A_array-i-j', 'j', 'y_1_array-j', 'i', 'x1_array-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[80', 'i', 'j', '[80', 'j', 'i', 'x2_array-i', 'j', 'i', 'A_array-j-i', 'j', 'y_2_array-j', 'i', 'x_array-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'retval']

final_rf = {}
knowledge_structure = {
        "variables": set(),
        "arrays": []
    }
isFirstLoop=True
# part2: array reference resolve.
array_refs_total = []
final_rf.setdefault(-1, 0)
separated_loop_blocks = separate_loop_blocks_from_refs(vec_refs)
# print(separated_loop_blocks)
regular_refs_non_array = []
# pred_rf = {}
for item in separated_loop_blocks:
    # print("Razzak")
    # print(item)
    if item[0].startswith('['):
        # print(final_rf)
        rps_small_probs = []
        smaller_problems, loop_bounds, list_of_small_bounds = create_smaller_loop_bounds(item)
        key_dict = {}

        # part2: array reference resolve.
        array_rfs_one_loop = []
        # print(smaller_problems)
        for small_prob in smaller_problems:
            unresolved_refs = []
            rf = {}
            expanded_trace = expend_loop_form_annotated_trace(small_prob)

            exp_trace_set, exp_trace_vector, exp_trace_in_order_merge_up, exp_rd = create_set_n_vector_n_rf(expanded_trace)

            for key, value in exp_rd.items():
                if key in rf:
                    rf[key] += value  
                else:
                    rf[key] = value 
            unresolved_refs.append([exp_trace_in_order_merge_up, exp_trace_vector])
            rf_unres, cold_miss = unresolved_refs_solve(unresolved_refs)
            array_rfs_one_loop.append(cold_miss)
            for key, value in rf_unres.items():
                if key in rf:
                    rf[key] += value
                else:
                    rf[key] = value

            # rf[-1] = len(cold_miss)
            rf[-1] = 0
            sorted_items = sorted(rf.items())
            # print(sorted_items)
            sorted_dict_str = "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"
            rps_small_probs.append(sorted_dict_str)
            # print(sorted_dict_str)


        
            values_dict = eval(sorted_dict_str.strip())
            
            # print(values_dict)
            
            # Loop through each key-value pair in the dictionary
            for key, value in values_dict.items():
                # Add the value to the corresponding list for each key
                if key not in key_dict:
                    key_dict[key] = []
                key_dict[key].append(value)

        if len(loop_bounds) == 2:
            pred_rf = predict_2_nested(key_dict=key_dict, i_tot=loop_bounds[0][0]-2, j_tot=loop_bounds[1][0]-2)
            # print(pred_rf)
            # print("2 nested loop")
        elif len(loop_bounds) == 3:
            pred_rf = predict_3_nested(key_dict=key_dict, i_tot=loop_bounds[0][0]-2, j_tot=loop_bounds[1][0]-2, k_tot=loop_bounds[2][0]-2)
            # print(pred_rf)
            # print("3 nested loop")
        else:
            pred_rf = {}
        
        for key, value in pred_rf.items():
            if key in final_rf:
                final_rf[key] += value
            else:
                final_rf[key] = value
        if mood == 3:
            array_references, const_refs = array_lookup_table(array_rfs_one_loop, loop_bounds[0][0], loop_bounds[1][0])
            
            if not array_refs_total:
                # print("first loop adding up all the references")
                array_refs_total.append(const_refs)
                array_refs_total.append(array_references)
                array_refs_total.append(set(array_references))
                # print(array_refs_total)
            else:
                array_rf, array_refs_total[0],array_refs_total[1], array_refs_total[2] = calc_array_reference_rd(array_refs_total, array_references, const_refs)
                #as the array prediction is already counted from the estimation, adds all the newly discovered rds and deduct from the cold misses
                count_resolved_array_rfs = 0
                for key, value in array_rf.items():
                    if key in final_rf:
                        final_rf[key] += value
                    else:
                        final_rf[key] = value
                    count_resolved_array_rfs += value
                final_rf[-1] -= count_resolved_array_rfs  
                # print(f"did nothing with:{array_rf[-1]}")
        elif mood == 2:
            # print("Hello")
            # print(item)
            if isFirstLoop:
                knowledge_structure_prev = mark_items_with_range_structure(item)
                isFirstLoop = False
                # print(knowledge_structure_prev)
            else:
                knowledge_structure2 = mark_items_with_range_structure(item)
                # print("--------MERGING LEFT--------")
                processed_array = []
                for key, value in knowledge_structure2.items():
                    if 'variables' in key:
                        for constInd, constVal in enumerate(value):
                            final_rf[constInd] +=1
                            final_rf[-1] -=1
                    if 'arrays' in key:
                        const_variables = len(knowledge_structure2["variables"])
                        predicted_rd = 0
                        if isinstance(value, list):
                            for item2 in value:
                                # This loop run through the Knowledge strcuture
                                # Item2 picks a an array structure each time
                                array_current = item2
                                array_name_key, array_name_value = list(item2.items())[0]
                                if array_name_value in processed_array:
                                    continue
                                else:
                                    processed_array.append(array_name_value)
                                # print("Final Array before processing array: ")
                                # print(final_rf)
                                # print(item2)
                                array_block_prev = next((item for item in knowledge_structure_prev['arrays'] if item['name'] == array_name_value), None)
                                # print("Found Block: ", array_block_prev)
                                if array_block_prev is not None:
                                    if len(array_current) == 5 and len(array_block_prev) == 5:
                                        curr_end_ind_1 = int(array_current['start2'])
                                        curr_end_ind_2 = int(array_current['end2'])
                                        prev_end_ind_1 = int(array_block_prev['start2'])
                                        prev_end_ind_2 = int(array_block_prev['end2'])
                                        # print(curr_end_ind_1, "-", curr_end_ind_2, "-", prev_end_ind_1, "-", prev_end_ind_2)
                                        if curr_end_ind_1 > prev_end_ind_1 and curr_end_ind_2 > prev_end_ind_2:
                                            curr_ref= (curr_end_ind_1+1) * (curr_end_ind_2 + 1)
                                            prev_ref = (prev_end_ind_1+1) * (prev_end_ind_2 + 1)
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_ref-prev_ref)
                                            final_rf[-1] -=prev_ref
                                            predicted_rd += prev_ref
                                            array_block_prev['start2'] = str(curr_end_ind_1)
                                            array_block_prev['end2'] = str(curr_end_ind_2)
                                        # write the only i is bigger
                                        elif curr_end_ind_1 > prev_end_ind_1:
                                            curr_ref= (curr_end_ind_1+1) * (curr_end_ind_2 + 1)
                                            prev_ref = (prev_end_ind_1+1) * (curr_end_ind_2 + 1)
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_ref-prev_ref)
                                            final_rf[-1] -=prev_ref
                                            predicted_rd += prev_ref
                                            array_block_prev['start2'] = str(curr_end_ind_1)
                                        # write the only j is bigger
                                        elif curr_end_ind_2 > prev_end_ind_2:
                                            curr_ref= (curr_end_ind_1+1) * (curr_end_ind_2 + 1)
                                            prev_ref = (curr_end_ind_1+1) * (prev_end_ind_2 + 1)
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_ref-prev_ref)
                                            final_rf[-1] -=prev_ref
                                            predicted_rd += prev_ref
                                            # array_block_prev['start2'] = str(curr_end_ind_1)
                                            array_block_prev['end2'] = str(curr_end_ind_2)
                                        # None of i and j is bigger
                                        else:
                                            curr_ref= (curr_end_ind_1+1) * (curr_end_ind_2 + 1)
                                            prev_ref = (prev_end_ind_1+1) * (prev_end_ind_2 + 1)
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_ref-prev_ref)
                                            final_rf[-1] -=curr_ref
                                            predicted_rd += curr_ref
                                        
                                    elif len(array_current) == 3 and len(array_block_prev) == 3:
                                        # print("1d array")
                                        curr_end_ind = int(array_current['end'])
                                        prev_end_ind = int(array_block_prev['end'])
                                        # print(curr_end_ind, "-", prev_end_ind)
                                        if curr_end_ind > prev_end_ind:
                                            prev_ref = prev_end_ind + 1
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_end_ind-prev_end_ind)
                                            final_rf[-1] -=prev_ref
                                            predicted_rd += prev_ref
                                            array_block_prev['end'] = str(curr_end_ind)
                                        else:
                                            prev_ref = curr_end_ind + 1
                                            # print("Used Reference: ", prev_ref)
                                            # print("New Reference: ", curr_end_ind-prev_end_ind)
                                            final_rf[-1] -=prev_ref
                                            predicted_rd += prev_ref
                                else:
                                    # print("completely new array: add to the knowledge")
                                    knowledge_structure_prev['arrays'].append(item2)
                        else:
                            print(f"  {value}")
                        # print("array rd: ", const_variables)
                        # if predicted_rd in final_rf:
                        #     final_rf[predicted_rd + const_variables] += predicted_rd
                        # else:
                        #     final_rf[predicted_rd + const_variables] = predicted_rd
                # print(knowledge_structure2)
            # print("Observe the updates")
            # print(knowledge_structure_prev)
    else:
        for singleRef in item:
            if singleRef not in regular_refs_non_array:
                final_rf[-1] += 1
                regular_refs_non_array.append(singleRef)

end_time = time.time()


# print(f'Before we start calc array: {final_rf}')

# array_rf = calc_array_reuse(separated_loop_blocks)
# print("Here")
reuse_from_same_loop_block = {}
root_nodes = []
for item in separated_loop_blocks:
    print(item)
    if item[0].startswith('['):
        root = calc_position_wise_tree_based(item, reuse_from_same_loop_block)
        print("output from Tree based calc: ")
        print(reuse_from_same_loop_block)
        root_nodes.append(root)

# print(final_rf)
# Add the same loop block reusse to the main grid. Adding the output of position wise tree based reuse distance
for key, value in reuse_from_same_loop_block.items():
    if key in final_rf:
        final_rf[key] += value
    else:
        final_rf[key] = value


# All the root nodes are stores, now run through all the loop nodes and resolve -1
array_used_under_in_blocks = []
const_refs_in_blocks = []
new_array_refs = 0
for root in root_nodes:
    print_loopnode(root)
    for item in root.array_used_below:
        # print(item)
        item = [item[0]] + [root.loop_used_below_with_bounds.get(x, x) for x in item[1:]]
        # print(item)
        # is_array_already_introduced = next((item[0] == arr[0] for arr in array_used_under_in_blocks), None)
        is_array_already_introduced = next((arr for arr in array_used_under_in_blocks if arr[0] == item[0]), None)
        if is_array_already_introduced:
            print(f"-------DO ARRAY MERGING FOR------{is_array_already_introduced}")
            # both smaller in the later array item -> no new reference, all reuse
            if item[1] <= is_array_already_introduced[1] and item[2] <= is_array_already_introduced[2]:
                add_rd_to_rf(final_rf, new_array_refs, item[1] * item[2])

            elif item[1] > is_array_already_introduced[1] and item[2] > is_array_already_introduced[2]:
                add_rd_to_rf(final_rf, new_array_refs, is_array_already_introduced[1] * is_array_already_introduced[2])
                new_array_refs += (item[1] - is_array_already_introduced[1]) * (item[2] - is_array_already_introduced[2])
                is_array_already_introduced[1] = item[1]
                is_array_already_introduced[2] = item[2]
            
            elif item[1] > is_array_already_introduced[1]:
                add_rd_to_rf(final_rf, new_array_refs, is_array_already_introduced[1] * item[2])
                new_array_refs += (item[1] - is_array_already_introduced[1]) * item[2]
                is_array_already_introduced[1] = item[1]

            elif item[2] > is_array_already_introduced[2]:
                add_rd_to_rf(final_rf, new_array_refs, item[1] * is_array_already_introduced[2])
                new_array_refs += item[1] * (item[2] - is_array_already_introduced[2])
                is_array_already_introduced[2] = item[2]

        else:
            new_array_refs += math.prod(item[1:])
            array_used_under_in_blocks.append(item)
        
    for const in root.unique_const_under_this_loop:
        if const not in const_refs_in_blocks:
            const_refs_in_blocks.append(const)

final_rf[-1] += new_array_refs + len(const_refs_in_blocks)




total_references = 0
for key, value in final_rf.items():
    if value < 0:
        final_rf[key] *= -1
        value =  final_rf[key]
    total_references += value

print("Final RP:")

final_rf = dict(sorted(final_rf.items())) 
print(final_rf)

print(f"Total Reference Estimated: {total_references}")

print(f"This Model RF Prediction time taken: {end_time-start_time}")

# Save as one-line dictionary format
with open("sardh_1_out_1_static_rf.txt", "w") as file:
    file.write(str(final_rf))