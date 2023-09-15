from itertools import combinations_with_replacement

def do_combinations(string, target, symbol):
	dictionary = {}
	count_indices = {}
	i = 0
	for item in enumerate(string):
		if(item[1] == target):
			count_indices[i] = item[0]
			i+=1
	if(len(count_indices)==0):
		return
	
	for item in combinations_with_replacement(range(len(count_indices)),r=len(count_indices)):
		characters = list(string)
		for i in range(len(item)):
			characters[count_indices[item[i]]] = symbol
		dictionary[''.join(characters)] = 0
		print(dictionary)

	f = open('letters.txt','a')
	for item in dictionary:
		f.write(item)
	f.close()
	
symbols = {'s':'$', 'a': '4', 'l': '1', 'e': '3', 't': '7', 'i': '1', 'o': '0', 'b': '8', 'g': '9'}
for item in symbols:
	f = open('letters.txt','r')
	list_of_words = f.readlines()
	f.close()
	for word in list_of_words:
		do_combinations(word,item,symbols[item])

