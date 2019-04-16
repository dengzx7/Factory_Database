# util.py
# some useful functions

def getIndex(name, list):
	for i in range(len(list)):
		if name == list[i]:
			return i
	return None

def showResults(table, AList, attribute, results):
	# show results
	print ('')
	print ('Table', table)
	print ('-----------------------------------')
	if attribute == '*':
		attribute = ''
		for A in AList:
			attribute += A + '\t'
	print (attribute)
	print ('-----------------------------------')
	for row in results:
		for value in row:
			print (value, end='\t')
		print ('')
	print ('-----------------------------------')
