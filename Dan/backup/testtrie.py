from tries import Trie
string = '49fb11420c99312b99914d094e522b75d3749c977c3ee08aad1386630687a682'
string2 ='516905fac3262990fffcb90f22a33a1ea13fa313f924cd21101b3ff0302ae9cc'
trie = Trie()
trie.insert(string,'irresponsiveness(7')
trie.insert(string2,'ischiocaudal3#')
print(trie.search(string))
print(trie.search(string2))
