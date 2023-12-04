import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

with open("./2/input.in") as file:

    sum = 0

    for line in file:
        print(line)
        split_line = line.split(':')
        game_number = re.findall("\d+", split_line[0])[0]
        samples = split_line[1].split(";")

        # sum += int(game_number)
        min_possible_red = 0
        min_possible_green = 0 
        min_possible_blue = 0
        for sample in samples:

            n_red = re.findall(r'(\d+)\sred', sample)
            n_green = re.findall(r'(\d+)\sgreen', sample)
            n_blue = re.findall(r'(\d+)\sblue', sample)

            if len(n_red) == 0:
                n_red = 0
            else:
                n_red = int(n_red[0])

            if len(n_green) == 0:
                n_green = 0
            else:
                n_green = int(n_green[0])

            if len(n_blue) == 0:
                n_blue = 0
            else:
                n_blue = int(n_blue[0])

            # if (n_red > MAX_RED or n_green > MAX_GREEN or n_blue > MAX_BLUE):
            #     print("---! Found invalid game.")
            #     sum -= int(game_number)
            #     break

            if n_red > min_possible_red:
                min_possible_red = n_red
            if n_green > min_possible_green:
                min_possible_green = n_green
            if n_blue > min_possible_blue:
                min_possible_blue = n_blue

            sum += min_possible_red * min_possible_green * min_possible_blue



        print(game_number, sum)
            
    print()
    print("The sum is", sum)



