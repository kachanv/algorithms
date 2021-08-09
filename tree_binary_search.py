from common.tree_type import Node, Tree, print_subtree
from common.create_test_data import create_bst


# O(h)
def search_bts_recursion(root: Node, value: object) -> (Node, None):
    if root is None or root.value == value:
        return root
    else:
        if value < root.value:
            return search_bts_recursion(root.l_child, value)
        else:
            return search_bts_recursion(root.r_child, value)


# O(h)
def search_bts_iterative(root: Node, value: object) -> (Node, None):
    while root is not None and root.value != value:
        if value < root.value:
            root = root.l_child
        else:
            root = root.r_child
    return root


# O(h)
def search_bts_min(root: Node) -> Node:
    while root.l_child is not None:
        root = root.l_child
    return root


# O(h)
def search_bts_max(root: Node) -> Node:
    while root.r_child is not None:
        root = root.r_child
    return root


# O(h)
def search_bts_successor(node: Node) -> (Node, None):
    # if exists right subtree, search min el. of it
    if node.check_r_child():
        return search_bts_min(node.r_child)
    # else search higher el. and it be l_child
    else:
        p = node.parent
        while p is not None and node.value == p.r_child.value:
            node = p
            p = p.parent
        return p


# O(h)
def search_bts_predecessor(node: Node) -> (Node, None):
    # if exists left subtree, search max el. of it
    if node.check_l_child():
        return search_bts_max(node.l_child)
    # else search higher el. and it be r_child
    else:
        p = node.parent
        while p is not None and node.value == p.l_child.value:
            node = p
            p = p.parent
        return p


# O(h)
def insert_node_bst(tree: Tree, node: Node):
    # search parent for new node
    y = None  # closing pointer
    x = tree.root
    while x is not None:
        y = x
        if node.value < x.value:
            x = x.l_child
        else:
            x = x.r_child
    node.parent = y
    # now, define type of child (L or R)
    if y is None:
        tree.root = node
    elif node.value < y.value:
        y.l_child = node
    else:
        y.r_child = node


# O(1)
def transplant_node_bst(tree: Tree, node_was: Node, node_will: Node):
    # replace subtree by other subtree
    if node_was.is_root():
        tree.root = node_will
    elif node_was.id == node_was.parent.l_child:
        node_was.parent.l_child = node_will
    else:
        node_was.parent.r_child = node_will
    if node_will is not None:
        node_will.parent = node_was.parent


# O(h)
def delete_node_bst(tree: Tree, node: Node):
    if node.l_child is None:
        transplant_node_bst(tree, node, node.r_child)
    elif node.r_child is None:
        transplant_node_bst(tree, node, node.l_child)
    else:
        y = search_bts_min(node.r_child)
        if y.parent != node:
            transplant_node_bst(tree, y, y.r_child)
            y.r_child = node.r_child
            y.r_child.parent = node
        transplant_node_bst(tree, node, y)
        y.l_child = node.l_child
        y.l_child.parent = y


# O(1)
def left_rotate_bst(tree: Tree, node: Node):
    if node.check_r_child():
        y = node.r_child
        node.r_child = y.l_child
        if y.check_l_child():
            y.l_child.parent = node
        y.parent = node.parent
        if node.is_root():
            tree.root = y
        elif node.parent.l_child is node:
            node.parent.l_child = y
        else:
            node.parent.r_child = y
        y.l_child = node
        node.parent = y


# test bst
node_5, node_3, node_7, node_2, node_4, node_6, node_9, node_1, node_8, node_10 = create_bst()
tree = Tree(root=node_5)

node_11 = Node(value=85)
node_12 = Node(value=5)

print(
    r"""    
    Binary search tree
                   50(5)
                  /     \
              30(3)      70(7)
              /   \     /    \
          20(2) 40(4)  60(6) 90(9)
           /                 /    \
         10(1)            80(8)   100(10)
         /                  \
        5(12 insert)         85(11 insert/delete)
    """
)

print('- search 10 by recurcion')
search_bts_recursion(node_5, 10).print_node()
print('- search 100 by iterative')
search_bts_iterative(node_5, 100).print_node()
print('- search min')
search_bts_min(node_5).print_node()
print('- search max')
search_bts_max(node_5).print_node()
print('- search successor by 4-th node')
search_bts_successor(node_4).print_node()
print('- search predcessor by 8-th node')
search_bts_predecessor(node_8).print_node()
print('- insert 11-th and 12-th nodes')
insert_node_bst(tree, node_11)
insert_node_bst(tree, node_12)
node_11.print_node()
node_12.print_node()
print('- delete 11-th node')
delete_node_bst(tree, node_11)
print('- left rotate from 9-th node')
left_rotate_bst(tree, node_9)
print_subtree(node_5)