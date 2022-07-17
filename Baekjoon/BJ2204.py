while True:
    testCase = int(input())

    if testCase == 0:
        break
        
    word = []
    for i in range(testCase):
        word.append(input())
    
    word.sort(key=str.lower) # change input string to lower alphabet
    print(word[0])