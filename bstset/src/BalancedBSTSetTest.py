#!/usr/bin/env python
# coding: UTF-8
# vim: tabstop=4:softtabstop=4:shiftwidth=4
#
## @package BalancedBSTSet
#
#  α-Balanced Binary Search Tree based Set
#
#  @author Claudio Roberto França Pereira
#  @date 14/05/2019
#
import unittest
import random
from BalancedBSTSet import *

##
 # @author Claudio Roberto França Pereira
 # @since 06/03/2019
 # @description Test class with tests for BalancedBSTSet
 #
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

    def test_setIntersection(self):
        a = BalancedBSTSet()
        a.update([x for x in range(1, 5)])
        b = BalancedBSTSet()
        b.update([x for x in range(3, 10)])
        c = BalancedBSTSet()
        c.update([x for x in range(3, 5)])
        self.assertEqual(set_intersection(a, b).toArray(), c.toArray())

        a = BalancedBSTSet()
        dA = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        a.update(dA)
        b = BalancedBSTSet()
        dB = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        b.update(dB)
        c = BalancedBSTSet()
        for x in a:
            if x in b:
                c.append(x)
        self.assertEqual(c.toArray(), set_intersection(a, b).toArray())

    def test_setUnion(self):
        a = BalancedBSTSet()
        a.update([x for x in range(1, 5)])
        b = BalancedBSTSet()
        b.update([x for x in range(3, 10)])
        c = BalancedBSTSet()
        c.update([x for x in range(1, 10)])
        self.assertEqual(set_union(a, b).toArray(), c.toArray())

        a = BalancedBSTSet()
        dA = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        a.update(dA)
        b = BalancedBSTSet()
        dB = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        b.update(dB)
        c = BalancedBSTSet()
        c.update(dA)
        c.update(dB)
        self.assertEqual(c.toArray(), set_union(a, b).toArray())

    def test_setDifference(self):
        a = BalancedBSTSet()
        a.update([x for x in range(15, 27)])
        b = BalancedBSTSet()
        b.update([x for x in range(21, 35)])
        c = BalancedBSTSet()
        c.update([x for x in range(15, 21)])
        self.assertEqual(set_difference(a, b).toArray(), c.toArray())

        a = BalancedBSTSet()
        dA = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        a.update(dA)
        b = BalancedBSTSet()
        dB = [random.randint(1, 500) for _ in range(random.randrange(100, 200))]
        b.update(dB)
        c = BalancedBSTSet()
        c.update(dA)
        for x in b:
            c.remove(x)
        self.assertEqual(c.toArray(), set_difference(a, b).toArray())

if __name__ == "__main__":
    unittest.main()

