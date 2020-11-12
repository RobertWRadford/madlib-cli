from madlib_cli.madlib import read_template, parse, newWords, merge

def test_read_template():
	actual = read_template('assets/test.txt')
	expect = 'this is a {test}'
	assert actual == expect

def test_parse():
	actual = parse(read_template('assets/test.txt'))
	expect = ['{test}']
	assert actual == expect

def test_merge():
	actual = merge('this is a {test}', ['string'])
	expect = 'this is a string'
	assert actual == expect