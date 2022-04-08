import time
from customize import ticks_per_frame

with open('list.txt', 'r') as f:
    words_string = f.read()

word_list = words_string.replace('"', '').split(',')

'''
target = None
while not target:
    try:
        user_input = int(input('Target guesses: '))
    except ValueError:
        print('Please enter a positive integer...\n')

    if user_input > 0:
        target = user_input
    else:
        print('Please enter a positive integer...\n')
'''

def get_distinct_letters(word):
    distinct_letters = []
    for letter in word:
        if letter not in distinct_letters:
            distinct_letters.append(letter)
    
    return distinct_letters

for target in range(0, 5):
    viable_words = []
    for word in word_list:
        if len(get_distinct_letters(word)) <= target:
            viable_words.append(word)
    
    print(f"\n\nChecking for grids solvable in {target} guesses.")
    
    l = len(viable_words)
    g = l * (l - 1) * (l - 2) * (l - 3) * (l - 4)
    print(f"There are {len(viable_words)} viable words out of {len(word_list)} total words...")
    print(f"Grids to check: {g}")
    
    ticks = 0
    grids = 1
    spin_pos = 0
    for cw1 in viable_words:
        for cw2 in viable_words:
            if cw2 == cw1:
                continue
            for cw3 in viable_words:
                if cw3 == cw1 or cw3 == cw2:
                    continue
                for cw4 in viable_words:
                    if cw4 == cw3 or cw4 == cw2 or cw4 == cw1:
                        continue
                    for cw5 in viable_words:
                        if cw5 == cw4 or cw5 == cw3 or cw5 == cw2 or cw5 == cw1:
                            continue
                        
                        cw_list = [cw1, cw2, cw3, cw4, cw5]
                        hw1 = ''.join([w[0] for w in cw_list])
                        hw2 = ''.join([w[1] for w in cw_list])
                        hw3 = ''.join([w[2] for w in cw_list])
                        hw4 = ''.join([w[3] for w in cw_list])
                        hw5 = ''.join([w[4] for w in cw_list])
                        hw_list = [hw1, hw2, hw3, hw4, hw5]
                        grid = '\n'.join(hw_list)
                        
                        spinner = ['|', '/', '-', '\\']
                        ellipses = ['', '.', '..', '...']
                        
                        print(f"\r{spinner[spin_pos]} | {' '.join(hw_list)} | [{grids}/{g}]{ellipses[spin_pos]}", end="")
                        
                        ticks += 1
                        if ticks == ticks_per_frame:
                            ticks = 0
                            spin_pos += 1
                            
                        if spin_pos == 4:
                            spin_pos = 0
                        
                        grids += 1
                        
                        if hw1 in word_list and hw2 in word_list and hw3 in word_list and hw4 in word_list and hw5 in word_list:
                            print(f"\nVIABLE GRID FOUND:\n{grid}\n\n")
                            

pause = input('')