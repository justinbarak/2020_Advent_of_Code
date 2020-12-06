import requests
import json
import sys
from collections import OrderedDict 

def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename))

jsonurl = 'https://adventofcode.com/2020/leaderboard/private/view/1127355.json'
sessionkey = {"session" : load('sessionkey.txt')[0]}

s = requests.Session()
s.cookies.update(sessionkey)
content = s.get(jsonurl)
jcontent = OrderedDict(json.loads(content.text))

scoreboard_temp = [[]]
scoreboard_temp.clear()
for member in jcontent['members']:
    scoreboard_temp.append([jcontent['members'][member]['name'], jcontent['members'][member]["local_score"]])

scoreboard_temp.sort(key = lambda x: x[1], reverse=True)
scoreboard = ""

left_col_width = len(scoreboard_temp[0][0]) + 2

for i, j in scoreboard_temp:
    scoreboard += f"{i:>{left_col_width}}{j:>6}\n"

with open('leaderboard.txt', 'w') as txtFile:
    txtFile.write(scoreboard)

print(scoreboard)