# This task will separate loop blocks from send a dict of separated blocks

# intput = ['retval', 'i', '[3', 'i', 'j', '[5', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-j', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i', 'i', '[3', 'i', 'j', '[7', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-j', 'j', 'j', ']', 'j', 'i', 'i', ']', 'i'] 
# output =
# ['retval', 'i']
# ['[3', 'i', 'j', '[5', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-j', 'j', 'j', ']', 'j', 'i', 'i']
# ['i', 'i']
# ['[3', 'i', 'j', '[7', 'j', 'i', 'i', 'j', 'arr-i-j', 'i', 'i', 'brr-j', 'j', 'j', ']', 'j', 'i', 'i']
# ['i']

def separate_loop_blocks_from_refs(vec_refs):
    stack = []
    baseline_sequence = []
    separated_loop_blocks= []
    separated_loop_blocks_index = -1

    for index, item in enumerate(vec_refs):
        if item.startswith('['):
            stack.append(index) 
        elif item == ']':  # End of a loop
            # Pop the last loop index
            start_ind = stack.pop()
            if not stack:
                # just ended a loop stack
                if baseline_sequence:
                    # dump the previous stored base references into a new location of separated_loop_blocks
                    separated_loop_blocks.append([])
                    separated_loop_blocks_index+=1
                    separated_loop_blocks[separated_loop_blocks_index] = baseline_sequence            
                    baseline_sequence = []
                # dump the current loop annotated trace
                separated_loop_blocks.append([])
                separated_loop_blocks_index+=1
                separated_loop_blocks[separated_loop_blocks_index] = vec_refs[start_ind:index+1]
        else:
            if not stack:
                baseline_sequence.append(item)  # Add directly to the final sequence

    # add the last un-added baseline traces for the end traces
    separated_loop_blocks.append([])
    separated_loop_blocks_index+=1
    separated_loop_blocks[separated_loop_blocks_index] = baseline_sequence            
    baseline_sequence = []
    # for item in separated_loop_blocks:
    #     print(item)
    return separated_loop_blocks
