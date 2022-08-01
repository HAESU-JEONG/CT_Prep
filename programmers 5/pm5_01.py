def solution (card):
    for i in range(len(card)):
        if card[i][0] < card[i][1] :
            card[i][0], card[i][1] = card[i][1],  card[i][0]
        
        w = max(card[i][0] for i in card)
        h = max(card[i][1] for i in card) 
        
    return w*h