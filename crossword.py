import json
import numpy as np
import random
from datetime import datetime
startTime = datetime.now()
import copy
from datetime import date
from datetime import timedelta

f = open("dictionary.json")
dictionary = json.load(f)
words = list(dictionary.keys())

def find_word_test(number_of_letters, requirements):
    # requirements is key: string index, value: required letter for that string index
    possible_words = []
    for word in words:
        if len(word) != number_of_letters:
            possible_words.append(word)
    for word in possible_words:
        for requirement in list(requirements.keys()):
            if word[requirement] != requirements[requirement]:
                possible_words.remove(word)

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

#transposed = [[test_crossword[j][i] for j in range(len(test_crossword))] for i in range(len(test_crossword[0]))]

def get_crossword_words_seperated_by_hor_vert(template):
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

    vertical_words = flipped_words
    return (horizontal_words, vertical_words)


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

    vertical_words = flipped_words

    for word in flipped_words:
        horizontal_words.append(word)

    ignore = ''' removing in case there are gaps somehow
    print("horizontal_words rn is", horizontal_words)
    for wc in horizontal_words:
        previous_x = -1
        previous_y = -1
        print("===========")
        print(wc)
        print("===========")
        for coord in wc:
            if coord == wc[0]:
                previous_x = coord[0]
                previous_y = coord[1]
            else:
                print("previous_x is", previous_x, "previous_y is", previous_y)
                print("curr x is", coord[0], "curr y is", coord[1])
                if (abs(previous_x - coord[0]) != 1 and abs(previous_x - coord[0]) != 0) or (abs(previous_y - coord[1]) != 1 and abs(previous_y - coord[1]) != 0):
                    print("removing", wc)
                    horizontal_words.remove(wc)
                    break
                else:
                    previous_x = coord[0]
                    previous_y = coord[1]
    '''

    word_list = []
    for wc in horizontal_words:
        if len(wc) > 1:
            word_list.append(wc)

    return word_list





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
      #  printed_row = "["
        printed_row = ""
        for square in row:
            if square == 0:
                printed_row += "\" \","
            else:
                printed_row += "\"" + str(square) + "\","

       # printed_row = printed_row[:-1]
        print(printed_row)

# TEMPLATE DEFINITIONS

ignore = '''

NUM_WORDS_MINIMUM = 9

test_crossword = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1]]


print_crossword(test_crossword)
words_coords = get_crossword_words(test_crossword)

print("GET_CROSSWORD_WORDS:")
print(words_coords)

_t = get_crossword_words_seperated_by_hor_vert(test_crossword)
horizontal_words_coords = _t[0]
vertical_words_coords = _t[1]

template_crossword = copy.deepcopy(test_crossword)

'''

def get_word(word_coords, template):
    word = ""
    for letter in word_coords:
        word += template[letter[0]][letter[1]]
    return word


def generate_definitions(words_coords, template):
    across = {} # 'key is int 1 across, value is definition'
    down = {}

    definitions = {}
    #print("len_words_coords is", len(words_coords), words_coords)
    for word_coords in words_coords:
        #if len(word_coords) == 1:
        #    continue

        if len(word_coords) <= 1:
            continue
        word = ""
        for letter_coord in word_coords:
            word += str(template[letter_coord[0]][letter_coord[1]])
        #print("word is", word, "in dictionary: ", (word in words))

        if word in words:

            definitions[word] = (word_coords, dictionary[word])
        ignore = '''
        if word_coords[0][0] == word_coords[1][0]:
            # horizontal

            if word in words:
                across[word_coords[0][0]] = dictionary[word]

        else:
            # vertical

            if word in words:
                down[word_coords[0][0]] = dictionary[word]
                '''
   # print("across has", len(across.keys()), "down has", len(down.keys()))
   # return (across, down)
    return definitions




def find_perpendicular_word(_words_coords, coord, curr):
    for word_coords in _words_coords:
        if coord in word_coords and word_coords != curr: # used to be coord != curr
            #print("in find_perpendicular given", curr, "returning", word_coords)
            return word_coords

def find_perpendicular_word_definitions(_words_coords, coord, curr):
    for word_coords in _words_coords:
        if coord in word_coords and word_coords != curr:
            #print("in find_perpendicular given", curr, "returning", word_coords)
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

