from common.tree_type import Tree, Node
from common.create_test_data import create_rbt

def insert_fixup_node_rbt(tree:Tree, node: Node):
    while node.parent.color == 'red':
        if node.parent is node.parent.parent.l_child:
            y = node.parent.parent.r_child
            if y.color == 'red':
                node.parent.color = 'black'
                y.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                pass
                # TODO

def insert_node_rbt(tree:Tree, node: Node):
    y = None
    x = tree.root
    while x is not None:
        y = x
        if node.value < x.value:
            x = x.l_child
        else:
            x = x.r_child
    node.parent = y

    if y is None:
        tree.root = node
    elif node.value < y.value:
        y.l_child = node
    else:
        y.r_child = node
    node.l_child = None
    node.r_child = None
    node.color = 'red'
    insert_fixup_node_rbt(tree, node)









node_26,node_17,node_41,node_14,node_21,node_30,node_47,node_10,node_16,node_19,node_23,node_28,node_38,node_40,node_48,node_7,node_12,node_15,node_20,node_35,node_39 = create_rbt()
tree = Tree(root=node_26)