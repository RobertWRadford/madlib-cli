import re
import os
from madlib import read_template, parse, newWords, merge

fillPattern = re.compile(r'{.*?}')
dirname = os.path.dirname(__file__)
writeFile = os.path.join(dirname, '../assets/madlib_complete.txt')
readFile = os.path.join(dirname, '../assets/madlib_template.txt')

print('Greetings! Let\'s have some fun with MadLibs. I will ask you for some words by grammatical family and then place them into a prebuilt story to find some funny results.')

template = read_template(readFile)
fillIns = parse(template)
userInput = newWords(fillIns)
finished = open(writeFile, 'wt')
finished.write(merge(template, userInput))
finished.close()
print(template)