def populate_crossword(words_coords, GLOBAL_DAYS_FROM_START, _temp_crossword, NUM_WORDS_MINIMUM, NOW):

    temp_crossword = copy.deepcopy(_temp_crossword)
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
                #actual_print_crossword(temp_crossword)
                #print("======== No viable words found for", word_coords, " ========")
                print("======== Made it through", number_of_words_made_through, "words =========")

                if number_of_words_made_through >= NUM_WORDS_MINIMUM:

                    #timestamp stuff
                    GLOBAL_DAYS_FROM_START = GLOBAL_DAYS_FROM_START + 1

                    crossword_date = NOW - timedelta(days=GLOBAL_DAYS_FROM_START)
                    timestamp = int(datetime.timestamp(crossword_date))*1000
                    print_crossword_as_list(temp_crossword)

                    new_temp_crossword = []
                    for a in range(len(temp_crossword)):
                        t = []
                        for b in range(len(temp_crossword[0])):
                            if temp_crossword[a][b] == 0:
                                t.append(" ")
                            elif temp_crossword[a][b] == 1:
                                t.append("E")
                            else:
                                t.append(temp_crossword[a][b])
                        new_temp_crossword.append(t)
                        t = []
                    temp_crossword = copy.deepcopy(new_temp_crossword)
                    crossword_string = "{\n"
                    print("{")
                    print("done_crossword:", temp_crossword, ",")
                    #crossword_string += "date: " + str(timestamp) + ",\n"
                    crossword_string += "date: " + "TIMESTAMP_GOES_HERE" + ",\n"
                    crossword_string += "done_crossword: " + repr(temp_crossword) + ",\n"

                    definitions = generate_definitions(words_coords, temp_crossword)

                    test = generate_word_numbers(temp_crossword, definitions, temp_crossword)
                    #print("horizontal:", test[0])
                    #print("vertical:", test[1])
                    print("grid_numbers:", test[2], ",")
                    crossword_string += "grid_numbers: " + repr(test[2]) + ",\n"
                    horizontal_definitions = get_definitions_from_generated_word_numbers(test[0])
                    vertical_definitions = get_definitions_from_generated_word_numbers(test[1])

                    print("across_definitions:", horizontal_definitions, ",")
                    print("down_definitions:", vertical_definitions, ",")
                    crossword_string += "down_definitions: " + repr(horizontal_definitions) + ",\n"
                    crossword_string += "across_definitions: " + repr(vertical_definitions) + ",\n" #these are flipped for whatever reason
                    crossword_string += "},\n"
                    print("}")

                    file1 = open("myfile.txt", "a")  # append mode
                    file1.write(crossword_string)
                    file1.close()



                    #print(definitions)
                return number_of_words_made_through

        else:
            random_word = random.choice(viable_words)
            index = 0
            for coord in word_coords:
                temp_crossword[coord[0]][coord[1]] = random_word[index]
                index += 1

    actual_print_crossword(temp_crossword)
    if number_of_words_made_through >= NUM_WORDS_MINIMUM:
        print('done', number_of_words_made_through)

        GLOBAL_DAYS_FROM_START = GLOBAL_DAYS_FROM_START + 1

        crossword_date = NOW - timedelta(days=GLOBAL_DAYS_FROM_START)
        timestamp = int(datetime.timestamp(crossword_date)) * 1000
        print_crossword_as_list(temp_crossword)

        new_temp_crossword = []
        for a in range(len(temp_crossword)):
            t = []
            for b in range(len(temp_crossword[0])):
                if temp_crossword[a][b] == 0:
                    t.append(" ")
                elif temp_crossword[a][b] == 1:
                    t.append("E")
                else:
                    t.append(temp_crossword[a][b])
            new_temp_crossword.append(t)
            t = []
        temp_crossword = copy.deepcopy(new_temp_crossword)
        crossword_string = "{\n"
        print("{")
        print("done_crossword:", temp_crossword, ",")
        #crossword_string += "date: " + str(timestamp) + ",\n"
        crossword_string += "date: " + "TIMESTAMP_GOES_HERE" + ",\n"
        crossword_string += "done_crossword: " + repr(temp_crossword) + ",\n"

        definitions = generate_definitions(words_coords, temp_crossword)

        test = generate_word_numbers(temp_crossword, definitions, temp_crossword)
        # print("horizontal:", test[0])
        # print("vertical:", test[1])
        print("grid_numbers:", test[2], ",")
        crossword_string += "grid_numbers: " + repr(test[2]) + ",\n"
        horizontal_definitions = get_definitions_from_generated_word_numbers(test[0])
        vertical_definitions = get_definitions_from_generated_word_numbers(test[1])

        print("across_definitions:", horizontal_definitions, ",")
        print("down_definitions:", vertical_definitions, ",")
        crossword_string += "down_definitions: " + repr(horizontal_definitions) + ",\n"
        crossword_string += "across_definitions: " + repr(
            vertical_definitions) + ",\n"  # these are flipped for whatever reason
        crossword_string += "},\n"
        print("}")

        file1 = open("myfile.txt", "a")  # append mode
        file1.write(crossword_string)
        file1.close()

        return True
    else:
        print("returning", number_of_words_made_through)
        return number_of_words_made_through

#populate_crossword(words_coords)

# 39 words currently

