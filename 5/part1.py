import re

# Regex patterns to read the file. 

seeds_pattern = r'seeds:\s(.*)'
sts_pattern = r'seed-to-soil map:\n((?:.+\n)+)'
stf_pattern = r'soil-to-fertilizer map:\n((?:.+\n)+)'
ftw_pattern = r'fertilizer-to-water map:\n((?:.+\n)+)'
wtl_pattern = r'water-to-light map:\n((?:.+\n)+)'
ltt_pattern = r'light-to-temperature map:\n((?:.+\n)+)'
tth_pattern = r'temperature-to-humidity map:\n((?:.+\n)+)'
htl_pattern = r'humidity-to-location map:\n((?:.+\n)+)'

contents = open('5/test.in', 'r').read()

def create_map_function(maps:list):
    def mapper(input):
        output = input
        for map in maps:
            to, fro, span = map
            if input in range(fro, fro+span):
                output = input - (fro - to)
        return output 
    return mapper


# Seeds
seeds = [int(s) for s in re.findall(seeds_pattern, contents)[0].split(" ")]
print("seeds:", seeds)

# Seed to soil
sts_find = [i for i in re.findall(sts_pattern, contents)[0].split("\n") if i ]
sts_map_values = []
for row in sts_find:
    cols = row.split(" ")
    sts_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

sts_mapper = create_map_function(sts_map_values)
soils = []
for seed in seeds:  
    soils.append(sts_mapper(seed))
print("soils:", soils)

# Soil to fertilizer
stf_find = [i for i in re.findall(stf_pattern, contents)[0].split("\n") if i ]
stf_map_values = []
for row in stf_find:
    cols = row.split(" ")
    stf_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

stf_mapper = create_map_function(stf_map_values)
fertilizers = []
for soil in soils:  
    fertilizers.append(stf_mapper(soil))
print("fertilizers:", fertilizers)

# Fertilizer to water
ftw_find = [i for i in re.findall(ftw_pattern, contents)[0].split("\n") if i ]
ftw_map_values = []
for row in ftw_find:
    cols = row.split(" ")
    ftw_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

ftw_mapper = create_map_function(ftw_map_values)
waters = []
for fertilizer in fertilizers:  
    waters.append(ftw_mapper(fertilizer))
print("waters:", waters)

# Water to light
wtl_find = [i for i in re.findall(wtl_pattern, contents)[0].split("\n") if i ]
wtl_map_values = []
for row in wtl_find:
    cols = row.split(" ")
    wtl_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

wtl_mapper = create_map_function(wtl_map_values)
lights = []
for water in waters:  
    lights.append(wtl_mapper(water))
print("lights:", lights)

# light to temperature
ltt_find = [i for i in re.findall(ltt_pattern, contents)[0].split("\n") if i ]
ltt_map_values = []
for row in ltt_find:
    cols = row.split(" ")
    ltt_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

ltt_mapper = create_map_function(ltt_map_values)
temperatures = []
for light in lights:  
    temperatures.append(ltt_mapper(light))
print("temperatures:", temperatures)

# temperature to humidity
tth_find = [i for i in re.findall(tth_pattern, contents)[0].split("\n") if i ]
tth_map_values = []
for row in tth_find:
    cols = row.split(" ")
    tth_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

tth_mapper = create_map_function(tth_map_values)
humidities = []
for temperature in temperatures:  
    humidities.append(tth_mapper(temperature))
print("humidities:", humidities)

# humidity to location
htl_find = [i for i in re.findall(htl_pattern, contents)[0].split("\n") if i ]
htl_map_values = []
for row in htl_find:
    cols = row.split(" ")
    htl_map_values.append( (int(cols[0]), int(cols[1]), int(cols[2])) )

htl_mapper = create_map_function(htl_map_values)
locations = []
for humidity in humidities:  
    locations.append(htl_mapper(humidity))
print("locations:", locations)

print("Closest location is", min(locations))