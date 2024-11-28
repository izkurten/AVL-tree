import unittest
import math

from random import random
from datetime import date
from avl_tree import AVLTree
from avl_node import AVLNode

tree = None
testList = None
testListBackUp = None


# noinspection PyUnresolvedReferences
class TestAssignment02(unittest.TestCase):

    def setUp(self):
        pass

    def reset(self):
        global tree
        tree = AVLTree()

    def insertNode(self, key, value):
        # handle a none tree object
        global tree
        return tree.insertNode(key, value)

    def insertNode(self, key):
        # handle a none tree object
        global tree
        return tree.insertNode(key, float(key))

    def test_size_provided(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.assertEqual(1, tree.getSize(),
                         ".getSize() is wrong after inserting a node with key 5 into an AVL tree .. first node "
                         + "inserted is 5.")
        self.insertNode(18)
        self.assertEqual(2, tree.getSize(),
                         ".getSize() is wrong after inserting the nodes with key sequence "
                         + "5, 18 into an AVL tree")
        self.insertNode(2)
        self.assertEqual(3, tree.getSize(),
                         ".getSize() is wrong after inserting the nodes with key sequence "
                         + "5, 18, 2 into an AVL tree")
        self.insertNode(8)
        self.assertEqual(4, tree.getSize(),
                         ".getSize() is wrong after inserting the nodes with key sequence "
                         + "5, 18, 2, 8 into an AVL tree")
        self.insertNode(14)
        self.assertEqual(5, tree.getSize(),
                         ".getSize() is wrong after inserting the nodes with key sequence "
                         + "5, 18, 2, 8, 14 into an AVL tree")

    def test_size_with_insertNode(self):
        global tree
        self.reset()
        self.assertEqual(0, tree.getSize())
        self.insertNode(5)
        self.assertEqual(1, tree.getSize(),
                         ".getSize() is wrong after inserting a node with key 5 into an AVL tree .. first node "
                         + "inserted is 5")
        self.insertNode(18)
        self.assertEqual(2, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18 into an AVL tree")
        self.insertNode(2)
        self.assertEqual(3, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2 into an AVL tree")
        self.insertNode(8)
        self.assertEqual(4, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8 into an AVL tree")
        self.insertNode(14)
        self.assertEqual(5, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14 into an AVL tree")
        self.insertNode(16)
        self.assertEqual(6, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16 into an AVL tree")
        self.insertNode(13)
        self.assertEqual(7, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13 into an AVL tree")
        self.insertNode(3)
        self.assertEqual(8, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3 into an AVL tree")
        self.insertNode(12)
        self.assertEqual(9, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12 into an AVL tree")
        self.insertNode(21)
        self.assertEqual(10, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21 into an AVL tree")
        self.insertNode(1)
        self.assertEqual(11, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1 into an AVL tree")
        self.insertNode(0)
        self.assertEqual(12, tree.getSize(), ".getSize() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0 into an AVL tree")

    def test_height_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(-1, tree.getTreeHeight(), ".getTreeHeight() is wrong for empty tree:")

    def test_height(self):
        global tree
        self.reset()

        self.assertEqual(-1, tree.getTreeHeight(), ".getTreeHeight() is wrong for empty tree: ")
        self.insertNode(5)
        self.assertEqual(0, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after inserting the node with key 5 into an empty AVL tree .. "
                         + "first node inserted is 5")
        self.insertNode(18)
        self.assertEqual(1, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18 into an AVL tree")
        self.insertNode(2)
        self.assertEqual(1, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2 into an AVL tree")
        self.insertNode(8)
        self.assertEqual(2, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8 into an AVL tree")
        self.insertNode(14)
        self.assertEqual(2, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14 into an AVL tree")
        self.insertNode(16)
        self.assertEqual(2, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16 into an AVL tree")
        self.insertNode(13)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13 into an AVL tree")
        self.insertNode(3)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3 into an AVL tree")
        self.insertNode(12)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12 into an AVL tree")
        self.insertNode(21)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21 into an AVL tree")
        self.insertNode(1)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1 into an AVL tree")
        self.insertNode(0)
        self.assertEqual(3, tree.getTreeHeight(), ".getTreeHeight() is wrong after inserting the nodes with keys "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0 into an AVL tree")

    def test_find(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)
        self.assertEqual(5, tree.find_by_key(5),
                         ".find_by_key(5) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(18, tree.find_by_key(18),
                         ".find_by_key(18) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(2, tree.find_by_key(2),
                         ".find_by_key(2) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(8, tree.find_by_key(8),
                         ".find_by_key(8) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(14, tree.find_by_key(14),
                         ".find_by_key(14) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(16, tree.find_by_key(16),
                         ".find_by_key(16) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(13, tree.find_by_key(13),
                         ".find_by_key(13) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(3, tree.find_by_key(3),
                         ".find_by_key(3) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(12, tree.find_by_key(12),
                         ".find_by_key(12) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(21, tree.find_by_key(21),
                         ".find_by_key(21) didn't return correct element of the following AVL tree with \n\tthe "
                         + "following inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(1, tree.find_by_key(1),
                         ".find_by_key(1) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")
        self.assertEqual(0, tree.find_by_key(0),
                         ".find_by_key(0) didn't return correct element of the following AVL tree with \n\tthe following "
                         + "inserted nodes: "
                         + "5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0")

    def test_find_not_existing(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)
        self.assertEqual(None, tree.find_by_key(4),
                         ".find_by_key() didn't return None when searching for a not existing key.")
        self.assertEqual(None, tree.find_by_key(99),
                         ".find_by_key() didn't return None when searching for a not existing key.")
        self.assertEqual(None, tree.find_by_key(100),
                         ".find_by_key() didn't return None when searching for a not existing key.")

    def test_find_not_existing_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(None, tree.find_by_key(4),
                         ".find_by_key() didn't return None when searching for a not existing key in an empty tree.")
        self.assertEqual(None, tree.find_by_key(99),
                         ".find_by_key() didn't return None when searching for a not existing key in an empty tree.")
        self.assertEqual(None, tree.find_by_key(100),
                         ".find_by_key() didn't return None when searching for a not existing key in an empty tree.")

    def test_remove(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)
        self.assertFalse(tree.removeNode(4), ".removeNode(4) didn't return FALSE for the following AVL tree")
        self.assertFalse(tree.removeNode(99), ".removeNode(99) didn't return FALSE for the following AVL tree")
        self.assertFalse(tree.removeNode(100), ".removeNode(100) didn't return FALSE for the following AVL tree")

        self.assertTrue(tree.removeNode(14), ".removeNode(14) didn't return TRUE for the following AVL tree")
        self.assertTrue(tree.removeNode(3), ".removeNode(3) didn't return TRUE for the following AVL tree")
        self.assertTrue(tree.removeNode(21), ".removeNode(21) didn't return TRUE for the following AVL tree")
        self.assertTrue(tree.removeNode(18), ".removeNode(18) didn't return TRUE for the following AVL tree")
        self.assertTrue(tree.removeNode(16), ".removeNode(16) didn't return TRUE for the following AVL tree")
        self.assertFalse(tree.removeNode(14), ".removeNode(14) didn't return FALSE for the following AVL tree")

    def test_size_with_remove(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)

        sb = self.print_tree()
        tree.removeNode(4)
        self.assertEqual(12, tree.getSize(),
                         ".getSize() is wrong after removing not existing node with key 4 from the following "
                         + "tree:" + sb)
        tree.removeNode(99)
        self.assertEqual(12, tree.getSize(),
                         ".getSize() is wrong after removing not existing node with key 99 from the following "
                         + "tree:" + sb)
        tree.removeNode(100)
        self.assertEqual(12, tree.getSize(),
                         ".getSize() is wrong after removing not existing node with key 100 from the following "
                         + "tree:" + sb)
        tree.removeNode(14)
        self.assertEqual(11, tree.getSize(),
                         ".getSize() is wrong after removing node with key 14 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(3)
        self.assertEqual(10, tree.getSize(),
                         ".getSize() is wrong after removing node with key 3 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(21)
        self.assertEqual(9, tree.getSize(),
                         ".getSize() is wrong after removing node with key 21 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(18)
        self.assertEqual(8, tree.getSize(),
                         ".getSize() is wrong after removing node with key 18 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(16)
        self.assertEqual(7, tree.getSize(),
                         ".getSize() is wrong after removing node with key 16 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(14)
        self.assertEqual(7, tree.getSize(),
                         ".getSize() is wrong after removing not existing node with key 14 from the following "
                         + "tree:" + sb)

    def test_height_with_remove(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)

        sb = self.print_tree()
        tree.removeNode(4)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing not existing node with key 4 from the following "
                         + "tree:" + sb)
        tree.removeNode(99)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing not existing node with key 99 from the following "
                         + "tree:" + sb)
        tree.removeNode(100)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing not existing node with key 100 from the "
                         + "following tree:" + sb)
        tree.removeNode(14)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing node with key 14 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(3)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing node with key 3 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(21)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing node with key 21 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(18)
        self.assertEqual(3, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing node with key 18 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(16)
        self.assertEqual(2, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing node with key 16 from the following tree:" + sb)
        sb = self.print_tree()
        tree.removeNode(14)
        self.assertEqual(2, tree.getTreeHeight(),
                         ".getTreeHeight() is wrong after removing not existing node with key 14 from the following "
                         + "tree:" + sb)

    def test_remove_not_existing_key(self):
        global tree
        self.reset()
        self.assertFalse(tree.removeNode(10212), ".removeNode() of a not existing key should return FALSE. ")

    def test_remove_none(self):
        global tree
        self.reset()
        expected_ex = None
        try:
            tree.removeNode(None)
        except Exception as e:
            expected_ex = e

        self.assertTrue(not (isinstance(ValueError, type(expected_ex))),
                        ".removeNode() of a None key should throw an ValueError.")

    def test_insert_duplicates(self):
        global tree
        self.reset()
        self.assertTrue(self.insertNode(5),
                        ".insert_node() didn't return TRUE when a node with a key is inserted for the first time.")
        self.assertFalse(self.insertNode(5),
                         ".insert_node() didn't return FALSE when a node with an already existing key is inserted.")

    def test_size_empty_tree(self):
        global tree
        self.reset()
        self.assertEqual(0, tree.getSize(), ".getSize() is wrong for empty tree: ")

    def test_structure1_rotation_hardcoded(self):
        global tree

        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        root = tree.getTreeRoot()

        self.assertEqual(root.key, 5)
        self.assertEqual(root.height, 2)
        # left branch
        self.assertEqual(root.left.key, 2)
        self.assertEqual(root.left.height, 0)
        # right branch
        self.assertEqual(root.right.key, 14)
        self.assertEqual(root.right.height, 1)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.left.key, 8)
        self.assertEqual(root.right.left.height, 0)
        self.assertEqual(root.right.left.left, None)
        self.assertEqual(root.right.left.right, None)
        self.assertEqual(root.right.right.key, 18)
        self.assertEqual(root.right.right.height, 0)
        self.assertEqual(root.right.right.left, None)
        self.assertEqual(root.right.right.right, None)


    # Function to convert
    def list_to_string(self, s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 = str1 + ele + ", "

        # return string
        return str1

    # ============================================test_multiple_values==================================================

    def test_multiple_values(self):
        global tree

        value_range = 20

        num_of_operations = 2500
        operation_sequence = []
        self.reset()
        print("----------------------------------------------------------")
        print("testMultipleValues: Checking Integrity after insert/remove")
        print("----------------------------------------------------------")
        i = 0
        while i < num_of_operations:
            check = False
            inserted = 0
            removed = 0
            sb_tree_after = self.print_tree()
            sb_tree_before = self.print_tree()
            val = int(random() * value_range)

            if tree.insertNode(val, float(val)):
                inserted = 1
                operation_sequence.append(" I: {} ".format(val))
            else:
                operation_sequence.append(" (I: {} )".format(val))

            check = self._check_avl_integrity()

            str_error = " of AVL tree broken after multiple insert/remove (number of operations processed: " + str(
                i) + " / " + str(num_of_operations) + ")\n\t"
            str_error += "--> Insert/Remove sequence (I...Insert; R...Remove; an operation in brackets () was " \
                         + "unsuccessful because of duplicate or not existing node " \
                         + "; the very last operation caused the error):\n "
            str_error += self.list_to_string(operation_sequence)
            str_error += "\nTree before insert:\n\t" + sb_tree_before + "\n\n\tTree after insert:" + sb_tree_after \
                         + "\n\t"

            self.assertTrue(check, "Integrity" + str_error)
            self.assertTrue(
                tree.getTreeHeight() <= (1.44 * (math.log(tree.getSize() + 2) / math.log(2)) - 0.328),
                "Height" + str_error)

            # print(i)
            if tree.removeNode(val):
                inserted = 1
                operation_sequence.append(" R: {} ".format(val))
            else:
                operation_sequence.append(" (R: {} )".format(val))

            sb_tree_after = self.print_tree()

            check = self._check_avl_integrity()

            str_error = " of AVL tree broken after multiple insert/remove (number of operations processed: " + str(
                i) + "/" + str(num_of_operations) + ")\n\t"
            str_error += "--> Insert/Remove sequence (I...Insert; R...Remove; an operation in brackets \"()\" was " \
                         + "unsuccessful because of duplicate or not existing node; the very last operation caused " \
                         + "the error):\n\t "
            str_error += self.list_to_string(operation_sequence)
            str_error += "\nTree before insert:\n\t" + sb_tree_before + "\n\n\tTree after insert:" + sb_tree_after \
                         + "\n\t"

            self.assertTrue(check, "Integrity" + str_error)
            self.assertTrue(
                tree.getTreeHeight() <= (1.44 * (math.log(tree.getSize() + 2) / math.log(2)) - 0.328),
                "Height" + str_error)

            i += 1

        print(" AVL integrity check successful (number of operations processed: " + str(i) + "/"
              + str(num_of_operations) + ")\n\t"
              + "--> Insert/Remove sequence (I...Insert; R...Remove; operation in brackets \"()\" was unsuccessful "
              + "because of duplicate or not existing node):\n\t "
              + self.list_to_string(operation_sequence))

    # ==============================================================================================

    def test_structure1(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14."

        # // test structure
        self.assertEqual(root.key, 5, str_error)
        # // left branch
        self.assertEqual(root.left.key, 2, str_error)
        # // right branch
        self.assertEqual(root.right.key, 14, str_error)
        self.assertEqual(root.left.left, None, str_error)
        self.assertEqual(root.left.right, None, str_error)
        self.assertEqual(root.right.left.key, 8, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right.key, 18, str_error)
        self.assertEqual(root.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right, None, str_error)

    def test_structure2(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        # // right branch
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right, None, str_error)
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure3(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure4(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 8, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure5(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 12, str_error)
        self.assertEqual(root.left.right.left.key, 8, str_error)
        self.assertEqual(root.left.right.left.left, None, str_error)
        self.assertEqual(root.left.right.left.right, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right, None, str_error)

    def test_structure6(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12, 21."

        # // test structure
        self.assertEqual(root.key, 14, str_error)
        # // left branch
        self.assertEqual(root.left.key, 5, str_error)
        self.assertEqual(root.left.left.key, 2, str_error)
        self.assertEqual(root.left.left.left, None, str_error)
        self.assertEqual(root.left.left.right.key, 3, str_error)
        self.assertEqual(root.left.left.right.left, None, str_error)
        self.assertEqual(root.left.left.right.right, None, str_error)
        self.assertEqual(root.left.right.key, 12, str_error)
        self.assertEqual(root.left.right.left.key, 8, str_error)
        self.assertEqual(root.left.right.left.left, None, str_error)
        self.assertEqual(root.left.right.left.right, None, str_error)
        self.assertEqual(root.left.right.right.key, 13, str_error)
        self.assertEqual(root.left.right.right.left, None, str_error)
        self.assertEqual(root.left.right.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 18, str_error)
        self.assertEqual(root.right.left.key, 16, str_error)
        self.assertEqual(root.right.left.left, None, str_error)
        self.assertEqual(root.right.left.right, None, str_error)
        self.assertEqual(root.right.right.key, 21, str_error)
        self.assertEqual(root.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right, None, str_error)

    def test_structure7(self):
        global tree
        self.reset()
        self.insertNode(5)
        self.insertNode(18)
        self.insertNode(2)
        self.insertNode(8)
        self.insertNode(14)
        self.insertNode(16)
        self.insertNode(13)
        self.insertNode(3)
        self.insertNode(12)
        self.insertNode(21)
        self.insertNode(1)
        self.insertNode(0)
        root = tree.getTreeRoot()

        str_error = "Rotation error after inserting the nodes with the keys 5, 18, 2, 8, 14, 16, 13, 3, 12, 21, 1, 0."

        # // test structure
        self.assertEqual(root.key, 5, str_error)
        # // left branch
        self.assertEqual(root.left.key, 2, str_error)
        self.assertEqual(root.left.left.key, 1, str_error)
        self.assertEqual(root.left.left.left.key, 0, str_error)
        self.assertEqual(root.left.left.left.left, None, str_error)
        self.assertEqual(root.left.left.left.right, None, str_error)
        self.assertEqual(root.left.left.right, None, str_error)
        self.assertEqual(root.left.right.key, 3, str_error)
        self.assertEqual(root.left.right.left, None, str_error)
        self.assertEqual(root.left.right.right, None, str_error)
        # // right branch
        self.assertEqual(root.right.key, 14, str_error)
        self.assertEqual(root.right.left.key, 12, str_error)
        self.assertEqual(root.right.left.left.key, 8, str_error)
        self.assertEqual(root.right.left.left.left, None, str_error)
        self.assertEqual(root.right.left.left.right, None, str_error)

        self.assertEqual(root.right.left.right.key, 13, str_error)
        self.assertEqual(root.right.left.right.left, None, str_error)
        self.assertEqual(root.right.left.right.right, None, str_error)

        self.assertEqual(root.right.right.key, 18, str_error)
        self.assertEqual(root.right.right.left.key, 16, str_error)
        self.assertEqual(root.right.right.left.left, None, str_error)
        self.assertEqual(root.right.right.left.right, None, str_error)
        self.assertEqual(root.right.right.right.key, 21, str_error)
        self.assertEqual(root.right.right.right.left, None, str_error)
        self.assertEqual(root.right.right.right.right, None, str_error)

    def _check_avl_integrity(self):
        global tree
        return self.check_avl_integrity(tree.getTreeRoot())

    def check_avl_integrity(self, n):
        global tree

        is_avl = True
        if n is None:
            return True
        if not self.is_avltree(n):
            is_avl = False

        if not is_avl:
            lh = -1 if n.left is None else n.left.height
            rh = -1 if n.right is None else n.right.height
            print(str(n.height) + ";" + str(lh) + ";" + str(rh))

        if not self.check_avl_integrity(n.left):
            is_avl = False
        if not self.check_avl_integrity(n.right):
            is_avl = False

        return is_avl

    def is_avltree(self, n):
        diff = (-1 if n.left is None else n.left.height)
        - (-1 if n.right is None else n.right.height)
        return (-1 <= diff) and (diff <= 1)

    def print_tree(self):
        global tree

        lst_tree = ["\n\n"]
        self.print_tree_r(tree.getTreeRoot(), 0, "", lst_tree)
        str_tree = " "

        return str_tree.join(lst_tree)

    def print_tree_r(self, node: AVLNode, level=0, direction="", str_tree=[]):
        if node is not None:
            self.print_tree_r(node.right, level + 1, "/", str_tree)

            if node.parent is None:
                # print(' ' * 4 * level + "ROOT->", int(node.key))
                str_tree.append(' ' * (4 * level) + "ROOT -> " + str(node.key)+"\n")
            else:
                # print(' ' * ((4 * level)+5) + direction, int(node.key))
                str_tree.append(' ' * ((4 * level)+6) + direction + " " + str(node.key)+"\n")

            self.print_tree_r(node.left, level + 1, "\\", str_tree)


if __name__ == '__main__':
    unittest.main()
