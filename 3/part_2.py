import numpy as np
import re
from string import punctuation

data = list(open("3/engine_schematic.in"))

cogs = {
    (ix, iy) : []
    for ix in range(len(data))
    for iy in range(len(data[0]) - 1)
    if data[ix][iy] in '*'
    }

for r, row in enumerate(data): # Loop through the data
    for number in re.finditer(r"\d+", row, ):
        surroundings = [ 
            (x, y) 
            for x in (r-1, r, r+1)
            for y in range(number.start()-1, number.end()+1)
        ]
        
        for s in surroundings & cogs.keys():
            print("  Found cog at ", s, ": ", cogs[s])
            print("  Collecting part number:", number.group())
            cogs[s].append(number.group())
            print()

cumsum = 0 
for k in cogs.keys():
    if len(cogs[k]) > 1:ga
        print(cogs[k])
        prod = 1
        for i in cogs[k]:
            prod *= int(i)
        cumsum += prod

print(cumsum)