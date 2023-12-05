cards = list(open("4/data.in"))

cumsum = 0 
for ix, card in enumerate(cards):
    card = card[:-1]

    winning = [w for w in card.split("|")[0].split(":")[1].split(" ") if w != '']
    numbers = [n for n in card.split("|")[1].split(" ") if n != '']
    winners = [n for n in numbers if n in winning]
    if len(winners) > 0:
        print("Found these winning numbers: ")
        print(winners)
        cumsum += 2 ** ( len(winners) - 1 ) 
        print(cumsum)
        print()

print("Result is", cumsum)
