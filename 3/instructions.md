# Day 3: Gear Ratios 

You and the Elf eventually reach a **gondola lift station**; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: **they're not moving.**

"Aaah!"

You turn around to see a **slightly-greasy Elf** with a wrench and a look of surprise. *"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it."* 

You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a **visual representation of the engine**. There are lots of numbers and symbols you don't really understand, but apparently **any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum**. 

(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

```
467..114..  
...*......  
..35..633.  
......#...  
617*......  
.....+.58.  
..592.....  
......755.  
...$.*....  
.664.598..  
```
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: **114 (top right)** and **58 (middle right)**. Every other number is adjacent to a symbol and so is a part number; **their sum is 4361.**

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

## Approach

1. Get valid part numbers (adjacent to symbols)
  - Can't read line-by-line (need to retain at least the line above and the line below)
  - Once i find a valid number, I need to retrieve adjacent characters
2. Sum valid part numbers


### Cases

**First row:**


First character. Check 1, 2, and ?. 


```
X?0000000
123456789
```

Second character. Check 1, 2, 3, and both ?.

```
?X?000000
123456789
```

Third character. Check 2, 3, 4, and both ?. 

```
0?X?00000
123456789
```

Last character. Check 8, 9, and ?. 

```
0000000?X
123456789
```


11071  Too low.

535756 too low.

537412 wrong