# [3', 'i', 'j', '[5', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i', ']
# This file will elaborate the loop part only
from collections import deque
import copy

def parse_and_generate_sequence(vec_refs):
    stack = []  # To manage nested loops
    sequence = []  # Final sequence to be generated

    for index, item in enumerate(vec_refs):
        if item.startswith('['):  # Start of a loop
            loop_count = int(item[1:])  # Extract loop count
            loop_var = vec_refs[index+1]
            stack.append((loop_count, [], loop_var))  # Push loop count and new temp list
        elif item == ']':  # End of a loop
            # Pop the last loop and its content
            loop_count, temp_sequence, loop_var = stack.pop()
            expanded_sequence=[]
            
            for loopInd in range(0, loop_count):
                temp_seq_one_loop = copy.deepcopy(temp_sequence)
                for index, item in enumerate(temp_seq_one_loop):
                    # if 'rr' in item:  # Check if 'rr' exists in the string
                    #     parts = item.split('-')

                    #     for idx, value in enumerate(parts):  # Check if `var` exists in any of the parts
                    #         # Replace `var` with `str(x)` only in the first occurrence of `var` in `parts`
                    #         if parts[idx] == loop_var:
                    #             parts[idx] = str(loopInd)
                    #     temp_seq_one_loop[index] = '-'.join(parts)  # Join back the modified parts
                    parts = item.split('-')
                    if len(parts) > 1:  # Check if 'rr' exists in the string
                        for idx, value in enumerate(parts):  # Check if `var` exists in any of the parts
                            # Replace `var` with `str(x)` only in the first occurrence of `var` in `parts`
                            if parts[idx] == loop_var:
                                parts[idx] = str(loopInd)
                        temp_seq_one_loop[index] = '-'.join(parts)  # Join back the modified parts
                            
                # print(temp_seq_one_loop)
                expanded_sequence += temp_seq_one_loop
                temp_seq_one_loop.clear()

            if stack:
                # Append expanded sequence to the parent loop
                stack[-1][1].extend(expanded_sequence)
            else:
                # Append expanded sequence to the final sequence
                sequence.extend(expanded_sequence)
        else:  # Normal elements
            if stack:
                stack[-1][1].append(item)  # Add to the current loop's temp list
            else:
                sequence.append(item)  # Add directly to the final sequence

    return sequence
    

def expend_loop_form_annotated_trace(vec_refs):
    # vec_refs = ['[3', 'i', 'j', '[5', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-i', 'j', 'j', ']', 'j', 'i', 'i',']' ]

    # print(unique_sets)
    final_sequence = parse_and_generate_sequence(vec_refs)
    
    return final_sequence