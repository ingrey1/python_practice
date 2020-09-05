# https://www.coursera.org/learn/principles-of-computing-2/supplement/qDdHk/math-notes-on-trees


# tree class implementation: http://www.codeskulptor.org/#poc_tree.py
# evaluate arithmetic expression recursively: http://www.codeskulptor.org/#poc_arith_expression.py
# tic tac toe mini-max discussion: https://www.coursera.org/learn/principles-of-computing-2/supplement/445vX/math-notes-on-minimax

# rooted tree: collection of nodes and edges that can be organized recursively, as follows
    # tree:
      # root node
        # no parent
      # a value
      #  list of references to a collection of subtrees
      # all nodes, besides root node, have exactly one parent
      # trees are a special type of graph
        # an unrooted tree is a graph with n nodes and n - 1 edges
          # any pair of nodes is connected by a sequence of edges
      # nodes of a tree are typically classified based on the number of children
        # internal nodes: nodes with one or more children
        # leaf nodes: nodes with no children
        # internal versus leaf node distinction allows for important recursive algorithms
          # The number of nodes in a tree satisfies:
             # If the root node of the tree is a leaf:
                # The number of nodes in a tree satisfies: If the root node of the tree is a leaf: 
                  # return 1 
                  # else: return 1 + the sum of the number of nodes for each subtree       
def node_count(root):
 '''recursively count size of tree'''
 if not root.left and not root.right: # tree with no edges has size 1 
   return 1
 
 return 1 + node_count(root.left) + node_count(root.right)


                # The number of leafs in a tree satisfies:
                            # if the root node of the tree is a leaf:
                            # return 1
                            # else: return the sum of the number of leaves for each subtree
def leaf_count(root):
  '''recursively count number of leaves of tree'''
  if not root.left and not root.right: # tree with no children is a leaf
      return 1
  
  return leaf_count(root.left) + leaf_count(root.right)

# the height of a tree is the longest sequence of edges from the root to a leaf
def tree_height(root):
  '''recursively count height of tree'''
  if not root.left and not root.right: # root node of tree is leaf
      return 0

  height_left = tree_height(root.left)
  height_right = tree_height(root.right) 

  return 1 + (height_left if height_left > height_right else height_right) 
  
# In general, the nodes of a tree can have any number of children
#  including just a single child.
#  One particularly important class of trees are binary trees
  #  in which all nodes have two or fewer children.
  #  Binary trees: in which all internal nodes
     #  that have exactly two children are called full binary trees.
     #  Full binary trees often arise in applications involving searching and sorting.
     # a perfect binary tree is one in which every leaf has the same depth
     # perfect binary tree has number of leaves: n = 2 ^ h
     # perfect binary tree has internal nodes: (2 ^ h) - 1
     # perfect binary tree has total nodes: (2 ^ (h + 1)) - 1
     # perfect binary tree has n nodes at height h: n = 2 ^ h 
     # notes: http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/bin-tree.html

# tree traversals:
  # Pre-order traversals - process root, process left subtree, process right subtree
  # Post-order traversals - process left subtree, process right subtree, process root
  # In-order traversals - process left subtree, process root, process right subtree

