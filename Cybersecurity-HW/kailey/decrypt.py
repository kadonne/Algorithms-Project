import hashlib
#import multiprocessing
import time
from itertools import product

def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
	
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return binary_search(arr, low, mid - 1, x)
	else:
		return binary_search(arr, mid + 1, high, x)
	return -1


def symbols_digits(word_list,hash_list,digits,symbols):
	hashed = {}
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				hashed_word = hashlib.sha256(('%s%s%s'%(word,symbols[i],digits[j])).encode()).hexdigest() 
				#store original password to password
				password = '%s%s%s'%(word,symbols[i],digits[j])
				#print(hashed_word, password)
				#store the hash into hashed dictionary as the key and password as the value
				hashed[hashed_word] = password
				# every time 20 million words are computed, compare the hashes and reset the hashed dictionary to save up RAM
				if(len(hashed) >= 20000000):
					compare_hashes(hashed,hash_list)
					hashed = {}
	# compare remaining combinations in case hashed dictionary's length > 0 and < 20million
	compare_hashes(hashed,hash_list)

def digits_symbols(word_list,hash_list,digits,symbols):
	hashed = {}
	for word in word_list:
		word = word.strip()
		for i in range(0,len(symbols)):
			for j in range(0,len(digits)):
				#for every word read from word_list, convert to hash using sha256 and store to hashed_word
				hashed_word = hashlib.sha256(('%s%s%s'%(word,digits[j],symbols[i])).encode()).hexdigest() 
				#store original password to password
				password = '%s%s%s'%(word,digits[j],symbols[i])
				#print(hashed_word, password)
				#store the hash into hashed dictionary as the key and password as the value
				hashed[hashed_word] = password
				# every time 20 million words are computed, compare the hashes and reset the hashed dictionary to save up RAM
				if(len(hashed) >= 20000000):
					compare_hashes(hashed,hash_list)
					hashed = {}
	# compare remaining combinations in case hashed dictionary's length > 0 and < 20million
	compare_hashes(hashed,hash_list)

def compare_hashes(hashed,hash_list):
	global decrypted_passwords 

	# sort the computed hashed dictionary from digit_symbol and symbol_digit functions
	sorted_hashed = sorted(hashed.items(), key=lambda x:x[0])
	# flatten the dictionary so all the keys are stored into a 1D array
	keys = [r[0] for r in sorted_hashed]

	# print out first element to see progress for the running code
	#print(sorted_hashed[0])
	
	for word in hash_list:
		try:
			# take each hash in hash_list (Hashes1.txt, 100 hashes) and see if it's in one of the 20million hashes inside hashed dictionary
			# using binary search
			# if there are no matches, program will throw an exception and won't enter the if statement 
			hashes_word = sorted_hashed[binary_search(keys,0,len(keys)-1,word)]
			found = True
		except Exception:
			found = False
		# if one of the 100 hashes is present in the dictionary, write to passwords1.txt along with the original password
		if found:
			#decrypted_passwords['%s %s\n'%(hashes_word[0],hashes_word[1])]
			decrypted_passwords[hashes_word[0]] = hashes_word[1]+'\n'
			#print('%s %s'%(word,hashes_word[1]))
			#hash_list.remove(word)
	for i in decrypted_passwords:
		if i in hash_list:
			hash_list.remove(i)

if __name__=='__main__':
	decrypted_passwords = {}

	symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>']
	digits = ['0','1','2','3','4','5','6','7','8','9']
	
	hash_file = open('encrypted_passwords.txt','r')

	#append every word in the Hashes.txt (100 hashed passwords that were given)
	hash_list = list()
	for word in hash_file.readlines():
		hash_list.append(word.split(' ')[0])
	hash_file.close()

	file1 = open('words.txt','r')
	# store all lines full of LEET SPEAK combinations that were converted from the original wordlist full of 140,000 english words with length greater than 10
	word_list = file1.readlines()
	file1.close()
	symbols_digits(word_list,hash_list,digits,symbols)
	digits_symbols(word_list,hash_list,digits,symbols)

	write_file = open('decrypted_passwords.txt','w')

	for i in decrypted_passwords: write_file.writelines(i + ' ' + decrypted_passwords[i])
	write_file.close()


	print('done')