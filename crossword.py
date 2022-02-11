import json
import numpy as np
import random
from datetime import datetime
startTime = datetime.now()

f = open("json_data.json")
dictionary = json.load(f)
words = list(dictionary.keys())


''' Creating the less than 6 word dictionary

less_than_6_words = {}

f = open("dictionary.json")
dictionary = json.load(f)
words = list(dictionary.keys())
for word in words:
    if len(word) <= 6:
        #if ("Z" in word or "Q" in word or "J" in word or "X" in word or "K" in word or "V" in word or "B" in word or "Y" in word or "W" in word):
        #    pass
        #else:
        less_than_6_words[word] = dictionary[word]

with open('json_data.json', 'w') as outfile:
    json.dump(less_than_6_words, outfile)
'''


test_crossword = [[1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1]]

#transposed = [[test_crossword[j][i] for j in range(len(test_crossword))] for i in range(len(test_crossword[0]))]

def get_crossword_words(template):

    horizontal_words = []

    # getting horizontal words

    for a in range(len(test_crossword)):
        new_word = []
        for b in range(len(test_crossword[0])):
            if template[a][b] == 1:
                new_word.append((a, b))
            else:
                if len(new_word) > 0:
                    horizontal_words.append(new_word)
                    new_word = []
        if len(new_word) > 0:
            horizontal_words.append(new_word)
            new_word = []

    transposed = [[template[j][i] for j in range(len(template))] for i in range(len(template[0]))]

    words = []
    # getting vertical words
    for a in range(len(transposed)):
        new_word = []
        for b in range(len(transposed[0])):
            if transposed[a][b] == 1:
                new_word.append((a, b))
            else:
                if len(new_word) > 0:
                    words.append(new_word)
                    new_word = []
        if len(new_word) > 0:
            words.append(new_word)
            new_word = []

    flipped_words = []
    for word in words:
        flipped_word = []
        for coord in word:
            flipped_coord = (coord[1], coord[0])
            flipped_word.append(flipped_coord)
        flipped_words.append(flipped_word)


    for word in flipped_words:
        horizontal_words.append(word)
    return horizontal_words





def print_crossword(template):
    for row in template:
        printed_row = ""
        for square in row:
            if square == 1:
                printed_row += "[ ]"
            else:
                printed_row += "[X]"
        print(printed_row)

def actual_print_crossword(template):
    for row in template:
        printed_row = ""
        for square in row:
            if square == 0:
                printed_row += "[ ]"
            else:
                printed_row += "[" + str(square) + "]"

        print(printed_row)

def print_crossword_as_list(template):
    for row in template:
        printed_row = ""
        for square in row:
            if square == 0:
                printed_row += "\" \","
            else:
                printed_row += "\"" + str(square) + "\","

        print(printed_row)

print_crossword(test_crossword)
words_coords = get_crossword_words(test_crossword)
print(words_coords)

template_crossword = [[1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1]]

def generate_definitions(words_coords, template):
    across = {} # 'key is int 1 across, value is definition'
    down = {}
    for word_coords in words_coords:
        if len(word_coords) == 1:
            continue
        if word_coords[0][0] == word_coords[1][0]:
            # horizontal
            word = ""
            for letter_coord in word_coords:
                word += str(template[letter_coord[0]][letter_coord[1]])
            if word in words:
                across[word_coords[0][0]] = dictionary[word]

        else:
            # vertical
            word = ""
            for letter_coord in word_coords:
                word += str(template[letter_coord[0]][letter_coord[1]])
            if word in words:
                down[word_coords[0][0]] = dictionary[word]
    return (across, down)




def find_perpendicular_word(words_coords, coord, curr):
    for word_coords in words_coords:
        if coord in word_coords and coord != curr:
            return word_coords

def is_word(word):
    if word in words:
        return True
    else:
        return False

def generate_new_word(word, index): # returns list of viable new words switching letter of word at index
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    viable_words = []
    for letter in alphabet:
        new_string = word[:index] + letter + word[index + 1:]
        if is_word(new_string):
            viable_words.append(new_string)
    return viable_words

def generate_all_possible_words_helper(all_possible_words):
    zero_index = all_possible_words[0].index('0')
    return_array = []
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    for word in all_possible_words:
        for letter in alphabet:
            new_string = word[:zero_index] + letter + word[zero_index + 1:]
            return_array.append(new_string)

    return return_array


