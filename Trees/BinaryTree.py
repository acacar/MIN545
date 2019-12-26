from collections import deque
import random
import unittest

###################
# Helper functions
###################


def preorder(node):
    if node is None:
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
    if node is None:
        return []

    # left_subtree first, node second, finally right subtree
    return inorder(node.left) +  \
        [node.item] + \
        inorder(node.right)


def postorder(node):
    if node is None:
        return []

    # left_subtree first, right subtree second, finally node
    return postorder(node.left) +  \
        postorder(node.right) + \
        [node.item]


def level_order(node):
    out = []
    q = deque()  # assume appendleft adds to end of the queue
    q.appendleft(node)
    while len(q) > 0:
        current = q.pop()
        if current.left is not None:
            q.appendleft(current.left)
        if current.right is not None:
            q.appendleft(current.right)
        out += [current.item]
    return out


def rec_bst_find(node, value, parent=None):
    """
    Searches down from 'node' and returns a tuple (self, parent) for the
    descendent node that has 'value'.
    """
    if node is None:
        return (None, parent)
    if node.item == value:
        return (node, parent)
    if value > node.item:
        return rec_bst_find(node.right, value, parent=node)
    else:
        return rec_bst_find(node.left, value, parent=node)

###################
# TreeNode class
###################


class TreeNode:

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


###################
# Base BT class
###################


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return f"""
Pre-order: {" ".join([str(x) for x in preorder(self.root)])}
In-order: {" ".join([str(x) for x in inorder(self.root)])}
"""
    def __repr__(self):
        return str(self)

###################
# BST class
###################


class BST(BinaryTree):
    def __contains__(self, value):
        node, parent = rec_bst_find(self.root, value)
        return node is not None  # Either value does not exist or tree is empty

    def insert(self, value):
        node, parent = rec_bst_find(self.root, value)
        # If we already have the value, don't insert it again
        # (too messy for not much gain)
        if value in self:
            return
        # Tree is empty
        if len(self) == 0:
            self.root = TreeNode(value)
        else:
            if value > parent.item:
                parent.right = TreeNode(value)
            else:
                parent.left = TreeNode(value)
        self.size += 1


###################
# Test code
###################


class TestBSTMethods(unittest.TestCase):

    def setUp(self):
        self.testbst_1 = BST()
        self.testbst_1.insert("G")
        self.testbst_1.insert("C")
        self.testbst_1.insert("A")
        self.testbst_1.insert("B")
        self.testbst_1.insert("D")
        self.testbst_1.insert("G")

        self.testbst_2 = BST()
        self.testbst_2.insert(50)
        self.testbst_2.insert(70)
        self.testbst_2.insert(30)
        self.testbst_2.insert(40)
        self.testbst_2.insert(10)
        self.testbst_2.insert(80)
        self.testbst_2.insert(60)
        self.testbst_2.insert(20)

    def test_insert(self):
        self.assertEqual(self.testbst_1.root.item, "G")
        self.assertEqual(self.testbst_2.root.item, 50)

    def test_order(self):
        self.assertEqual(inorder(self.testbst_1.root),
                         ["A", "B", "C", "D", "G"])
        self.assertEqual(inorder(self.testbst_2.root),
                         [10, 20, 30, 40, 50, 60, 70, 80])

    def test_len(self):
        self.assertEqual(len(self.testbst_1), 5)
        self.assertEqual(len(self.testbst_2), 8)

    def test_contains(self):
        self.assertTrue("G" in self.testbst_1)
        self.assertTrue("D" in self.testbst_1)
        self.assertTrue("A" in self.testbst_1)
        self.assertFalse("X" in self.testbst_1)
        self.assertFalse("a" in self.testbst_1)
        self.assertFalse("AA" in self.testbst_1)
        self.assertTrue(30 in self.testbst_2)
        self.assertTrue(20 in self.testbst_2)
        self.assertTrue(70 in self.testbst_2)
        self.assertTrue(30.0 in self.testbst_2)
        self.assertFalse(90 in self.testbst_2)
        self.assertFalse(70.1 in self.testbst_2)

    def test_large_random(self):
        bst = BST()
        thelist = list(range(-1000, 1000))
        random.shuffle(thelist)
        for i in thelist:
            bst.insert(i)
        self.assertEqual(inorder(bst.root), sorted(thelist))

unittest.main()
