import matplotlib.pyplot as plt

#data_file = open('time_sheets.txt','r')
data_file = open("10k_time_sheets.txt",'r')
max_data_size = str(10000)

data = data_file.readlines()
dictionary_index = 0
bst_index = 0
for i in data:
    #if "Dictionary: 10000" in i:
    if "Dictionary: "+max_data_size in i:
        dictionary_index = data.index(i)+1
for i in data:
    #if "Self-Balancing-Tree: 10000" in i:
    if "Self-Balancing-Tree: "+max_data_size in i:
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

my_keys = list(dictionary.keys())
my_keys.sort()
sorted_dict = {i: dictionary[i] for i in my_keys}
dictionary = sorted_dict

my_keys = list(bst.keys())
my_keys.sort()
sorted_dict = {i: bst[i] for i in my_keys}
bst = sorted_dict

my_keys = list(trie.keys())
my_keys.sort()
sorted_dict = {i: trie[i] for i in my_keys}
trie = sorted_dict

print(dictionary)
print()
print(bst)
print()
print(trie)

x_data = []
y_data = [[],[],[]]
for i in dictionary:
    x_data.append(i)
    y_data[0].append(dictionary[i][0])
    y_data[1].append(dictionary[i][1])
    y_data[2].append(dictionary[i][2])
plt.plot(x_data,y_data[0], label='Insert Time')
plt.plot(x_data,y_data[1], label='Search Time')
plt.plot(x_data,y_data[2], label='Sort Time')
plt.title("Hash Table Running Time")
plt.xlabel("Data Size (n)")
plt.ylabel("Running Time O(n)")
plt.legend()
plt.show()


x_data = []
y_data = [[],[]]
for i in bst:
    x_data.append(i)
    y_data[0].append(bst[i][0])
    y_data[1].append(bst[i][1])
plt.plot(x_data,y_data[0], label='Insert Time')
plt.plot(x_data,y_data[1], label='Search Time')
plt.title("Self-Balancing BST Running Time")
plt.xlabel("Data Size (n)")
plt.ylabel("Running Time O(n)")
plt.legend()
plt.show()


x_data = []
y_data = [[],[]]
for i in trie:
    x_data.append(i)
    y_data[0].append(trie[i][0])
    y_data[1].append(trie[i][1])
plt.plot(x_data,y_data[0], label='Insert Time')
plt.plot(x_data,y_data[1], label='Search Time')
plt.title("Trie Tree Running Time")
plt.xlabel("Data Size (n)")
plt.ylabel("Running Time O(n)")
plt.legend()
plt.show()