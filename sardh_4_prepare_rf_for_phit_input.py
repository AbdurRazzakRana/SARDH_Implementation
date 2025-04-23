import ast
from graph_genration import generate_rp_comparison_graph

def prepare_phit_compatible_data_from_RF(rf, destination_file):
    total_rf_count = sum(rf.values())
    with open(destination_file, "w") as f:
        for key, count in rf.items():
            ratio = count / total_rf_count
            f.write(f"{key}, {ratio:.8f}, {count}\n")

# Read the dictionaries from the text file
with open("sardh_2_output_1_match_rf_size_dynamic_static.txt", "r") as file:
    lines = file.readlines()

# Check that there are at least two lines
if len(lines) >= 2:
    parda_reference_rf = ast.literal_eval(lines[0].strip())
    this_model_rf = ast.literal_eval(lines[1].strip())

    prepare_phit_compatible_data_from_RF(parda_reference_rf, "sardh_5_input_1_parda_phit_prepared.dat")

    REUSE_DISTANCE_MISS_ALWAYS = 2 ** 30
    unidentified_references_by_model = sum(parda_reference_rf.values()) - sum(this_model_rf.values())
    if unidentified_references_by_model > 0:
        this_model_rf[REUSE_DISTANCE_MISS_ALWAYS] = unidentified_references_by_model
        print("Unidentified References by the model: ", unidentified_references_by_model)
        print("REUSE_DISTANCE_MISS_ALWAYS: ", REUSE_DISTANCE_MISS_ALWAYS)
    prepare_phit_compatible_data_from_RF(this_model_rf, "sardh_5_input_2_model_phit_prepared.dat")
    
else:
    print("Error: File does not contain at least two lines.")