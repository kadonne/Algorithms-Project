import matplotlib.pyplot as plt
import numpy as np

#data_file = open('time_sheets.txt','r')
data_file = open("lime_in_3D.txt",'r')
max_data_size = str(4000)

trie = {}
data = data_file.readlines()
data_set = ''
for i in data:
    if "Trie-Tree: " in i:
        values = data_set.split('\n')
        value1 = values[0][values[0].find('\t')+1:].split(' ')
        value2 = values[1][values[1].find('\t')+1:].split(' ')
        value3 = values[2][values[2].find('\t')+1:].split(' ')
        value4 = values[3][values[3].find('\t')+1:].split(' ')
        #value5 = values[4][values[4].find('\t')+1:].split(' ')
        #value6 = values[5][values[5].find('\t')+1:].split(' ')
        #value7 = values[6][values[6].find('\t')+1:].split(' ')
        #value8 = values[7][values[7].find('\t')+1:].split(' ')
        trie[int(i.split(' ')[1])] = {float(value1[0]):int(value1[1]), float(value2[0]):int(value2[1]), float(value3[0]):int(value3[1]), float(value4[0]):int(value4[1])}
                                      #float(value5[0]):int(value5[1]), float(value6[0]):int(value6[1]), float(value7[0]):int(value7[1]), float(value8[0]):int(value8[1])}
        data_set = ''
        continue
    data_set = data_set + i
print(trie)
my_keys = list(trie.keys())
my_keys.sort()
sorted_dict = {i: trie[i] for i in my_keys}
trie = sorted_dict

print(trie)

x_data = []
y_data = []
z_data = []
for i in trie:
    for j in trie[i]:
        x_data.append(i)
        y_data.append(j)
        z_data.append(trie[i][j])
ax = plt.axes(projection="3d")
ax.plot3D(x_data,y_data,z_data)
plt.title("Trie Tree Running Time")
plt.xlabel("Data Size (n)")
plt.ylabel("Running Time O(n)")
plt.clabel("Hash String length")
plt.legend()

plt.show()