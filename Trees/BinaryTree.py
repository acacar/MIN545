

class TreeNode:

    def __init__(self,item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    if node == None:
        return []
    # node first, left subtree second, finally right subtree
    return [node.item] + \
           preorder(node.left) +  \
           preorder(node.right)

def preorder_with_stack(node):
    stk = [node]
    out = []
    while len(stk) > 0:
        current = stk.pop()
        out += [current.item]
        if current.right is not None:
            stk.append(current.right)
        if current.left is not None:
            stk.append(current.left)
    return out
    
        
def inorder(node):
    if node == None:
        return []

    # left_subtree first, node second, finally right subtree
    return inorder(node.left) +  \
           [node.item] + \
           inorder(node.right)
            

def postorder(node):
    if node == None:
        return []

    # left_subtree first, right subtree second, finally node
    return postorder(node.left) +  \
            postorder(node.right) + \
            [node.item]

from collections import deque

def level_order(node):
    out = []
    q = deque() #left is end of the queue
    q.appendleft(node)
    while len(q) > 0:
        current = q.pop()
        if current.left is not None:
            q.appendleft(current.left)
        if current.right is not None:
            q.appendleft(current.right)
        out += [current.item]
    return out

class BinaryTree:
    def __init__(self, from_tree=None):
        self.root = from_tree
        
    def __str__(self):
        return " ".join(inorder(self.root))


def rec_bst_find(node, value, parent=None):
    if node is None:
        return parent
    if node.item == value:
        if node.left is None:
            return node
        else: ## keep going left if you have a left child
            return rec_bst_find(node.left, value, parent=node)
        
    if value > node.item:
        return rec_bst_find(node.right, value, parent=node)
    else:
        return rec_bst_find(node.left, value, parent=node)



class BST(BinaryTree):

    def __contains__(self, value):
        loc = rec_bst_find(self.root, value)
        if loc is None:
            return False # b/c the tree is empty
        elif loc.item == value:
            return True
        else:
            return False
    
    def insert(self, value):
        loc = rec_bst_find(self.root, value)
        if loc is None:
            self.root = TreeNode(value)
        else:
            if value > loc.item:
                loc.right = TreeNode(value)
            else:
                loc.left = TreeNode(value)
        
mytree = BST()

mytree.insert(6)
mytree.insert(8)
mytree.insert(1)
mytree.insert(0)
mytree.insert(2)
mytree.insert(5)
mytree.insert(1)
mytree.insert(1)














        
        
def build_very_simple_tree():
    root = TreeNode("A",
                    left=TreeNode("B",
                                  left=TreeNode("D")),
                    right=TreeNode("C",
                                   right=TreeNode("E",
                                                  left=TreeNode("F"))))
    return root