print("=== TESTING DONE ===")
ignore = '''
done_crossword = [["P","E","C","K"," ","A","N","T"],
["O","H","M"," "," ","L","O","O"],
["I","N","G"," ","L","O","I","N"],
[" "," ","T","H"," ","W","E"," "],
["W"," "," "," "," "," "," ","W"],
["S","T","E","M"," ","Z","A","X"],
[" ","A"," ","H","O"," ","M","O"],
[" ","B","E","E"," ","L","I","M"],
["F","U","N","K"," ","O","A","R"]]
'''
'''
["P","E","C","K"," ","A","N","T"],
["O","H","M"," "," ","L","O","O"],
["I","N","G"," ","L","O","I","N"],
[" "," ","T","H"," ","W","E"," "],
["W"," "," "," "," "," "," ","W"],
["S","T","E","M"," ","Z","A","X"],
[" ","A"," ","H","O"," ","M","O"],
[" ","B","E","E"," ","L","I","M"],
["F","U","N","K"," ","O","A","R"]
'''
#done_words_coords = [[(0, 7), (1, 7), (2, 7)], [(3, 5), (3, 6)], [(6, 4)], [(8, 0), (8, 1), (8, 2), (8, 3)], [(6, 3), (6, 4)], [(7, 5), (7, 6), (7, 7)], [(5, 2)], [(2, 4), (2, 5), (2, 6), (2, 7)], [(2, 4)], [(6, 6), (6, 7)], [(4, 7)], [(0, 0), (1, 0), (2, 0)], [(1, 5), (1, 6), (1, 7)], [(6, 1)], [(5, 1), (6, 1), (7, 1), (8, 1)], [(0, 6), (1, 6), (2, 6), (3, 6)], [(3, 2), (3, 3)], [(3, 3)], [(4, 0)], [(8, 0)], [(5, 5), (5, 6), (5, 7)], [(8, 5), (8, 6), (8, 7)], [(0, 3)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(5, 5)], [(7, 5), (8, 5)], [(0, 5), (0, 6), (0, 7)], [(7, 1), (7, 2), (7, 3)], [(7, 2), (8, 2)], [(0, 5), (1, 5), (2, 5), (3, 5)], [(5, 6), (6, 6), (7, 6), (8, 6)], [(2, 0), (2, 1), (2, 2)], [(1, 0), (1, 1), (1, 2)], [(5, 0), (5, 1), (5, 2), (5, 3)], [(5, 3), (6, 3), (7, 3), (8, 3)], [(4, 0), (5, 0)], [(4, 7), (5, 7), (6, 7), (7, 7), (8, 7)], [(0, 2), (1, 2), (2, 2), (3, 2)], [(0, 1), (1, 1), (2, 1)]]
#done_definitions = generate_definitions(done_words_coords, done_crossword)
#print_crossword_as_list(done_crossword)
# done_definitions key is word, value is [0] the word coords, [1] the definition
#print("done_definitions is", done_definitions, "length of keys is", len(done_definitions.keys()))
#print(done_definitions.keys())

def generate_word_number_positions(across, down, definitions, crossword):
    across_words = across.keys()
    across_positions = {}
    for word in across_words:
        # key is number, value is coord
        across_positions[across[word]] = definitions[word][0][0]
    down_words = down.keys()
    down_positions = {}
    for word in down_words:
        # key is number, value is coord
        down_positions[down[word]] = definitions[word][0][0]

    height = len(crossword)
    width = len(crossword[0])

    returnArray = []

    for a in range(height):
        new = []
        for b in range(width):
            new.append(0)
        returnArray.append(new)

    down_positions_numbers = list(down_positions.keys())
    across_positions_numbers = list(across_positions.keys())

    for d in down_positions_numbers:
        coord = down_positions[d]
        returnArray[coord[0]][coord[1]] = d
    for v in across_positions_numbers:
        coord = across_positions[v]
        returnArray[coord[0]][coord[1]] = v

    # return (across_positions, down_positions)

    return returnArray




