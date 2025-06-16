# '[3', 'i', 'j', 
#     '[4', 'j', 'i', 'j', 'T-i-j', 'k', 
#         '[5', 'k', 'alpha', 'i', 'k', 'A-i-k', 'k', 'j', 'B-j-k', 'i', 'j', 'T-i-j', 'T-i-j', 'k', 'k', ']',
#     'k', 'j', 'j', ']', 
# 'j', 'i', 'i', ']'

def calculate_single_array_position_reuse(oneArrayPos):
    # 
    for item in oneArrayPos:
        print(item, "-", oneArrayPos[item])


def extract_array_info_with_loops(trace):
    loop_stack = []                  # Stack of active loop levels
    array_info = []                 # Output list
    loop_level_to_var = {}         # Dynamic map of loop level → loop variable
    i = 0

    while i < len(trace):
        token = trace[i]

        if token.startswith("["):
            loop_level = int(token[1:])
            if i + 1 < len(trace):
                next_token = trace[i + 1]
                if not next_token.startswith("[") and next_token != "]":
                    loop_level_to_var[loop_level] = next_token
            loop_stack.append(loop_level)
        elif token == "]":
            if loop_stack:
                loop_stack.pop()
        elif token.startswith("'") and token.endswith("'"):
            ref = token.strip("'")

            # Skip scalar values like 'alpha'
            if "-" not in ref:
                i += 1
                continue

            parts = ref.split("-")
            base = parts[0]
            vars_used = parts[1:]

            depth = len(loop_stack)
            outer_loops = [f"{lvl}-{loop_level_to_var.get(lvl, '?')}" for lvl in loop_stack]

            # Find inner loops
            inner_loops = []
            temp_stack = loop_stack.copy()
            for j in range(i + 1, len(trace)):
                t = trace[j]
                if t.startswith("["):
                    lvl = int(t[1:])
                    if j + 1 < len(trace):
                        var = trace[j + 1]
                        loop_level_to_var[lvl] = var  # Update mapping
                        inner_loops.append(f"{lvl}-{var}")
                    temp_stack.append(lvl)
                elif t == "]":
                    if temp_stack:
                        temp_stack.pop()
                elif t.startswith("'") and "-" in t:
                    break  # stop at next array reference

            array_info.append({
                "ref": ref,
                "array": base,
                "depth": depth,
                "variables": sorted(set(vars_used)),
                "outer_loops": outer_loops,
                "inner_loops": sorted(set(inner_loops))
            })
        i += 1

    return array_info




trace = ['[3', 'i', 'j', 
         '[4', 'j', 'i', 'j', "'T-i-j'", 'k', 
             '[5', 'k', "'alpha'", 'i', 'k', "'A-i-k'", 'k', 'j', "'B-j-k'", 'i', 'j', "'T-i-j'", "'T-i-j'", 'k', 'k', ']', 
         'k', 'j', 'j', ']', 
        'j', 'i', 'i', ']']

result = extract_array_info_with_loops(trace)
index = -1
for entry in result:
    index+=1
    if index == 0:
        print("do notihing")
    else:
        calculate_single_array_position_reuse(entry)
        break
    # print()