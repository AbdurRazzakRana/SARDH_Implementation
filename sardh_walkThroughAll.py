
from t0_separate_loop_blocks_from_refs import separate_loop_blocks_from_refs
from t1_create_smaller_loop_bounds import create_smaller_loop_bounds
from t2_expand_loop_from_annotated_trace import expend_loop_form_annotated_trace
from t3_create_setn_vector_n_rf import create_set_n_vector_n_rf
from t4_unresolved_refs_solve import unresolved_refs_solve
import time
start_time = time.time()

vec_refs = ['retval', 'i', '[100', 'i', 'j', '[200', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[300', 'i', 'j', '[400', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i']
separated_loop_blocks = separate_loop_blocks_from_refs(vec_refs)
for item in separated_loop_blocks:
    if item[0].startswith('['):
        # print(item)
        rps_small_probs = []
        smaller_problems = create_smaller_loop_bounds(item)
        for small_prob in smaller_problems:
            unresolved_refs = []
            final_rf = {}
            expanded_trace = expend_loop_form_annotated_trace(small_prob)
            exp_trace_set, exp_trace_vector, exp_trace_in_order_merge_up, exp_rd = create_set_n_vector_n_rf(expanded_trace)
            for key, value in exp_rd.items():
                if key in final_rf:
                    final_rf[key] += value  
                else:
                    final_rf[key] = value 
            unresolved_refs.append([exp_trace_in_order_merge_up, exp_trace_vector])
            rf_unres, cold_miss = unresolved_refs_solve(unresolved_refs)
            for key, value in rf_unres.items():
                if key in final_rf:
                    final_rf[key] += value
                else:
                    final_rf[key] = value

            final_rf[-1] = len(cold_miss)
            sorted_items = sorted(final_rf.items())
            # sorted_dict_str = "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"
            rps_small_probs.append(sorted_items)
        break
    # else:
        # unresolved_refs.append([item, []])

# for key, value in rf_unres.items():
#     if key in final_rf:
#         final_rf[key] += value
#     else:
#         final_rf[key] = value

# final_rf[-1] = len(cold_miss)

# end_time = time.time()
# execution_time = end_time - start_time

# print(f"Execution time: {execution_time:.6f} seconds")


# sorted_items = sorted(final_rf.items())

# sorted_dict_str = "{" + ", ".join(f"{k}: {v}" for k, v in sorted_items) + "}"

# print(sorted_dict_str)