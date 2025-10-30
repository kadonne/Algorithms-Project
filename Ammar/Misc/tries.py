class TrieNode: #definition for the TrieNode itself
    def __init__(self):
        self.children = {} #keeps track of this nodes children
        self.is_end = False #indicates if value is in Trie
        self.values = list() #actual val of each node, this is equal to the char in our case

class Trie: #definition of Trie structure, consisting of TrieNodes. Starting with rootNode
    def __init__(self):
        self.root = TrieNode()

    def insert(self,value):
        node = self.root
        for char in value:
            if char not in node.children: #if node is not in the child nodes
                node.children[char] = TrieNode() #make new node
            node = node.children[char]#else, it is in our trie already
            node.is_end = True
            node.values.append(value)
    
    def search(self,value):
        node = self.root
        for char in value:
            if char not in node.children:
                return None #not found
            node = node.children[char] #move down tree when we find the char
        return node.values #returns bottom child, which will have vals of our whole hash!

    def _print_values(self, node, prefix):
        if node.is_end:
            print(prefix)
        for char, child_node in node.children.items():
            self._print_values(child_node, prefix + char)

    def print_values(self):
        self._print_values(self.root,'')
