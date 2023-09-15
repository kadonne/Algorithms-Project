1) Download a wordlist from the English dictionary as a text file
2) Use python program to convert the wordlist to all lowercase characters and write to lowercase.txt
3) Use python program to convert the worldlist to all capitalized words and write to capitalized.txt
4) Use convert_to_leetspeak.py to use combinations_with_replacement to convert lowercase.txt and capitalized.txt to LEET SPEAK combinations
5) Since lowercase_leetspeak.txt yields around 150million words and capitalized_leetspeak.txt yields around 130million words, I used a python program to separate 
   each file into chunks of 10 million words per file. This ends up having about 15 different files for lowercase, and 13 different files for capitalized all with 
   10 million words each
6) Copy ctf_lowercased.py 14 times and use screen command to run each program multiprocessed. Same thing goes for files with capitalized words, using ctf_cpaitalized.py
7) Program yields 96 passwords.
8) Use python program to convert each of the 96 passwords to ctf_4621{password}2546120 and hash with sha256 and compare to original Hashes.txt with given 100 hashes 
   to see if the passwords are correct, which they are.
