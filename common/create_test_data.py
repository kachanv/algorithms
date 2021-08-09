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

    print(r"""
    Binary search tree
                   50(5)
                  /     \
              30(3)      70(7)
              /   \     /    \
          20(2) 40(4)  60(6) 90(9)
           /                 /    \
         10(1)            80(8)   100(10) 
    """)
    return node_5, node_3, node_7, node_2, node_4, node_6, node_9, node_1, node_8, node_10

def create_arr_for_sort():
    return [1,4,-7,9,3,-1,679,31,0,-9, 12,4,78,9,-2,-2,3,85,0]

def create_lessarr_for_sort():
    return [0.15,0.44,0.7,0.9,0.39,0.1,0.000679,0.0031,0,0.95,0.012,0.4,0.0078,0.009,0.2,0.29,0.3,0.085,0]

# create red_black_tree
def create_rbt():
    # create nodes
    node_26 = Node(26, color='black')
    node_17 = Node(17, parent=node_26, color='red')
    node_41 = Node(41, parent=node_26, color='black')
    node_14 = Node(14, parent=node_17, color='black')
    node_21 = Node(21, parent=node_17, color='black')
    node_30 = Node(30, parent=node_41, color='red')
    node_47 = Node(47, parent=node_41, color='black')
    node_10 = Node(10, parent=node_14, color='red')
    node_16 = Node(16, parent=node_14, color='black')
    node_19 = Node(19, parent=node_21, color='black')
    node_23 = Node(23, parent=node_21, color='black')
    node_28 = Node(28, parent=node_30, color='black')
    node_38 = Node(38, parent=node_30, color='black')
    node_40 = Node(40, parent=node_47, color='red')
    node_48 = Node(46, parent=node_47, color='red')
    node_7 = Node(7, parent=node_10, color='black')
    node_12 = Node(12, parent=node_10, color='black')
    node_15 = Node(15, parent=node_16, color='red')
    node_20 = Node(20, parent=node_19, color='red')
    node_35 = Node(35, parent=node_38, color='red')
    node_39 = Node(39, parent=node_38, color='red')
    # create links
    node_26.l_child = node_17
    node_26.r_child = node_41
    node_17.l_child = node_14
    node_17.r_child = node_21
    node_41.l_child = node_30
    node_41.r_child = node_47
    node_14.l_child = node_10
    node_14.r_child = node_16
    node_21.l_child = node_19
    node_21.r_child = node_23
    node_30.l_child = node_28
    node_30.r_child = node_38
    node_47.l_child = node_40
    node_47.r_child = node_48
    node_10.l_child = node_7
    node_10.r_child = node_12
    node_16.l_child = node_15
    node_19.r_child = node_20
    node_38.l_child = node_35
    node_38.r_child = node_39

    print(r"""
    Red black tree          26b
                        /         \  
                       /           \
                 17r                    41b
              /      \               /       \
             /        \             /         \
          14b          21b         30r          47b
       /      \       /    \      /   \       /     \
    10r       16b   19b   23b   28b   38b    40r     48r
  /    \      /        \             /   \
 7b     12b  15r       20r          35r   39r
    """)
    return node_26,node_17,node_41,node_14,node_21,node_30,node_47,node_10,node_16,node_19,node_23,node_28,node_38,node_40,node_48,node_7,node_12,node_15,node_20,node_35,node_39
