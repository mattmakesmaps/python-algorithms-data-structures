#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mkenny'
__date__ = '6/6/14'
from binary_tree_as_class import BinaryTree
import operator

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def buildParseTree(fpexp):
    # split the expression into tokens.
    fplist = fpexp.split()
    pStack = Stack()
    # Create a new binary tree with an empty root node.
    eTree = BinaryTree('')
    # Add node to stack
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            # create new node; push onto stack; move down.
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            # we have an operand.
            currentTree.setRootVal(int(i))
            # use the stack to get back to the parent.
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            # we have an operator.
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            # drop back down.
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    """
    Recursively evaluate a Parse Tree.
    The base case is a leaf node, representing
    an operand (numerical value).
    """
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    # If we have a left and right child, evaluate them
    # using the operator in the root node.
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def preorderTraversal(tree):
    """
    Reads from left to right going as deep as possible
    for each node before moving right.

    1. visit root node
    2. traverse left subtree
    3. traverse right subtree
    """
    if tree:
        print(tree.getRootVal())
        preorderTraversal(tree.getLeftChild())
        preorderTraversal(tree.getRightChild())

def postorderTraversal(tree):
    """
    Reads from left to right going as deep as possible
    for each node before moving right.

    1. traverse left subtree
    2. traverse right subtree
    3. visit the root node
    """
    if tree is not None:
        postorderTraversal(tree.getLeftChild())
        postorderTraversal(tree.getRightChild())
        print(tree.getRootVal())

def postorderEval(tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    res1 = None
    res2 = None

    if tree:
        res1 = postorderEval(tree.getLeftChild())
        res2 = postorderEval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            # Base case, leaf node
            return tree.getRootVal()

def inorderTraversal(tree):
    if tree is not None:
        inorderTraversal(tree.getLeftChild())
        print(tree.getRootVal())
        inorderTraversal(tree.getRightChild())

def printExp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printExp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printExp(tree.getRightChild()) + ')'
    return sVal

if __name__ == '__main__':
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print pt
    print "evaluate(pt)"
    print evaluate(pt)
    print "Pre Order Traversal"
    preorderTraversal(pt)
    print "Post Order Traversal"
    postorderTraversal(pt)
    print "Post Order Eval"
    print postorderEval(pt)
    print "inorderTraversal"
    print inorderTraversal(pt)
    print "In Order Eval"
    print printExp(pt)
