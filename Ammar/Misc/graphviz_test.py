from graphviz import Digraph
from tries import Trie
ex = '1aa75091df4977ac9678dea6f97f4b4c68cdee861fb86bcc69902d992f82376c'
ey = '1aa75091df4977ac9678dba6f97f4b4c68cdee861fb86bcc69902d992f82376c'
tr = Trie()
for i in ex:
    tr.insert(i)
for i in ey:
    tr.insert(i)
print(tr.print_values())
#dot = Digraph(comment='Trie',format='jpg')
#root = (ex[0])
#dot.node(root)
#dot.render('output/trie.gv',view=True)