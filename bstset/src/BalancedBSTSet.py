#!/usr/bin/env python
# coding: UTF-8
# vim: tabstop=4:softtabstop=4:shiftwidth=4
#
## @package BalancedBSTSet
#
#  α-Balanced Binary Search Tree based Set
#
#  @author Claudio Roberto França Pereira
#  @date 06/03/2019
#

from BSTSet import BSTSet, generateRandomArray

##
 # @author Claudio Roberto França Pereira
 # @since 06/03/2019
 #
class BalancedBSTSet(BSTSet):
    ##
     # Node type for BalancedBSTSet
     #
    class Node(BSTSet.Node):
        ##
         # Constructor for BalancedBSTSet.Node.
         #
         # @param data object to be stored.
         # @param parent parent node, None for root node.
         #
        def __init__(self, data, parent):
            BSTSet.Node.__init__(self, data, parent)
            ## Number of nodes in the subtree rooted at this node.
            self.subtreeSize = 1

        ## Return a string representation of this node.
        def __repr__(self):
            return "%s (%d)" % (self.data, self.subtreeSize)

    ##
     # The iterator is basically the same as BSTSet's, we just need to make
     # sure the node subtree size is updated on the remove call.
     #
    class BalancedBSTIterator(BSTSet.BSTIterator):
        ##
         # The API is the same as BSTSet.BSTIterator's. Remove the node returned
         # by the last call to next().
         #
         # @raise IndexError if next() hasn't been called before, or if the
         #                   current node has already been removed.
         #
        def remove(self):
            ##
             # Updates the successor node's parents if we remove the current
             # node by substituting its value with its successor's value and
             # deleting the successor.  In this iterator, current is referenced
             # by __pending and its successor is referenced by __current.
            current = self.__BSTIterator__pending

            nodeToUpdateParents = current
            if current.left != None and current.right != None:
                successor = self.__BSTIterator__current
                nodeToUpdateParents = successor

            tree = self.__BSTIterator__tree
            nodeToRebalance = tree.__updateParents(nodeToUpdateParents, -1)
            BSTSet.BSTIterator.remove(self)
            if nodeToRebalance != None:
                tree.rebalance(nodeToRebalance)
            
    ##
     # Constructor for an α-Balanced Binary Search Tree Set
     #
     # @param alphaNumerator numerator for the fraction that represents α
     # @param alphaDenominator denominator for the fraction that represents α
     #
    def __init__(self, isSelfBalancing = False, top = 2, bottom = 3):
        BSTSet.__init__(self)
        if not isinstance(isSelfBalancing, bool):
            raise TypeError("Argument isSelfBalancing must be a boolean.")
        if not isinstance(top, int):
            raise TypeError("Argument top must be an integer.")
        if not isinstance(bottom, int):
            raise TypeError("Argument bottom must be an integer.")
        if not (1/2 <= top/bottom < 1):
            raise ValueError("Inappropriate top/bottom value. It should be " + \
                    "a value in the [0.5, 1) range.")
        self.__alphaNumerator = top
        self.__alphaDenominator = bottom
        self.__autoBalance = isSelfBalancing

    def __str__(self):
        return "BalancedBSTSet(isSelfBalancing=%s, top=%d, bottom=%d)" % \
            (self.__autoBalance, self.__alphaNumerator, self.__alphaDenominator)

    ##
     # Helper function to update the subtree size of all parents nodes
     #
     # @param node Node whose parents will be updated
     # @param change Integer value to be summed to each parent node subtree size
     #               Use 1 when adding a node or -1 when removing
     #
    def __updateParents(self, node, change):
        parentNode = node.parent
        parentToRebalance = None
        while parentNode != None:
            parentNode.subtreeSize += change
            if self.__autoBalance and not self.__isBalanced(parentNode):
                parentToRebalance = parentNode
            parentNode = parentNode.parent

        return parentToRebalance

    def __isBalanced(self, node):
        leftSize = 0
        if (node.left != None):
            leftSize = node.left.subtreeSize
        rightSize = 0
        if (node.right != None):
            rightSize = node.right.subtreeSize
        leftIsBalanced = (leftSize * self.__alphaDenominator <= \
                                node.subtreeSize * self.__alphaNumerator)
        rightIsBalanced = (rightSize * self.__alphaDenominator <= \
                                node.subtreeSize * self.__alphaNumerator)
        return (leftIsBalanced and rightIsBalanced)

    ## Add data to the tree as a new node
    def add(self, data):
        added = BSTSet.add(self, data)
        ## Update subtree sizes only if the key was really added
        if (added):
            node = self.findEntry(data)
            assert node != None, "Just added entry couldn't be found."
            rebalanceNode = self.__updateParents(node, 1)
            if rebalanceNode != None:
                self.rebalance(rebalanceNode)
        return added

    ## Remove node with value data from the tree
    def remove(self, data):
        n = self.findEntry(data)
        if n is None:
            return False
        
        nodeToUpdateParents = n
        if n.left != None and n.right != None:
            nodeToUpdateParents = self.successor(n)

        ## Update parents' subtree size before removing the node
        rebalanceNode = self.__updateParents(nodeToUpdateParents, -1)
        self.unlinkNode(n)
        if rebalanceNode != None:
            self.rebalance(rebalanceNode)
        return True

    def rebalance(self, node):
        nodeArray = self._BSTSet__inOrder(node, None)
        parent = node.parent

        insertLeft = False
        if parent != None and node.parent.left == node:
            insertLeft = True

        newRoot = self.__recreateTree(nodeArray, 0, len(nodeArray)-1, parent)
        if parent != None:
            if insertLeft:
                parent.left = newRoot
            else:
                parent.right = newRoot
        else:
            self._BSTSet__root = newRoot

    def __recreateTree(self, nodeArray, start, end, parent):
        middle = (start + end) // 2
        node = None

        if start <= middle <= end:
            node = nodeArray[middle]
            node.parent = parent
            node.subtreeSize = (end - start + 1)
            node.left = self.__recreateTree(nodeArray, start, middle - 1, node)
            node.right = self.__recreateTree(nodeArray, middle + 1, end, node)

        return node

