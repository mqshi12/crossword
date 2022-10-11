import json
import ast
import random
import re

# initializing stuff for replacing 'no definition'
num_to_alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
                   'E': 5, 'F': 6, 'G': 7, 'H': 8,
                   'I': 9, 'J': 10, 'K': 11, 'L': 12,
                   'M': 13, 'N': 14, 'O': 15, 'P': 16,
                   'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                   'U': 21, 'V': 22, 'W': 23, 'X': 24,
                   'Y': 25, 'Z': 26, '-' : '-'}

military = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
                   'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
                   'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
                   'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
                   'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
                   'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-Ray',
                   'Y': 'Yankee', 'Z': 'Zulu', '-': '-'}

def word_to_num(word): # returns clue with word for num
    t = []
    for char in word:
        t.append(num_to_alphabet[char])
    return_str = ""
    for num in t:
        return_str += str(num) + " - "
    return return_str[:-3]

def word_to_military(word): # returns clue with word for military
    t = []
    for char in word:
        t.append(military[char])
    return_str = ""
    for s in t:
        return_str += s + "--"
    return return_str[:-2]


def opposite(word): # returns clue that's like 'The opposite of ' + flipped word
    t = []
    for char in word:
        t.append(char)
    t.reverse()
    reversed = ""
    for char in t:
        reversed += char
    return "The opposite of " + reversed + ""

def reverse(word): # returns clue that's like 'The opposite of ' + flipped word
    t = []
    for char in word:
        t.append(char)
    t.reverse()
    reversed = ""
    for char in t:
        reversed += char
    return "What happens when you put " + reversed + " in reverse"

def anagram(word): # returns clue that's like "anagram of " + word
    shuffled = ''.join(random.sample(word, len(word)))
    return "Anagram of '" + shuffled + "'"

print(word_to_num('HELLO'))
print(word_to_military('HELLO'))
print(opposite('HELLO'))
print(reverse('HELLO'))
print(anagram('HELLO'))

# Opening JSON file
f = open('all_crosswords.txt', "r")

t = f.read()

for i in range(100):
    t = t.replace("\n\n", "\n")

temp = t.split("},\n{")

temp.reverse()

print("number of crosswords:", len(temp))

START_TIMESTAMP = 1689897600000 # July 1 2020

failed = 0
attempted = 0

for json_string in temp:
    attempted += 1
    try:
        if 'date' not in json_string or 'done_crossword' not in json_string or 'grid_numbers' not in json_string or 'down_definitions' not in json_string or 'TIMESTAMP_GOES_HERE' not in json_string:
            continue

        if json_string[0] == "{":
            pass
        else:
            json_string = "{" + json_string
        json_string += "}"
        json_string = json_string.replace("date", "\"date\"")
        json_string = json_string.replace("done_crossword", "\"done_crossword\"")
        json_string = json_string.replace("grid_numbers", "\"grid_numbers\"")
        json_string = json_string.replace("down_definitions", "\"down_definitions\"")
        json_string = json_string.replace("across_definitions", "\"across_definitions\"")
        json_string = json_string.replace("TIMESTAMP_GOES_HERE", "\"TIMESTAMP_GOES_HERE\"")
        # print(json_string)
        res = ast.literal_eval(json_string)
        # print(res, type(res))

        down_definitions = res["down_definitions"]
        for k in down_definitions.keys():
            word = down_definitions[k][0]
            definition = down_definitions[k][1]
            if definition == 'NO DEFINITION':
                new_definition = ""
                hint_random = random.randint(0, 5)
                if hint_random == 0:
                    new_definition = word_to_num(word)
                elif hint_random == 1:
                    new_definition = word_to_military(word)
                elif hint_random == 2:
                    new_definition = opposite(word)
                elif hint_random == 3:
                    new_definition = reverse(word)
                else:
                    new_definition = anagram(word)

                down_definitions[k] = (word, new_definition)

        across_definitions = res["across_definitions"]
        for k in across_definitions.keys():
            word = across_definitions[k][0]
            definition = across_definitions[k][1]
            if definition == 'NO DEFINITION':
                new_definition = ""
                hint_random = random.randint(0, 5)
                if hint_random == 0:
                    new_definition = word_to_num(word)
                elif hint_random == 1:
                    new_definition = word_to_military(word)
                elif hint_random == 2:
                    new_definition = opposite(word)
                elif hint_random == 3:
                    new_definition = reverse(word)
                else:
                    new_definition = anagram(word)

                across_definitions[k] = (word, new_definition)



        s = str(res)
        s = s.replace("\'date\'", "date", )
        s = s.replace("\'done_crossword\'", "done_crossword")
        s = s.replace("\'grid_numbers\'", "grid_numbers")
        s = s.replace("\'down_definitions\'", "down_definitions")
        s = s.replace("\'across_definitions\'", "across_definitions")
        s = s.replace("\'TIMESTAMP_GOES_HERE\'", str(START_TIMESTAMP))
        # print(s)

        print("done:", s)

        file1 = open("sanitized_crosswords.txt", "a")  # append mode
        file1.write(s)
        file1.write(",\n\n")
        file1.close()

        START_TIMESTAMP -= 86400000
    except:
        print('failed once')
        failed += 1

print("total failed:", failed)
print("total attempted:", attempted)



    # remember to remove quotes around key names for converting back to json / .txt
    #break



# json_string = "{\"crosswords\": " + t + "}"
#
# json_string = json_string.replace("date", "\"date\"")
# json_string = json_string.replace("done_crossword", "\"done_crossword\"")
# json_string = json_string.replace("grid_numbers", "\"grid_numbers\"")
# json_string = json_string.replace("down_definitions", "\"down_definitions\"")
# json_string = json_string.replace("across_definitions", "\"across_definitions\"")
# json_string = json_string.replace("'", "\"")
# json_string = json_string.replace("TIMESTAMP_GOES_HERE", "1")
#
# print(json_string[1110:1115])
# print(json_string)
# temp = json.loads(json_string)
# print(temp)

# Iterating through the json
# list

f.close()
# for i in data['emp_details']:
#     print(i)
#
# # Closing file
# f.close()