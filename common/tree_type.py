from itertools import count


class Node(object):
    _ids = count(1)

    def __init__(self, value, l_child=None, r_child=None, parent=None, color=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child
        self.parent = parent
        self.color = color
        self.id = next(self._ids)

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.l_child or self.r_child)

    def is_r_child(self):
        return self.parent and self.parent.r_child is self

    def is_l_child(self):
        return self.parent and self.parent.l_child is self

    def check_l_child(self):
        return True if self.l_child else False

    def check_r_child(self):
        return True if self.r_child else False

    def check_both_child(self):
        return True if self.l_child and self.r_child else False

    def check_any_child(self):
        return True if self.l_child or self.r_child else False

    def print_node(self):
        l_child_val, r_child_val, parent_val = None, None, None
        if not self.is_root():
            parent_val = self.parent.value
        if self.check_l_child():
            l_child_val = self.l_child.value
        if self.check_r_child():
            r_child_val = self.r_child.value
        print('[value:%s l_child_val:%s r_child_val:%s parent_val:%s]' % (self.value, l_child_val, r_child_val, parent_val))


class Tree(object):

    def __init__(self, root = None):
        if isinstance(root, (Node, type(None))):
            self.root = root

def print_subtree(node):
    if node is not None:
        node.print_node()
        print_subtree(node.l_child)
        print_subtree(node.r_child)
