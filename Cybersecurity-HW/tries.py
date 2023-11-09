class TrieNode: #definition of TrieNode
    def __init__(self):
        self.children = {} #dictionary containing this nodes children
        self.is_end = False #if true, this hash is "in" our tree
        self.values = [] #list to store values associated with this node

class Trie:
    def __init__(self):
        self.root = TrieNode() #Trie Tree definition, starting with the root
    
    def insert(self, value):
        node = self.root 
        for char in value: #for each character in our encoded Hash
            if char not in node.children: # if the char is not already a child of current 
                node.children[char] = TrieNode() #new node! 
            node = node.children[char] # else, its in the Trie, we call that our new root, continue the loop
        node.is_end = True #once were here, its the end of the Hash. Mark it true
        node.values.append(value) #add the character to this nodes values list

    def search(self, value):
        #starting at root of the Trie
        node = self.root 
        for char in value:
            if char not in node.children:
                #If the current Char is not in the children of current node
                #the hash is not in the Trie
                return None
            node = node.children[char]
        #Loop is finished, node now points to last character in the search hash
        #return the values list associated with this node.
        result = str(node.values)[1:-1]
        return print(result)

    