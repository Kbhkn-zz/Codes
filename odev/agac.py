from collections import namedtuple
 
Node = namedtuple('Node', 'data, left, right')

tree = [1, [2, [4, 7], [5]], [3, [6, [8], [9]]]]
 
a = []
 
def preorder(node):
  if node is not None:
    a.append(node.data)
    preorder(node.left)
    preorder(node.right)

preorder(tree)
print("En küçük eleman: ", min(a))