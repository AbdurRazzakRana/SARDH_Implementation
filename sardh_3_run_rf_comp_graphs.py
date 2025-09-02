import ast
from graph_genration import generate_rp_comparison_graph


# Read the dictionaries from the text file
with open("sardh_2_output_1_match_rf_size_dynamic_static.txt", "r") as file:
    lines = file.readlines()

# Check that there are at least two lines
if len(lines) >= 2:
    parda_reference_rf = ast.literal_eval(lines[0].strip())
    this_model_rf = ast.literal_eval(lines[1].strip())

    # generate_rp_comparison_graph.draw_RF_comparison_bar_graph(parda_reference_rf, this_model_rf, 100)
    generate_rp_comparison_graph.draw_RF_comparison_bar_graph(parda_reference_rf, this_model_rf, 800)
else:
    print("Error: File does not contain at least two lines.")
