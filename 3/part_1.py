import numpy as np
import re
from string import punctuation

FILENAME = "3/engine_schematic.in"
SYMBOLS = set(punctuation) - {"."} # Definition of valid symbols (cogs).

def find_cogs(a:np.ndarray):

    found_cogs = {}
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):            
            if a[i][j] in SYMBOLS:
                found_cogs[(i, j)] = a[i][j]

    return found_cogs

    
def get_content_array(filename:str):

    # Read the content from the file
    with open(filename) as file:
        content = [line.strip() for line in file] 

    # Determine the dimensions of the array
    num_rows = len(content)
    num_cols = len(content[0])

    # Create a NumPy array to hold the characters
    content_array = np.empty((num_rows, num_cols), dtype='str')

    # Fill the array with characters from the file content
    for i in range(num_rows):
        for j in range(num_cols):
            content_array[i][j] = content[i][j]
    
    return np.pad(content_array, (1,1), pad_with)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', '.')
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector

print()
print("--- RUNNING SCRIPT ---")
print()
print(" - FILE = ")
print(" -", FILENAME)
print()
print("----------------------\n\n")

print("Content array looks like:\n")
data = get_content_array(FILENAME)
print(data)
cogs_dict = find_cogs(data)

cumsum = 0
for r, row in enumerate(data): # Loop through the data
    string_row = "".join(row.tolist())
    for number in re.finditer(r"\d+", string_row, ):
        print(number.group())
        surroundings = [ 
            (x, y) 
            for x in (r-1, r, r+1)
            for y in range(number.start()-1, number.end()+1)
        ]
        
        for s in surroundings:
            if s in cogs_dict.keys():
                print("  Found cog at ", s, ": ", cogs_dict[s])
                print("  Collecting part number:", number.group())
                cumsum += int(number.group())
                print()

print("Result:", cumsum)