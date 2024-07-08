from LinkedBinaryTree import LinkedBinaryTree as Tree

tree = Tree()
#create a binary tree from values 1, 2, 3, 4, 5, 6
tree._add_root(1)
tree._add_left(tree.root(), 2)
tree._add_right(tree.root(), 3)
tree._add_left(tree.left(tree.root()), 4)
tree._add_right(tree.right(tree.root()), 5)

#use the preorder traversal to print the tree
print("Preorder traversal: ", end = " ")
for i in tree.positions():
    print(i.element(), end = " ")
print()

#use the post order traversal to print the tree
print("Postorder traversal: ", end = " ")
for i in tree.postorder():
    print(i.element(), end = " ")
print()