def generate_word_numbers(done_crossword, definitions, template):

    # new schema:
    # given the positions of all words, generate numbers for each vertical word first by
    # looking at the first element of the word (the position of first letter) and appending to some dict.
    # then loop through all horizontal words, and if the position of first letter doesn't currently have a key,
    # add that as a new key

    placements_horizontal = {}
    placements_vertical = {}
    index = 1

    coords_with_indexes = {}

    for word_coords in vertical_words_coords:
        if tuple(word_coords[0]) not in list(coords_with_indexes.keys()):
            word = get_word(word_coords, done_crossword)
            if len(word) > 1:
                placements_vertical[index] = get_word(word_coords, done_crossword)
                coords_with_indexes[tuple(word_coords[0])] = index
                index += 1

    for word_coords in horizontal_words_coords:
        if tuple(word_coords[0]) not in list(coords_with_indexes.keys()):
            word = get_word(word_coords, done_crossword)
            if len(word) > 1:
                placements_horizontal[index] = get_word(word_coords, done_crossword)
                coords_with_indexes[tuple(word_coords[0])] = index
                index += 1
        else:
            word = get_word(word_coords, done_crossword)
            if len(word) > 1:
                placements_horizontal[coords_with_indexes[tuple(word_coords[0])]] = get_word(word_coords, done_crossword)

    number_positions = []
    #print("coords_with_indexes is", coords_with_indexes)
    #initialize
    for a in range(len(template)):
        temp_array = []
        for b in range(len(template[0])):
            temp_array.append(0)
        number_positions.append(temp_array)

    #populate with actual number positions
    # for a in range(len(template)):
    #     for b in range(len(template[0])):
    #         if (a, b) in coords_with_indexes:
    #             number_positions[a][b] = coords_with_indexes[(a, b)]
    for key in list(coords_with_indexes.keys()):

        value = coords_with_indexes[key]
        number_positions[key[0]][key[1]] = value

    return (placements_horizontal, placements_vertical, number_positions)

#test = generate_word_numbers(done_crossword, done_definitions, done_crossword)
#print("horizontal:", test[0])
#print("vertical:", test[1])
#print("number positions:", test[2])
#horizontal_definitions = get_definitions_from_generated_word_numbers(test[0])
#vertical_definitions = get_definitions_from_generated_word_numbers(test[1])

#print(horizontal_definitions)
#print(vertical_definitions)

def get_definitions_from_generated_word_numbers(words_dict):

    indexes = words_dict.keys()
    d = {}

    for index in indexes:
        if words_dict[index] in dictionary:
            d[index] = (words_dict[index], dictionary[words_dict[index]].split(".")[0])
        else:
            d[index] = (words_dict[index], "NO DEFINITION")
    # words = words_dict.values()
    # d = {}
    # for word in words:
    #     if word in dictionary:
    #         d[word] = dictionary[word].split(".")[0]
    return d

#horizontal_definitions = get_definitions_from_generated_word_numbers(test[0])
#vertical_definitions = get_definitions_from_generated_word_numbers(test[1])

#print(horizontal_definitions)
#print(vertical_definitions)

# mapping of where to put the positions
#t2 = generate_word_number_positions(test[0], test[1], done_definitions, done_crossword)
#print(t2)

# need a 'if not there, do ur own hint'



tries = 0
best_run = 0
GLOBAL_DAYS_FROM_START = 0

while(True):

    ignore = """
    NUM_WORDS_MINIMUM = 34

    potential_templates = [[[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
[1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0,  1, 1, 1, 1]],
                           [[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]],
                           [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]],
                           [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                            [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]],
                           [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]
                            ]
    """

    potential_templates = [[
[1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
],
        [
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
],

        [
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
],

        [
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
[0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
],

        [[1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]],

        [[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
         [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]],

        [[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]],

        [[1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
         [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
         [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
         [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
         [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]],
        ]





    test_crossword = random.choice(potential_templates)
    NUM_WORDS_MINIMUM = len(get_crossword_words(test_crossword))-5


    # test_crossword_tuple = random.choice(potential_templates)
    # test_crossword_tuple = potential_templates[0]
    # test_crossword = test_crossword_tuple[0]
    # NUM_WORDS_MINIMUM = int(test_crossword_tuple[1]/2) + 3



    #print_crossword(test_crossword)
    words_coords = get_crossword_words(test_crossword)

    # print("GET_CROSSWORD_WORDS:")
    # print(words_coords)

    _t = get_crossword_words_seperated_by_hor_vert(test_crossword)
    horizontal_words_coords = _t[0]
    vertical_words_coords = _t[1]

    template_crossword = copy.deepcopy(test_crossword)



    tries += 1


    return_value = populate_crossword(words_coords, GLOBAL_DAYS_FROM_START, template_crossword, NUM_WORDS_MINIMUM, datetime.now())
    if type(return_value) == type(True):
        GLOBAL_DAYS_FROM_START += 1
        print("Succeeded after " + str(tries) + "tries, hit rate of " + str(1/tries) + ", process took " + str(datetime.now() - startTime))
        # break
    else:
        if return_value > best_run:
            best_run = return_value
            GLOBAL_DAYS_FROM_START += 1
        if return_value >= NUM_WORDS_MINIMUM:
            GLOBAL_DAYS_FROM_START += 1
        print("crossword return value:", return_value)

    if tries > 20000:
        print("Failed after " + str(tries) + "tries, hit rate of " + str(1 / tries) + ", process took " + str(
            datetime.now() - startTime))
        print("Best run was", best_run, "words")
        break


#actual_print_crossword(template_crossword)

