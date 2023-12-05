cards = list(open("4/data.in"))

print()
cumsum = 0 
card_counter = [1 for n in range(len(cards))]
for ix, card in enumerate(cards):
    card = card[:-1]
    print("Processing card", card, " (index", ix, ")") 

    winning = [w for w in card.split("|")[0].split(":")[1].split(" ") if w != '']
    numbers = [n for n in card.split("|")[1].split(" ") if n != '']
    winners = [n for n in numbers if n in winning]
    
    if len(winners) > 0:
        print("Found", len(winners), "winning numbers:", winners)
        cumsum += card_counter[ix] * 2 ** ( len(winners) - 1 ) 
    
    for i in range(ix+1, ix+len(winners)+1):
        card_counter[i] += card_counter[ix] 

    print(card_counter)
    print()
    

        
        

print("> Result is", cumsum)

print(sum(card_counter))