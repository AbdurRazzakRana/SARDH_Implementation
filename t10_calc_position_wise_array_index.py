# # '[3', 'i', 'j', 
# #     '[4', 'j', 'i', 'j', 'T-i-j', 'k', 
# #         '[5', 'k', 'alpha', 'i', 'k', 'A-i-k', 'k', 'j', 'B-j-k', 'i', 'j', 'T-i-j', 'T-i-j', 'k', 'k', ']',
# #     'k', 'j', 'j', ']', 
# # 'j', 'i', 'i', ']'

class LoopNode:
    def __init__(self, number, level, var, parent=None):
        self.type = "loop"
        self.number = number
        self.level = level
        self.var = var
        self.array_used_below = []
        self.array_used_loop_var = []
        self.children = []     # for DFS printing
        self.unique_const_under_this_loop = []
        self.parent = parent
        self.left = None
        self.right = None
        self.child = None      # pointer to first child

    def __repr__(self):
        return f"LoopNode({self.number}, level={self.level})"


class NormalNode:
    def __init__(self, parts, level, parent=None):
        self.type = "normal"
        self.parts = parts
        self.level = level
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        parent_num = self.parent.number if self.parent else None
        return f"NormalNode({self.parts}, level={self.level}, parent={parent_num})"


trace = ['[3', 'i', 'j',
         '[4', 'j', 'i', 'j', "'T-i-j'", 'k',
             '[5', 'k', "'alpha'", 'i', 'k', "'A-i-k'", 'k', 'j', "'B-j-k'", 'i', 'j', "'T-i-j'", "'T-i-j'", 'k', 'k', ']',
         'k', 'j', 'j', ']',
        'j', 'i', 'i', ']']


level = 0
prevNode = None
parent_stack = []
root_nodes = []   # to track top-level nodes

for index, token in enumerate(trace):
    if token.startswith('[') and token[1:].isdigit():
        number = int(token[1:])
        current_parent = parent_stack[-1] if parent_stack else None
        parts = trace[index+1].replace("'", "").split("-")
        loop = LoopNode(number, level, var=parts[0], parent=current_parent)

        # connect sequentially
        if prevNode:
            prevNode.right = loop
            loop.left = prevNode

        # if has a parent, add as a child
        if parent_stack:
            parent_stack[-1].children.append(loop)
        else:
            root_nodes.append(loop)

        prevNode = loop
        level += 1
        parent_stack.append(loop)

    elif token == ']':
        # end of this loop scope
        prevNode = parent_stack.pop()
        level -= 1

    else:
        # Normal node
        parts = token.replace("'", "").split("-")
        print(parts)
        current_parent = parent_stack[-1] if parent_stack else None
        normal_node = NormalNode(parts, level, parent=current_parent)

        # connect sequentially
        if prevNode:
            prevNode.right = normal_node
            normal_node.left = prevNode

        # attach as a child of current parent loop
        if current_parent:
            current_parent.children.append(normal_node)
            normal_node.parent = current_parent
        else:
            root_nodes.append(normal_node)
        
        # treverse top and enlist to all loop node if it is array node
        if len(normal_node.parts) > 1:
            tempNode = normal_node.parent
            while tempNode is not None:
                # tempNode.array_used_below.append(parts)
                base_name = parts[0]
                already_listed = any(existing[0] == base_name for existing in tempNode.array_used_below)
                if not already_listed:
                    tempNode.array_used_below.append(parts)

                if any(p == tempNode.var for p in parts):
                    already_listed = any(existing[0] == base_name for existing in tempNode.array_used_loop_var)
                    if not already_listed:
                        tempNode.array_used_loop_var.append(parts)
                tempNode = tempNode.parent
        elif len(normal_node.parts) == 1:
            # consts
            base_name = parts[0]
            already_listed = any(existing[0] == base_name for existing in normal_node.parent.unique_const_under_this_loop)
            if not already_listed:
                normal_node.parent.unique_const_under_this_loop.append(parts)
        prevNode = normal_node

# DFS traversal
def dfs_print(node, indent=0):
    prefix = "  " * indent
    if isinstance(node, LoopNode):
        print(f"{prefix}Loop {node.number} (level {node.level}) (Array used below {node.array_used_below}) (Array used loop var {node.array_used_loop_var})")
        for child in node.children:
            dfs_print(child, indent + 1)
    else:
        print(f"{prefix}Normal {node.parts} (level {node.level})")

print("\n=== DFS Tree Structure ===")
for root in root_nodes:
    dfs_print(root)


