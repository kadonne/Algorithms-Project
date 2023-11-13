import hashlib
from tries import Trie
import time
import sys

def hash_it(hash_function, password):
	if hash_function == 32:
		return str(hashlib.md5(password.encode()).hexdigest())
	elif hash_function == 40:
		return str(hashlib.sha1(password.encode()).hexdigest())
	elif hash_function == 56:
		return str(hashlib.sha224(password.encode()).hexdigest())
	elif hash_function == 64:
		return str(hashlib.sha256(password.encode()).hexdigest())
	elif hash_function == 96:
		return str(hashlib.sha384(password.encode()).hexdigest())
	return ''


def symbols_digits(word_list,hash_list,digits,symbols):
	global t
	t0 = time.time()
	
	tree = Trie()
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				password = '%s%s%s'%(word,symbols[i],digits[j])
				hashed_word = hash_it(int(sys.argv[1]), password)
				tree.insert(hashed_word, password)
	t[0] = t[0]+time.time()-t0

	compare_hashes(tree, hash_list)

def digits_symbols(word_list,hash_list,digits,symbols):
	global t
	t0 = time.time()
	tree = Trie()
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				password = '%s%s%s'%(word,symbols[i],digits[j])
				hashed_word = hash_it(int(sys.argv[1]), password)
				tree.insert(hashed_word, password)
	t[0] = t[0]+time.time()-t0
	compare_hashes(tree, hash_list)

def compare_hashes(tree, hash_list):
	global t
	global decrypted_passwords
	t0 = time.time()

	for word in hash_list:
		hashes_word = tree.search(word)
		# if one of the 100 hashes is present in the dictionary, write to passwords1.txt along with the original password
		if hashes_word != None:
			decrypted_passwords[hashes_word[0]] = hashes_word[1]
	t[1] = t[1]+time.time()-t0

	for i in decrypted_passwords:
		if i in hash_list:
			hash_list.remove(i)

				
if __name__=='__main__':
	t = [0, 0, 0]
	t0 = time.time()
	decrypted_passwords = {}

	symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>']
	digits = ['0','1','2','3','4','5','6','7','8','9']
	
    #initialize self-balancing tree

hash_file = open('encrypted_passwords.txt','r')

	#append every word in the Hashes.txt (100 hashed passwords that were given)
hash_list = list()
for word in hash_file.readlines():
		hash_list.append(word.strip())
		
hash_file.close()

file1 = open('words.txt','r')
# store all lines full of LEET SPEAK combinations that were converted from the original wordlist full of 140,000 english words with length greater than 10
word_list = file1.readlines()
file1.close()
symbols_digits(word_list,hash_list,digits,symbols)
digits_symbols(word_list,hash_list,digits,symbols)

write_file = open('decrypted_passwords.txt','w')
for i in decrypted_passwords: 
	write_file.writelines(i + ' ' + decrypted_passwords[i]+'\n')
write_file.close()

#print('done')
t[2] = time.time() - t0
print('Insert time:\t%fs'%(t[0]))
print('Search time:\t%fs'%(t[1]))
#print('Total time:\t%fs'%(t[2]))
