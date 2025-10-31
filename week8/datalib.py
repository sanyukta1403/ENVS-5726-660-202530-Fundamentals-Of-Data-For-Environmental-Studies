from typing import List, Any

def convert_yesno_to_binary(table: List[tuple]) -> List[tuple]: #the function expects table to be a list of tuples 
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


"""""
def convert_str_to_numeric(table: List[tuple]) -> List[tuple]:
    string_class = type(table[0]) # get the class type of the first row in the table

    string_to_value_dict = {} # dict to map string to number 
    next_num = 1 # assigning strings beginining with number 1 

    str_to_val_table = [] # initializes an empty list to hold the converted rows

    for row in table:
        values_list = list(row) # converts the NamedTuple which is immutable into a mutable list so you can modify its contents

        for i, value in enumerate(values_list): # iterates over every value and its index in the current row
            if isinstance(value, (int, float)) or value == "": #skips any value that is already numeric (int or float), or is an empty string ("")
                continue # if this cell doesn’t need converting, ignore it and go to the next one

            if value not in string_to_value_dict:
                string_to_value_dict[value] = next_num
                next_num += 1
            
            values_list[i] = string_to_value_dict[value]

        str_to_val_table.append(string_class(*values_list))
    
    return str_to_val_table

"""""

from typing import List

def convert_str_to_numeric(table: List[tuple]) -> List[tuple]:
    named_tuple_class = type(table[0]) # takes the first row of the table and gets its type: the namedtuple clas
    column_name_list = named_tuple_class._fields #returns a list of all the field names

    numeric_column_list = []
    for column_name in column_name_list: #looping over every column in the table
        column_values = [getattr(row, column_name) #fetches the value of that specific column (like row.Gender) for each row
                         for row in table]
        
        #this goes through the column values and filters out anything that’s already numeric
        unique_non_numeric_column_values = set([column_value 
                                                for column_value in column_values
                                                if not isinstance(column_value, (int, float, complex))])
        
        map_dict = {unique_value: index
                    for (index, unique_value) in enumerate(unique_non_numeric_column_values)} #assigns an index number to each unique string so that the function knows how to replace strings with numbers
        
        #this replaces each value in the column using the mapping; if the value is in map_dict (ex: 'Male'), it replaces it with the numeric code (ex: 0)
        numeric_column_values = [map_dict[column_value] if column_value in map_dict else column_value
                                 for column_value in column_values]
        numeric_column_list.append(numeric_column_values) #

    numeric_row_table = [list(column) for column in zip(*numeric_column_list)] #transposes the list of columns into a list of rows
    numeric_tuple_table = [named_tuple_class(*row) for row in numeric_row_table] #rebuilds each row list into an instance of the original NamedTuple class
    return numeric_tuple_table
