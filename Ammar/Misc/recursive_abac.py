import threading 



def recursive(index,j, i,target,leet,sentinel,temp):

	if(j==-1):
		return

	for z in range(index, len(temp)):
		if(temp[z]==target):
			if (sentinel==i):
				temp[z] = leet
				recursive(z,j-1,i,target,leet,sentinel,temp)
				break
			sentinel+=1
	
def recursive_threading(target, leet, name_of_file):

	read = open('%s'%(name_of_file),'r')
	words = read.readlines()
	read.close()

	f = open('%s'%(name_of_file),'a')



	for word in words:
		temp = list(word)
		count = 0
		sentinel = 0
		
		for i in range(0,len(temp)):
			if(temp[i]==target):
				count+=1
		
		for j in range(0, count):
			for i in range(0, count-j):
				recursive(0,j,i,target,leet,sentinel,temp)
		
				sentinel = 0
				f.write(''.join(temp))
				temp = list(word)
	f.close()
def multi_threaded(name_of_file):
	symbols = ['s','a','l','e','t','i','o','b','g']
	leet = ['$','4','1','3','7','1','0','8','9']
	
	for i in range(0,len(symbols)):
		recursive_threading(symbols[i],leet[i], name_of_file)
	

#t1 = threading.Thread(target=multi_threaded, args=('LEET/lowercased.txt',))
t2 = threading.Thread(target=multi_threaded, args=('LEET/capitalized.txt',))
#t1.start()
t2.start()
