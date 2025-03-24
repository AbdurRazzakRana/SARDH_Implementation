data_dict = {-1: 140404, 0: 561198, 1: 140798, 2: 280000, 3: 279600}
reference_dict = {0: 561203, 1: 140799, 2: 280000, 3: 279600, 19902: 1, 20101: 200, 20102: 1, 20301: 200, 20302: 1, 20501: 200, 20502: 1, 20701: 200, 20702: 1, 20901: 200, 20902: 1, 21101: 200, 21102: 1, 21301: 200, 21302: 1, 21501: 200, 21502: 1, 21901: 200, 21902: 1, 22101: 200, 22102: 1, 22301: 200, 22302: 1, 22501: 200, 22502: 1, 22701: 200, 22702: 1, 22901: 200, 22902: 1, 23101: 200, 23102: 1, 23301: 200, 23302: 1, 23501: 200, 23502: 1, 23701: 200, 23702: 1, 23901: 200, 23902: 1, 24101: 200, 24102: 1, 24301: 200, 24302: 1, 24501: 200, 24502: 1, 24701: 200, 24702: 1, 24901: 200, 24902: 1, 25101: 200, 25102: 1, 25301: 200, 25302: 1, 25501: 200, 25502: 1, 25701: 200, 25702: 1, 25901: 200, 25902: 1, 26101: 200, 26102: 1, 26301: 200, 26302: 1, 26501: 200, 26502: 1, 26701: 200, 26702: 1, 26901: 200, 26902: 1, 27101: 200, 27102: 1, 27301: 200, 27302: 1, 27501: 200, 27502: 1, 27701: 200, 27702: 1, 27901: 200, 27902: 1, -1: 120303}
total_refs = 0
for key in data_dict:
    total_refs += data_dict[key]

# total_refs = 852219
print(total_refs)

for key, value in reference_dict.items():
    if key not in data_dict:
        print(key)
        data_dict[key] = 0

# Preparing the lines in the required format
lines = []
for key, value in data_dict.items():
    if key != -1:
        ratio = value / total_refs
        line = f"{key}, {ratio:.8f}, {value}"
        lines.append(line)
value = data_dict[-1]
ratio = value / total_refs
lines.append(f"{-1}, {ratio:.8f}, {value}")

# Saving the lines to a file
file_path = "prepared_RP_static.txt"
with open(file_path, "w") as file:
    for line in lines:
        file.write(line + "\n")