# Given a preorder and inorder traversal of a binary tree, reconstruct that
# tree.

# A tree is given as a 3-tuple of (value, left, right). left and right are None
# when there are no corresponding children.

def traverse_preorder(tree):
    def helper(node, result):
        if node is None: return
        result.append(node[0])
        helper(node[1], result)
        helper(node[2], result)
    result = []
    helper(tree, result)
    return result

def traverse_inorder(tree):
    def helper(node, result):
        if node is None: return
        helper(node[1], result)
        result.append(node[0])
        helper(node[2], result)
    result = []
    helper(tree, result)
    return result

#           F
#        /     \
#     B           G
#   /   \           \
#  A     D           I
#       / \         /
#      C   E       H

# https://en.wikipedia.org/wiki/Tree_traversal#/media/File:Sorted_binary_tree_preorder.svg

C = ('C', None, None)
E = ('E', None, None)
H = ('H', None, None)
A = ('A', None, None)
D = ('D', C, E)
I = ('I', H, None)
B = ('B', A, D)
G = ('G', None, I)
F = ('F', B, G)
tree = F

def reconstruct(preorder, inorder):
    if len(preorder) == 0: return None
    index = inorder.index(preorder[0])
    return (
        preorder[0],
        reconstruct(preorder[1:index+1], inorder[:index]),
        reconstruct(preorder[index+1:], inorder[index+1:])
    )

print reconstruct(traverse_preorder(tree), traverse_inorder(tree)) == F