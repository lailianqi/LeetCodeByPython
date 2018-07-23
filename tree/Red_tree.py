class Color:
    pass


class Black(Color):
    def __init__(self):
        pass


class Red(Color):
    def __init__(self):
        pass


class Entry(object):
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = Black()


def rotateLeft(p, root):
    '''
    :type p: Entry 要旋转的节点
    '''
    if p is not None:
        r = p.right
        p.right = r.left
        if r.left is not None:
            r.left.parent = p
        r.parent = p.parent
        if p.parent is None:
            root = r
        elif p == p.parent.left:
            p.parent.left = r
        else:
            p.parent.right = r
        r.left = p
        p.parent = r
