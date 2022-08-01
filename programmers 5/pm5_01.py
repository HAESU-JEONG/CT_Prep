def solution (card):
    w, h = 0, 0 #width, hight
    for i in range(len(card)): #repeat as much as card list's length 
        if card[i][0] < card[i][1] : # if card[i][0] ia smaller than card[i][1]
            card[i][0], card[i][1] = card[i][1],  card[i][0] #change their seats
        
        w = max(w, card[i][0]) #compare original w and card[i][0] and put the big one in the 'w'
        h = max(h, card[i][1]) #compare original h and card[i][1] and put the big one in the 'h'
        
    return w * h # return w * h