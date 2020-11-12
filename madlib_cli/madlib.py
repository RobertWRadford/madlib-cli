import re

fillPattern = re.compile(r'{.*?}')

print('Greetings! Let\'s have some fun with MadLibs. I will ask you for some words by grammatical family and then place them into a prebuilt story to find some funny results.')

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

template = read_template('../assets/madlib_template.txt')
fillIns = parse(template)
userInput = newWords(fillIns)
finished = open('../assets/madlib_complete.txt', 'wt')
finished.write(merge(template, userInput))
finished.close()
print(template)