def generate_all_possible_words(word):
    all_possible_words = [word]
    return all_possible_words # comment this out later
    while ("0" in all_possible_words[0]):
        apw = generate_all_possible_words_helper(all_possible_words)
        all_possible_words = list(set(apw) - set(all_possible_words))

    if len(all_possible_words) == 1:
        return all_possible_words

    actual_return = []
    for word in all_possible_words:
        if is_word(word):
            actual_return.append(word)
    return actual_return






    '''
    
    word is "000d"
    first append swapping first 0 with all letters (passing in [word]), adding it to all_possible_words -> all possible words is now [000d, a00d, b00d, c00d, ... z00d] . remove elements from previous list
    (e.g. 000d) s.t. all possible words is just [a00d, b00d, ... z00d]
    then pass result of ^ to function again, and then all_possible_words becomes [a00d, ... z00d, aa0d, ab0d, ac0d, ... za0d, zb0d, ... zz0d]
    Remove previous [a00d, b00d, ... z00d] and run again s.t. all_possible_words is [aaad, aabd, aacd, ... zzad, zzbd, zzcd]
    Repeat until no 0 in first element of all_possible_words
    '''

def populate_crossword(words_coords):
    temp_crossword = [[1, 1, 1, 1, 0, 1, 1, 1],
                          [1, 1, 1, 0, 0, 1, 1, 1],
                          [1, 1, 1, 0, 1, 1, 1, 1],
                          [0, 0, 1, 1, 0, 1, 1, 0],
                          [1, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 0, 1, 1, 1],
                          [0, 1, 0, 1, 1, 0, 1, 1],
                          [0, 1, 1, 1, 0, 1, 1, 1],
                          [1, 1, 1, 1, 0, 1, 1, 1]]

    random.shuffle(words_coords)

    number_of_words_made_through = -1
    for word_coords in words_coords:
        number_of_words_made_through += 1
        word_length = len(word_coords)
        # Find constraints of the current word we're assessing
        constraints = [""] * word_length
        index = 0
        for coord in word_coords:
            if temp_crossword[coord[0]][coord[1]] != 1:
                constraints[index] = temp_crossword[coord[0]][coord[1]]
            index += 1
        #print(word_coords, constraints)

        # Find word in dictionary that satisfies these constraints
        viable_words = []
        for word in words:
            if len(word) != word_length:
                continue

            index = 0

            word_found = True
            for constraint in constraints:
                if constraint != "" and constraint != word[index]:
                    word_found = False
                index += 1

            if word_found:
                viable_words.append(word)

        if len(viable_words) == 0:

            done = False

            # here I'd have to change each letter and see if it a) makes it a viable word and b) keeps the dependency (the perpendicular row / column word) as a viable word

            current_word = ""
            for letter_coord in word_coords:
                if type(temp_crossword[letter_coord[0]][letter_coord[1]]) == type(1):
                    current_word += str(0) # this part can be optimized actually
                else:
                    current_word += temp_crossword[letter_coord[0]][letter_coord[1]]

            current_word_array = generate_all_possible_words(current_word)

            for _current_word in current_word_array:
                if done:
                    break

                index = 0 # word_coords[index] = the one we are changing
                for letter_index in range(len(_current_word)):
                    if done:
                        break
                    viable_words_2 = generate_new_word(_current_word, letter_index) # letter_index is index being changed
                    for w in viable_words_2:
                        perpendicular = find_perpendicular_word(words_coords, word_coords[index], word_coords)

                        perpendicular_word = ""
                        for letter_coord in perpendicular:
                            perpendicular_word += temp_crossword[letter_coord[0]][letter_coord[1]]
                        perp_index = perpendicular.index(word_coords[index])
                        modified_perpendicular = perpendicular_word[:perp_index] + w[letter_index] + perpendicular_word[perp_index + 1:]

                        if is_word(modified_perpendicular):
                            temp_crossword[word_coords[index][0]][word_coords[index][1]] = w[letter_index]
                            done = True
                            break
                    index += 1

            if (not done):
                actual_print_crossword(temp_crossword)
                print("======== No viable words found for", word_coords, " ========")
                print("======== Made it through", number_of_words_made_through, "words =========")
                print_crossword_as_list(temp_crossword)
                definitions = generate_definitions(words_coords, temp_crossword)
                across = definitions[0]
                down = definitions[1]
                print("across:")
                print(across)
                print("down:")
                print(down)
                return number_of_words_made_through








        else:
            random_word = random.choice(viable_words)
            index = 0
            for coord in word_coords:
                temp_crossword[coord[0]][coord[1]] = random_word[index]
                index += 1

    actual_print_crossword(temp_crossword)
    return True


print(template_crossword)

populate_crossword(words_coords)

# 39 words currently

tries = 0
best_run = 0
while(True):

    tries += 1


    return_value = populate_crossword(words_coords)
    if type(return_value) == type(True):
        print("Succeeded after " + str(tries) + "tries, hit rate of " + str(1/tries) + ", process took " + str(datetime.now() - startTime))
        break
    else:
        if return_value > best_run:
            best_run = return_value

    if tries > 300:
        print("Failed after " + str(tries) + "tries, hit rate of " + str(1 / tries) + ", process took " + str(
            datetime.now() - startTime))
        print("Best run was", best_run, "words")
        break


#actual_print_crossword(template_crossword)

