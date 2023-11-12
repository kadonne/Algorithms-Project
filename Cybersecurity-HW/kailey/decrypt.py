import hashlib
from self_balancing_tree import SelfBalancingTree
import time

def symbols_digits(word_list,hash_list,digits,symbols):
	global t
	t0 = time.time()
	tree = SelfBalancingTree()
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				hashed_word = hashlib.sha256(('%s%s%s'%(word,symbols[i],digits[j])).encode()).hexdigest() 
				#store original password to password
				password = '%s%s%s'%(word,symbols[i],digits[j])
				tree.insert_key(hashed_word, password)
	t[0] = t[0]+time.time()-t0
	compare_hashes(tree, hash_list)

def digits_symbols(word_list,hash_list,digits,symbols):
	global t
	t0 = time.time()
	tree = SelfBalancingTree()
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				hashed_word = hashlib.sha256(('%s%s%s'%(word,digits[j],symbols[i])).encode()).hexdigest() 
				#store original password to password
				password = '%s%s%s'%(word,digits[j],symbols[i])
				tree.insert_key(hashed_word, password)
	t[0] = t[0]+time.time()-t0
	compare_hashes(tree, hash_list)

def compare_hashes(tree, hash_list):
	global t
	global decrypted_passwords
	t0 = time.time()

	for word in hash_list:
		hashes_word = tree.search_key(word)
		# if one of the 100 hashes is present in the dictionary, write to passwords1.txt along with the original password
		if hashes_word != None:
			decrypted_passwords[hashes_word[0]] = hashes_word[1]
	for i in decrypted_passwords:
		if i in hash_list:
			hash_list.remove(i)
	t[1] = t[1]+time.time()-t0

				
if __name__=='__main__':
	decrypted_passwords = {}
	t = [0,0,0]

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
t0 = time.time()
symbols_digits(word_list,hash_list,digits,symbols)
digits_symbols(word_list,hash_list,digits,symbols)
t[2] = t[2]+time.time()-t0

write_file = open('decrypted_passwords.txt','w')
for i in decrypted_passwords: 
	write_file.writelines(i + ' ' + decrypted_passwords[i]+'\n')
write_file.close()

#print('done')
print('Insert time:\t%fs'%(t[0]))
print('Search time:\t%fs'%(t[1]))
#print('Total time:\t%fs'%(t[2]))