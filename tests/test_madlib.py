from madlib_cli.madlib import read_template, parse, newWords, merge
import os

dirname = os.path.dirname(__file__)
testName = os.path.join(dirname, '../assets/test.txt')

def test_read_template():
	actual = read_template(testName)
	expect = 'this is a {test}'
	assert actual == expect

def test_parse():
	actual = parse(read_template(testName))
	expect = ['{test}']
	assert actual == expect

def test_merge():
	actual = merge('this is a {test}', ['string'])
	expect = 'this is a string'
	assert actual == expect