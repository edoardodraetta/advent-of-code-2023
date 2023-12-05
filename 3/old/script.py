import re
from string import punctuation


def find_valid_numbers(line_index:int, file:list, valid_characters_index:list):
    line = file[line_index]
    line_length = len(line)
    found = {}
    # Find contiguous numbers 
    for i in valid_characters_index: # right
        number = str(line[i]) 
        # print("idenfied digit:", number)
        for j in range(i+1, line_length):
            if line[j].isdigit():
                number = number + line[j]
                # print(j, "Concat", line[j], "right:", number)
            else:
                break

        for j in range(i-1, -1, -1): # left
            if line[j].isdigit():
                number = line[j] + number
                # print(j, "Concat", line[j], "left:", number)
            else:
                break
        # print(number)
        found[i] = number

    return found

def find_valid_characters(previous_index:int, current_index:int, next_index:int, file:list):
    """Given indexes for the line context (and the file itself), 
    identifies the indices of valid characters according to the problem statement.

    Args:
        previous_index (int): Index of the preceding line. 
        current_index (int): Index of the current line.
        next_index (int): Index of the next line.
        file (list): A list of the lines in the file.

    Returns:
        (list(int), list(int)): A tuple of two lists: (valid_indexes, valid_characters)
    """

    print_line(previous_index, file)
    print_line(current_index, file, emphasize=True)
    print_line(next_index, file)
    valid_indexes = []
    valid_characters = []
    if previous_index is None: # First line

        for ix, char in enumerate(file[current_index]):
            is_valid = False
            line_length = len(file[current_index])

            try:
                value = int(char)
            except:
                value = char 

            if type(value) is int:
                if ix == 0: # First character

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix+1])
                        is_valid = True
                    
                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True
                
                elif ix < line_length - 1: # Intermediate characters

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix+1])
                        is_valid = True
                    elif file[next_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True

                else: # Final characters

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True

            if is_valid:
                valid_indexes.append(ix)
                valid_characters.append(char)


    elif next_index is not None: # Intermediate line

        for ix, char in enumerate(file[current_index]):
            is_valid = False
            line_length = len(file[current_index])

            try:
                value = int(char)
            except:
                value = char 

            if type(value) is int:
                if ix == 0: # First character

                    # Previous line
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix+1])
                        is_valid = True

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix+1])
                        is_valid = True
                    
                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True
                
                elif ix < line_length - 1: # Intermediate character

                    # Previous line
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix+1])
                        is_valid = True
                    elif file[previous_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix-1])
                        is_valid = True

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix+1])
                        is_valid = True
                    elif file[next_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True

                else: # Final character

                    # Previous line 
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix-1])
                        is_valid = True

                    # Next line
                    if file[next_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix])
                        is_valid = True
                    elif file[next_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[next_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True
                
            if is_valid:
                valid_indexes.append(ix)
                valid_characters.append(char)

    else: # Final line
        for ix, char in enumerate(file[current_index]):
            is_valid = False
            line_length = len(file[current_index])

            try:
                value = int(char)
            except:
                value = char 

            if type(value) is int:
               
                if ix == 0: # First character
                    # Previous line
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix+1])
                        is_valid = True
                    
                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True

                elif ix < line_length - 1: # Intermediate characters

                    # Previous line
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix+1])
                        is_valid = True
                    elif file[previous_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix+1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix+1] )
                        is_valid = True
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True

                else: # Final character
                    # Previous line
                    if file[previous_index][ix] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix])
                        is_valid = True
                    elif file[previous_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[previous_index][ix-1])
                        is_valid = True

                    # Current line
                    elif file[current_index][ix-1] in SYMBOLS:
                        # print("Found adjacent symbol", value, "adjacent to", file[current_index][ix-1] )
                        is_valid = True

                if is_valid:
                    valid_indexes.append(ix)
                    valid_characters.append(value)
                
    return valid_indexes, valid_characters            

def print_line(index:int, file:list, emphasize:bool=False):
    '''
    Given a line index and a file,
    Print the line if the index is not none.
    '''
    if index is not None:
        if emphasize:
            print(index, ": ", file[index], "<--")
        else:
            print(index, ": ", file[index])

def line_indexer(scan_index:int, file:list):
    '''
    When given the scanning index of the files,
    return valid previus, current, and next line indexes.
    '''
    lines_in_file = len(file)
    if scan_index == 0:                  # first row
        previous_index = None
        current_index = scan_index
        next_index = 1
    elif scan_index < lines_in_file - 1: # intermediate row
        previous_index = scan_index - 1
        current_index = scan_index
        next_index = scan_index + 1 
    else:                                # last row
        previous_index = scan_index - 1
        current_index = scan_index
        next_index = None
    
    return previous_index, current_index, next_index

# CONSTANTS
SYMBOLS = set(punctuation) - {"."} # Definition of valid symbols.

FILE = "3/engine_schematic.in"
# FILE = "3/sample.in"
MAX_LINES = 1

with open(FILE) as f: 

    print()
    print()
    print("--- RUNNING SCRIPT ---")
    print()
    print()
    print(" - FILENAME = ")
    print(" - - FILE")
    print()
    print()
    print("----------------------")
    print()
    print()

    # Get all lines in the file at once
    eng_schema = f.read().splitlines()

    # These will store the line "context"
    # i.e. current, previous, and next lines. 
    p_line = None
    c_line = None
    n_line = None

    result = 0
    for ix, line in enumerate(eng_schema):
        if ix < MAX_LINES:
            p_ix, c_ix, n_ix = line_indexer(ix, eng_schema)

            valid_ixs, valid_chars = find_valid_characters(p_ix, c_ix, n_ix, eng_schema)
            valid_numbers = find_valid_numbers(c_ix, eng_schema, valid_ixs)
            # result += sum(valid_numbers)
            print(valid_numbers)
            # print("Cumulative sum:", result)
            print()
