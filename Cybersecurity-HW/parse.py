data_file = open("10k_time_sheets.txt",'r')
#data_file = open('time_sheets.txt','r')
data = data_file.readlines()
dictionary_index = 0
bst_index = 0
for i in data:
    #if "Dictionary: 10000" in i:
    if "Dictionary: 10000" in i:
        dictionary_index = data.index(i)+1
for i in data:
    #if "Self-Balancing-Tree: 10000" in i:
    if "Self-Balancing-Tree: 10000" in i:
        bst_index = data.index(i)+1
dictionary_data = data[:dictionary_index]
bst_data = data[dictionary_index:bst_index]
trie_data = data[bst_index:]

dictionary = {}
bst = {}
trie = {}

data_set = ''
for i in dictionary_data:
    if "Dictionary: " in i:
        values = data_set.split('\n')
        value1 = values[0][values[0].find('\t')+1:-1]
        value2 = values[1][values[1].find('\t')+1:-1]
        value3 = values[2][values[2].find('\t')+1:-1]
        dictionary[int(i.split(' ')[1])] = [float(value1), float(value2), float(value3)]
        data_set = ''
        continue
    data_set = data_set + i 

data_set = ''
for i in bst_data:
    if "Self-Balancing-Tree: " in i:
        values = data_set.split('\n')
        value1 = values[0][values[0].find('\t')+1:-1]
        value2 = values[1][values[1].find('\t')+1:-1]
        bst[int(i.split(' ')[1])] = [float(value1), float(value2)]
        data_set = ''
        continue
    data_set = data_set + i 

data_set = ''
for i in trie_data:
    if "Trie-Tree: " in i:
        values = data_set.split('\n')
        value1 = values[0][values[0].find('\t')+1:-1]
        value2 = values[1][values[1].find('\t')+1:-1]
        trie[int(i.split(' ')[1])] = [float(value1), float(value2)]
        data_set = ''
        continue
    data_set = data_set + i 

print(dictionary)
print()
print(bst)
print()
print(trie)