def get_arrays_impose_reuses(loop_node: LoopNode):
    not_used = []
    
    for parts in loop_node.array_used_below:
        base = parts[0]
        
        # Check if same base exists in array_used_loop_var
        already_used = any(base == var_parts[0] for var_parts in loop_node.array_used_loop_var)
        
        if not already_used:
            not_used.append(parts)
    
    return not_used

def print_loopnode(loop_node, parts):
    print(f"\n=== Calculating for Array Reference: {parts}===")
    print(f"LoopNode {loop_node.number}")
    print(f"Level: {loop_node.level}")
    print(f"Loop Var: {loop_node.var}")
    print(f"Parent Loop: {loop_node.parent.number if loop_node.parent else None}")
    print(f"Array Used Below: {loop_node.array_used_below}")
    print(f"Array Used Loop Var: {loop_node.array_used_loop_var}")
    print(f"Unique const variables: {loop_node.unique_const_under_this_loop}")

def traverse_and_print_arrays(node, array_dict, occurance_time, parts):
    if node is None:
        return
    
    # If it's a NormalNode
    if isinstance(node, NormalNode):
        return
    
    # If it's a LoopNode → go inside its child
    elif isinstance(node, LoopNode):
        for array in node.array_used_loop_var:
            for key in array_dict:
                if key == array[0]:
                    array_dict[key] *= node.number
            
            if array[0] == parts[0]:
                occurance_time[0] *= node.number
                

        for child in node.children:
            traverse_and_print_arrays(child, array_dict, occurance_time, parts)


def calc_reuse_distance_positional_array(loop_node, parts):
    # print_loopnode(loop_node, parts)
    # Create key-value dict where key = parts[0], value = 1
    array_dict = {parts[0]: 1 for parts in loop_node.array_used_below}
    occurance_time = [loop_node.number - 1]
    
    for child in loop_node.children:
        traverse_and_print_arrays(child, array_dict, occurance_time, parts)
    tempNode = loop_node.parent
    while tempNode != None:
        occurance_time[0] *= tempNode.number
        tempNode = tempNode.parent
    
    return sum(array_dict.values()) + len(loop_node.unique_const_under_this_loop) -1, occurance_time[0]

def calculate_loopnode_metrics(loop_node: LoopNode, prefix):
    # print_loopnode(loop_node)
    # Example calculation: find arrays in below but not using loop var
    reuse_introducing_array_refs = [
        parts for parts in loop_node.array_used_below
        if not any(parts[0] == var_parts[0] for var_parts in loop_node.array_used_loop_var)
    ]

    is_last_level = not any(isinstance(child, LoopNode) for child in loop_node.children)
    # print(f"Arrays NOT dependent on loop var: {not_reused}")
    for parts in reuse_introducing_array_refs:
        if loop_node.var not in parts and is_last_level:   # <-- main condition
            print(f"  → Already Covered in earlier process Skipped: {parts} (does NOT depend on loop var '{loop_node.var}') and used as a const")
        else:
            rd_array, occurance = calc_reuse_distance_positional_array(loop_node, parts)
            print("RD CALCULATED: ", rd_array)
            print("Occurance CALCULATED: ", occurance)
            # break # remove later


def dfs_bottom_up(node, indent=0):
    # visit children first
    for child in node.children:
        if isinstance(child, LoopNode):
            dfs_bottom_up(child, indent + 2)
    # Then print THIS LoopNode information
    if isinstance(node, LoopNode):
        prefix = "  " * indent
        print_loopnode(node, prefix)
        if node.parent:
            for const in node.unique_const_under_this_loop:
                base_name = const[0]
                already_listed = any(existing[0] == base_name for existing in node.parent.unique_const_under_this_loop)
                if not already_listed:
                    node.parent.unique_const_under_this_loop.append(const)
        # print(f"{prefix}=== LoopNode Info ===")
        # print(f"{prefix}Number: {node.number}")
        # print(f"{prefix}Level: {node.level}")
        # print(f"{prefix}Var: {node.var}")
        # parent_num = node.parent.number if node.parent else None
        # print(f"{prefix}Parent: {parent_num}")
        # print(f"{prefix}Array Used Below: {node.array_used_below}")
        # print(f"{prefix}Array Used Loop Var: {node.array_used_loop_var}")
        # # print(f"{prefix}Array Reuse Calc: {get_arrays_impose_reuses(node)}")
        # print(f"{prefix}Children Count: {len(node.children)}")

        # print(f"{prefix}-------------------------")

        calculate_loopnode_metrics(node, prefix)

print("\n=== Bottom-Up DFS Loop Traversal ===")
for root in root_nodes:
    if isinstance(root, LoopNode):
        dfs_bottom_up(root)