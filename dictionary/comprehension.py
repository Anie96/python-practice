#dictionary comprehenson

comp_dict = {value: value * 2 for value in range(1, 6) if value % 2 == 0}

print(comp_dict)