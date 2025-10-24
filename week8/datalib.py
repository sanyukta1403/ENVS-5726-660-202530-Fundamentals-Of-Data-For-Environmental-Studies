from typing import List, Any

def convert_yesno_to_binary(table: List[tuple]) -> List[tuple]:
    theclass = type(table[0]) # get the NamedTuple class
    binary_table = [] # this will store the modified rows

    for row in table:
        binary_list = list(row)  # turn NamedTuple into a list
        binary_row_list = [] # store converted values for this one row

        for value in binary_list:
            if value == 'Yes':
                binary_row_list.append(1)
            elif value in ["", "No", "Do not know", "Do Not Know"]:
                binary_row_list.append(0)
            else:
                binary_row_list.append(value)
        
        back_to_tuple = theclass(*binary_row_list) # turn list back into NamedTuple
        binary_table.append(back_to_tuple) # add to new table
    
    return binary_table

def convert_str_to_numeric(table: List[tuple]) -> List[tuple]:
    string_class = type(table[0])

    string_to_value_dict = {} #dict to map string to number 
    next_num = 1 #assigning strings beginining with number 1 

    str_to_val_table = []

    for row in table:
        values_list = list(row)

        for i, value in enumerate(values_list):
            if isinstance(value, (int, float)) or value == "":
                continue

            if value not in string_to_value_dict:
                string_to_value_dict[value] = next_num
                next_num += 1
            
            values_list[i] = string_to_value_dict[value]

        str_to_val_table.append(string_class(*values_list))
    
    return str_to_val_table


