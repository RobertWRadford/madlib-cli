import re
import os

fillPattern = re.compile(r'{.*?}')
dirname = os.path.dirname(__file__)
writeFile = os.path.join(dirname, '../assets/madlib_complete.txt')
readFile = os.path.join(dirname, '../assets/madlib_template.txt')

def read_template(path):
	return open(path, 'rt').read()

def parse(template):
	return re.findall(fillPattern, template)

def newWords(fillIns):
	for i in range(len(fillIns)):
		fillIns[i] = input(f'Give me a {fillIns[i][1:len(fillIns[i])-1]}: ')
	return fillIns

def merge(template, filledIn):
	fillIns = parse(template)
	for i in range(len(filledIn)):
		template = template.replace(fillIns[i], filledIn[i], 1)
	return template