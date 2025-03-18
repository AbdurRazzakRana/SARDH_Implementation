def predict_2_nested(key_dict, i_tot, j_tot):
    # print(i_tot)
    # print(j_tot)
    len0=  len(key_dict[0])
    predicted_list = {}
    predicted_list.setdefault(-1, 0)
    for key, values in key_dict.items():
        if len(values) == len0:
            r_22 = values[0]
            r_23 = values[1]
            r_32 = values[2]
            r_33 = values[3]
            
            bb = r_22
            j_inc = r_23 - r_22
            i_inc = r_32 - r_22
            c_ij = r_33 - (bb + i_inc + j_inc)
            # print(c_ij)
            
            rd = bb + i_inc * i_tot + j_inc * j_tot + c_ij * i_tot * j_tot
            # print(f"Key {key}: {rd}")
            predicted_list[key] = rd
    # print(predicted_list)
    return predicted_list

def predict_3_nested(key_dict, i_tot, j_tot, k_tot):
    len0=  len(key_dict[0])
    predicted_list = {}
    predicted_list.setdefault(-1, [])
    for key, values in key_dict.items():
        if len(values) == len0:
            bb = values[0]
            k1 = values[1]
            j1 = values[2]
            jk = values[3]
            i1 = values[4]
            ik = values[5]
            ij = values[6]
            ijk = values[7]
            k_inc = k1 - bb
            j_inc = j1-bb
            i_inc = i1-bb
            c_jk = jk - (bb + k_inc + j_inc)
            c_ij = ij - (bb + i_inc + j_inc)
            c_ik = ik - (bb + i_inc + k_inc)
            c_ijk = ijk - (bb + i_inc + j_inc + k_inc + c_ik + c_ij + c_jk)
            rd = bb + k_inc * k_tot + i_inc*i_tot + j_inc*j_tot + c_jk * j_tot * k_tot + c_ik* i_tot * k_tot + c_ij* i_tot*j_tot + c_ijk*i_tot*j_tot*k_tot
            print(f"Key {key}: {rf}")
            # print(f"Key {key}: {rd}")
            predicted_list[key] = rd
    # print(predicted_list)
    return predicted_list



