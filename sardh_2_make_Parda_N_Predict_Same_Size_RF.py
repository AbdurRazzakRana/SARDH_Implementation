# This file will convert dynamic reusse profile taken from parda output mentioned in sardh_dynamic_rp_ASIS.txt 
# Then it will balance the parda_rf and this_method_rf keys: make them at least same size

import ast

parda_rf_asis = {}
parda_total_rf = 0
with open("sardh_2_input_1_dynamic_rf_ASIS.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            key = int(parts[0])
            value = int(parts[2])
            parda_rf_asis[key] = value
parda_total_rf = sum(parda_rf_asis.values())

parda_rf = {-1: parda_rf_asis[-1]}
for k in sorted(k for k in parda_rf_asis if k != -1):
    parda_rf[k] = parda_rf_asis[k]

# print(parda_rf)

this_model_rf = {}
with open("sardh_1_out_1_static_rf.txt", "r") as file:
    line = file.readline().strip()
    this_model_rf = ast.literal_eval(line)
print(this_model_rf)

for key in this_model_rf:
    if key not in parda_rf:
        parda_rf[key] = 0

for key in parda_rf:
    if key not in this_model_rf:
        this_model_rf[key] = 0

with open("sardh_2_output_1_match_rf_size_dynamic_static.txt", "w") as file:
    file.write(str(parda_rf) + "\n")
    file.write(str(this_model_rf) + "\n")

print("Total Parda Reference: ", parda_total_rf)
print("Total This Model Reference: ", sum(this_model_rf.values()))
