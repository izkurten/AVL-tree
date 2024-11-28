from avl_node import AVLNode


class AVLTree:
    class NodeGroup:
        def __init__(self):
            self.a = None
            self.b = None
            self.c = None
            self.t0 = None
            self.t1 = None
            self.t2 = None
            self.t3 = None

    def __init__(self):
        self.root = None
        self.size = 0
        self.to_restruct = None

    def getTreeRoot(self):
        """
        Method to get the root node of the AVLTree
        :return AVLNode -- the root node of the AVL tree
        """
        return self.root

    def getTreeHeight(self):
        """Retrieves tree height.
        :return -1 in case of empty tree, current tree height otherwise.
        """
        return self.root.height if self.root else -1

    def getSize(self):
        """Return number of key/value pairs in the tree.
        :return Number of key/value pairs.
        """
        return self.size

    def find_by_key(self, key):
        """Returns value of node with given key.
        :param key: Key to search.
        :return Corresponding value if key was found, None otherwise.
        :raises ValueError if the key is None
        """
        if key is None:
            raise ValueError("Cannot search for null key!")
        current = self.root
        while current is not None:
            if current.key == key:
                return current.value
            elif current.key < key:
                current = current.right
            else:
                current = current.left

        return None

    def insertNode(self, key, value):
        """Inserts a new node into AVL tree.
        :param key: Key of the new node.
        :param value: Data of the new node. Must not be None. Nodes with the same key
        are not allowed. In this case False is returned. None-Keys and None-Values are
        not allowed. In this case an error is raised.
        :return True if the insert was successful, False otherwise.
        :raises ValueError if the key or value is None.
        """
        if key is None:
            raise ValueError("Null keys are not allowed!")

        if self.root is None:
            self.root = AVLNode(key, value)
            self.size += 1
            return True
        else:
            current = self.root
            while True:
                if current.key == key:
                    return False
                elif current.key < key:
                    if current.right is not None:
                        current = current.right
                    else:
                        self.set_right(current, AVLNode(key, value))
                        break
                else:
                    if current.left is not None:
                        current = current.left
                    else:
                        self.set_left(current, AVLNode(key, value))
                        break
        self.size += 1

        

        while current is not None:
            self.update_height(current)
            current = self.rebalance(current)
            current = current.parent

        return True

    def update_height(self, node):

        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node.height if node else -1


    def get_height(self, node):
        return node.height if node else -1


    def get_balance(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        return 0


    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.update_height(x)
        self.update_height(y)
        return y



    def rebalance(self, node):

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1: 
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right  = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node



    def removeNode(self, key):
        """Removes node with given key.
        :param key: Key of node to remove.
        :return True If node was found and deleted, False otherwise.
        @raises ValueError if the key is None.
        """
        if key is None:
            raise ValueError("Null key is not allowed!")

        def _delete_node(node):
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right
            node.key, node.value = predecessor.key, predecessor.value
            node.left = _delete_node(node.left)
            return node

        #def _remove_and_rebalance(node, key):
        #    if not node:
       #         return node
      #      if key < node.key:
     #           node.left = _remove_and_rebalance(node.left, key)
    #        elif key > node.key:
   #             node.right = _remove_and_rebalance(node.right, key)
  #          else:
 #               node = _delete_node(node)
#
    #        if not node:
   #             return None
  #          self.update_height(node)
 #           return self.rebalance(node)
#
      #  self.root = _remove_and_rebalance(self.root, key)
     #   self.size -= 1
    #    return True

            

        current = self.root
        parent = None
        while current:
            if current.key == key:
                if parent is None:
                    self.root = self._remove_bst(current)
                if self.root:
                    self.root.parent = None
            elif parent.left == current:
                new_sub_root = self._remove_bst(current)
                self.set_left(parent, new_sub_root)
            elif parent.right == current:
                new_sub_root = self._remove_bst(current)
                self.set_right(parent, new_sub_root)
            else:
                raise ValueError()
            self.size -= 1

            while parent:
                parent = self.rebalance(parent)
                parent = parent.parent
            return True
        parent = current
        current = current.left if key < current.key else current.right
        return False

    # auxiliary functions

    def _remove_bst(self, old_sub_root):
        new_sub_root = None
        if old_sub_root.left is None and old_sub_root.right is None:
            new_sub_root = None
            self.to_restruct = old_sub_root.parent
        elif old_sub_root.left is None:
            new_sub_root = old_sub_root.right
            self.to_restruct = new_sub_root
        elif old_sub_root.right is None:
            new_sub_root = old_sub_root.left
            self.to_restruct = new_sub_root
        elif old_sub_root.left.right is None:
            new_sub_root = old_sub_root.left
            self.set_right(new_sub_root, old_sub_root.right)
            self.to_restruct = new_sub_root
        elif old_sub_root.right.left is None:
            new_sub_root = old_sub_root.right
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = new_sub_root
        else:
            new_sub_root = old_sub_root.left
            while new_sub_root.right is not None:
                new_sub_root = new_sub_root.right
            predecessor_p = new_sub_root.parent
            self.set_right(predecessor_p, new_sub_root.left)
            self.set_right(new_sub_root, old_sub_root.right)
            self.set_left(new_sub_root, old_sub_root.left)
            self.to_restruct = predecessor_p

        return new_sub_root

    def set_left(self, parent, child):
        parent.left = child
        if child is not None:
            child.parent = parent

    def set_right(self, parent, child):
        parent.right = child
        if child is not None:
            child.parent = parent

#added
def is_balanced(self, node):
    return abs(self.get_balance(node)) <= 1
