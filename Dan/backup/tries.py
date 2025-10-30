class TrieNode: #definition of TrieNode
    def __init__(self):
        self.children = {} #dictionary containing this nodes children
        self.is_end = False #if true, this hash is "in" our tree
        self.values = [] #the actual value contained in the node, in our case the Char
        self.password = ''

class Trie:
    def __init__(self):
        self.root = TrieNode() #Trie Tree definition, starting with the root
    
    def insert(self, value,password):
        node = self.root 
        node.password = password
        for char in value: #for each character in our encoded Hash
            if char not in node.children: # if the char is not already a child of current 
                node.children[char] = TrieNode() #new node! 
            node = node.children[char] # else, its in the Trie, we call that our new root, continue the loop
            node.password = password
        node.is_end = True #once were here, its the end of the Hash. Mark it true
        node.values.append(value) #value stored here will be path to get here

    def search(self, value):
        node = self.root
        for char in value: #for every char on input value
            if char not in node.children:
                return None #if were here, the input value can't be in trie, return None
            node = node.children[char] # if found, move down the tree 
        return node.values[0], node.password 
    
    def print_search(self, value):
        #do a search for the hash
        result = self.search(value)

        if result: #if we have a result
            result = str(result)[1:-1] #remove brackets
            print(result) 

    
