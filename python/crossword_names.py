import pandas as pd
import random
from unidecode import unidecode
import re
import json
# interviews_df = pd.read_csv('pantheon.tsv', sep='\t')
# print(interviews_df)

ans = []
with open("pantheon.tsv") as f:
    # Read data line by line
    for line in f:
        # split data by tab
        # store it in list
        l = line.split('\t')

        # append list to ans
        ans.append(l)

# print data line by line

d = {}

for i in ans:
    name = i[1]
    from_specific = i[3].capitalize()
    from_country = i[5].capitalize()
    job = i[13].lower()

    formats = ["{job} from {from_country}", "famous {job} from {from_country}"] # remember to .capitalize()

    clue_f = random.randint(0, 1)
    clue_f_two = random.randint(0, 1)
    f = ""
    if clue_f_two == 0:
        f = formats[clue_f].format(job=job, from_country=from_country)
    else:
        f = formats[clue_f].format(job=job, from_country=from_specific)
    f = f[0].upper() + f[1:]
    f = unidecode(f)

    clue_r = random.randint(0, 2)
    clue = ""
    if clue_r == 0 or clue_r == 1:
        clue = name
    elif clue_r == 2:
        clue = name.split(" ")[0]
    clue = unidecode(clue)
    clue = clue.replace(" ", "")
    clue = clue.upper()
    regex = re.compile('[^a-zA-Z]')
    # First parameter is the replacement, second parameter is your input string
    clue = regex.sub('', clue)


    d[clue] = f
    print(clue, ":", f)
    #print(i)

with open('names.json', 'w') as outfile:
    json.dump(d, outfile)