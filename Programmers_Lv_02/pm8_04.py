from itertools import product

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for i in alphabet:
        dictionary.append(i)

    for i in range(2, 6):
        for j in product(alphabet, repeat=i): # Redundant permutation
            alphabet_pro = ''.join(j) # Switch tuples to string form
            dictionary.append(alphabet_pro)

    dictionary.sort() # Sort in dictionary order
    index = dictionary.index(word) # find index the word in the dictionary

    return index + 1