import unittest
import random

class TestBalancedBSTSet(unittest.TestCase):
    def test_creation(self):
        self.assertIsNotNone(BalancedBSTSet())
        self.assertIsNotNone(BalancedBSTSet(True))
        self.assertIsNotNone(BalancedBSTSet(False))
        self.assertIsNotNone(BalancedBSTSet(True, 5, 7))
        self.assertIsNotNone(BalancedBSTSet(True, 1, 2))
        with self.assertRaises(TypeError):
            BalancedBSTSet("abc")
        with self.assertRaises(TypeError):
            BalancedBSTSet(10)
        with self.assertRaises(TypeError):
            BalancedBSTSet(top = "foo")
        with self.assertRaises(TypeError):
            BalancedBSTSet(bottom = "bar")
        with self.assertRaises(TypeError):
            BalancedBSTSet(True, 1, 2.3)
        with self.assertRaises(TypeError):
            BalancedBSTSet(False, 5.0, 7)
        with self.assertRaises(TypeError):
            BalancedBSTSet(False, "2", "3")
        with self.assertRaises(ZeroDivisionError):
            BalancedBSTSet(bottom = 0)
        with self.assertRaises(ValueError):
            BalancedBSTSet(False, 2, 7)
        with self.assertRaises(ValueError):
            BalancedBSTSet(False, 15, 3)

    def test_root(self):
        tree = BalancedBSTSet()
        self.assertTrue(tree.isEmpty())
        self.assertIsNone(tree.root())
        self.assertEqual(len(tree), 0)

        tree.add(5)
        self.assertFalse(tree.isEmpty())
        self.assertIsNotNone(tree.root())
        self.assertEqual(len(tree), 1)

        previousRoot = tree.root()
        tree.add(12)
        self.assertFalse(tree.isEmpty())
        self.assertIsNotNone(tree.root())
        self.assertEqual(tree.root(), previousRoot)
        self.assertEqual(len(tree), 2)

    def test_add(self):
        tree = BalancedBSTSet()
        added = []
        elems = [random.randint(1, 500) for _ in range(random.randint(10, 30))]
        for e in elems:
            if tree.add(e):
                added.append(e)
        self.assertEqual(len(tree), len(added))
        for e in added:
            self.assertIsNotNone(tree.findEntry(e))
        added.sort()
        inOrder = [x.data for x in tree._BSTSet__inOrder(tree.root(), None)]
        self.assertEqual(inOrder, added)
        elems = list(set(elems))
        elems.sort()
        self.assertEqual(added, elems)

    def test_remove(self):
        tree = BalancedBSTSet(False)
        elements = [50, 34, 72, 12, 6]

        for x in elements:
            tree.add(x)
        self.assertEqual(len(tree), len(elements))
        originalHeight = tree.height()
        tree.remove(6)
        self.assertEqual(tree.height(), originalHeight - 1)
        self.assertEqual(len(tree), len(elements) - 1)
        tree.remove(34)
        self.assertEqual(tree.height(), originalHeight - 2)
        self.assertEqual(len(tree), len(elements) - 2)

        for x in elements:
            tree.remove(x)
        self.assertEqual(len(tree), 0)
        for x in elements:
            tree.add(x)
        elements.sort()
        for _ in range(len(elements) - 1):
            x = elements[random.randrange(len(elements))]
            elements.remove(x)
            tree.remove(x)
            self.assertEqual(len(tree), len(elements))
            inOrder = [x.data for x in tree._BSTSet__inOrder(tree.root(), None)]
            self.assertEqual(inOrder, elements)

    def test_height(self):
        tree = BalancedBSTSet(False)
        self.assertEqual(tree.height(), -1)
        tree.add(5)
        self.assertEqual(tree.height(), 0)
        tree.add(3)
        self.assertEqual(tree.height(), 1)
        tree.add(7)
        self.assertEqual(tree.height(), 1)
        tree.add(2)
        self.assertEqual(tree.height(), 2)
        tree.add(1)
        self.assertEqual(tree.height(), 3)

    def test_rebalance(self):
        tree = BalancedBSTSet(False)
        tree.update([x for x in range(1, 10)])
        self.assertEqual(tree.root().data, 1)
        self.assertEqual(tree.height(), 8)
        tree.rebalance(tree.root())
        self.assertEqual(tree.root().data, 5)
        self.assertEqual(tree.height(), 3)

        tree = BalancedBSTSet(False)
        tree.update([x for x in range(1, 10)])
        node4 = tree.root().right.right.right
        node5 = node4.right
        self.assertEqual(node5.data, 5)
        self.assertEqual(tree.getHeight(node5), 4)
        tree.rebalance(node5)
        self.assertEqual(node5.data, 5)
        self.assertEqual(node4.right.data, 7)
        self.assertEqual(tree.getHeight(node4.right), 2)

        tree = BalancedBSTSet(True, 1, 2)
        tree.add(1)
        self.assertEqual(tree.height(), 0)
        self.assertEqual(tree.root().data, 1)
        tree.add(2)
        self.assertEqual(tree.root().data, 1)
        self.assertEqual(tree.height(), 1)
        tree.add(3)
        self.assertEqual(tree.root().data, 2)
        self.assertEqual(tree.height(), 1)
        tree.add(4)

    def test_iterator(self):
        tree = BalancedBSTSet()
        elems = [random.randint(1, 500) for _ in range(random.randint(50, 100))]
        for x in elems:
            tree.add(x)
        elems = list(set(elems))
        elems.sort()
        self.assertEqual(tree.toArray(), elems)

        iterator = tree.iterator()
        while next(iterator, None):
            iterator.remove()
        self.assertEqual(len(tree), 0)

        for x in elems:
            tree.add(x)
        iterator = tree.iterator()
        for x in iterator:
            if random.choice((True, False)):
                elems.remove(x)
                iterator.remove()
            self.assertEqual(len(tree), len(elems))

if __name__ == "__main__":
    unittest.main()
