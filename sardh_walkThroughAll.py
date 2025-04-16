from t0_separate_loop_blocks_from_refs import separate_loop_blocks_from_refs
from t1_create_smaller_loop_bounds import create_smaller_loop_bounds
from t2_expand_loop_from_annotated_trace import expend_loop_form_annotated_trace
from t3_create_setn_vector_n_rf import create_set_n_vector_n_rf
from t4_unresolved_refs_solve import unresolved_refs_solve
from t5_equation_n_predict_actual_bound import predict_2_nested, predict_3_nested
from t6_array_lookup_table import array_lookup_table
from t7_calc_array_reference_rd import calc_array_reference_rd
from t8_mark_items_with_range import mark_items_with_range_structure

import time

# 1 = completely static prediction
# 2 = set an avg to the later arrays
# 3 = generating the array sequence
mood = 2
start_time = time.time()

vec_refs = ['retval', 'i', '[100', 'i', 'j', '[200', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[300', 'i', 'j', '[400', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
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
print(separated_loop_blocks)
for item in separated_loop_blocks:
    if item[0].startswith('['):
        # print(item)
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

            rf[-1] = len(cold_miss)
            sorted_items = sorted(rf.items())
            sorted_dict_str = "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"
            rps_small_probs.append(sorted_dict_str)
            # print(sorted_dict_str)


        
            values_dict = eval(sorted_dict_str.strip())
            
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
                print(f"did nothing with:{array_rf[-1]}")
        elif mood == 2:
            # print("Hello")
            # print(item)
            if isFirstLoop:
                knowledge_structure = mark_items_with_range_structure(item)
                isFirstLoop = False
            else:
                print("--------MERGING LEFT--------")
                print(item)

end_time = time.time()
print("Final RP:")
print(final_rf)
print(f"Time taken: {end_time-start_time}")