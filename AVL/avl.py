
"""
My notes:
AVL - an BST programmed to maintain the tree balanced, 
and so better complexity (thinking with the height at most less than 2*log n).
It mantains using rotations!!
We have single rotations (to right and left), and double rotations
(which uses single rotations twice)

AVL-sort -> Insert all nodes( O(n * h = n * log n [fact because avl])) and do in-order traversal (O(n)) - O(n*log n)
"""

"""
Code made by the MIT teacher with some parts missing (the tests functions and _str methods)
"""
class BSTNode(object):
    """A node in the vanilla BST tree."""
    
    def __init__(self, parent, k):
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            k: The key of the node we want to find.
        
        Returns:
            The node with key k.
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:  
                return None
            else:
                return self.right.find(k)
    
    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this 
        node.
        
        Returns:
            The node with the minimum key.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current
       
    def next_larger(self):
        """Returns the node with the next larger key (the successor) in the BST.
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.
        
        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)
  
    def delete(self):
        """Deletes and returns this node from the BST."""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()
    
    def check_ri(self):
        """Checks the BST representation invariant around this node.
    
        Raises an exception if the RI is violated.
        """
        if self.left is not None:
            if self.left.key > self.key:
                raise RuntimeError("BST RI violated by a left node key")
            if self.left.parent is not self:
                raise RuntimeError("BST RI violated by a left node parent "
                                   "pointer")
            self.left.check_ri()
        if self.right is not None:
            if self.right.key < self.key:
                raise RuntimeError("BST RI violated by a right node key")
            if self.right.parent is not self:
                raise RuntimeError("BST RI violated by a right node parent "
                                   "pointer")
            self.right.check_ri()

class BST(object):
    """A binary search tree."""
    def __init__(self, klass = BSTNode):
        """Creates an empty BST.
        
        Args:
            klass (optional): The class of the node in the BST. Default to 
                BSTNode.
        """
        self.root = None
        self.klass = klass
        
    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this 
        node.
        
        Args:
            k: The key of the node we want to find.
        
        Returns:
            The node with key k or None if the tree is empty.
        """
        return self.root and self.root.find(k)
                
    def find_min(self):
        """Returns the minimum node of this BST."""
        
        return self.root and self.root.find_min()
    
    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        
        Args:
            k: The key of the node to be inserted.
            
        Returns:
            The node inserted.
        """
        node = self.klass(None, k)
        if self.root is None:
            # The root's parent is None.
            self.root = node
        else:
            self.root.insert(node)
        return node
            
    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        
        Args:
            k: The key of the node that we want to delete.
            
        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = self.klass(None, 0)
            pseudoroot.left = self.root
            self.root.parent = pseudoroot
            deleted = self.root.delete()
            self.root = pseudoroot.left
            if self.root is not None:
                self.root.parent = None
            return deleted
        else:
            return node.delete()   
        
    def next_larger(self, k):
        """Returns the node that contains the next larger (the successor) key in
        the BST in relation to the node with key k.
        
        Args:
            k: The key of the node of which the successor is to be found.
            
        Returns:
            The successor node.
        """
        node = self.find(k)
        return node and node.next_larger()
    
    def check_ri(self):
        """Checks the BST representation invariant.
        
        Raises:
            An exception if the RI is violated.
        """
        if self.root is not None:
            if self.root.parent is not None:
                raise RuntimeError("BST RI violated by the root node's parent " 
                                   "pointer.")
            self.root.check_ri()


def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(BST):
    """
AVL binary search tree implementation.
Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    #double rotation
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    #double rotation
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node to be inserted.
        """
        node = super(AVL, self).insert(k)
        self.rebalance(node)

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node that we want to delete.
            
        Returns:
            The deleted node with key k.
        """
        node = super(AVL, self).delete(k)
        ## node.parent is actually the old parent of the node,
        ## which is the first potentially out-of-balance node.
        self.rebalance(node.parent)
