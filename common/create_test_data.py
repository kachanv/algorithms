from common.tree_type import Node


# create binary search tree
def create_bst():
    # create nodes
    node_5 = Node(50)
    node_3 = Node(30, parent=node_5)
    node_7 = Node(70, parent=node_5)
    node_2 = Node(20, parent=node_3)
    node_4 = Node(40, parent=node_3)
    node_6 = Node(60, parent=node_7)
    node_9 = Node(90, parent=node_7)
    node_1 = Node(10, parent=node_2)
    node_8 = Node(80, parent=node_9)
    node_10 = Node(100, parent=node_9)
    # create links
    node_5.l_child = node_3
    node_5.r_child = node_7
    node_3.l_child = node_2
    node_3.r_child = node_4
    node_2.l_child = node_1
    node_7.l_child = node_6
    node_7.r_child = node_9
    node_9.l_child = node_8
    node_9.r_child = node_10

    r"""
    Binary search tree
                   50(5)
                  /     \
              30(3)      70(7)
              /   \     /    \
          20(2) 40(4)  60(6) 90(9)
           /                 /    \
         10(1)            80(8)   100(10) 
    """
    return node_5, node_3, node_7, node_2, node_4, node_6, node_9, node_1, node_8, node_10
