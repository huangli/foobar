class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = []
        self.right = []

    def add_left(self, obj):
        self.left.append(obj)

    def add_right(self, obj):
        self.right.append(obj)

def create_tree(grid, x, y, node):
    row = len(grid)
    column = len(grid[0])
    # result = [-1] * (row + column - 1)
    # no doors
    if ((x+1 > row) and (y+1 > column)):
       return node
    else:
        node.data = grid[x][y]
    # create node
    if (x+1 < row):
        left = Node(-1)
        node.add_left(left)
        create_tree(grid, x+1, y, left)
    if (y+1 < column):
        right = Node(-1)
        node.add_right(right)
        create_tree(grid, x, y+1, right)

    return node


if __name__ =="__main__":
    l1 = [[1,2,3], [4,5,6], [7,8,9]]
    start_node = Node(0)
    create_tree(l1, 0, 0, start_node)
    # n = Node(0)
    # l = Node(4)
    # m = Node(2)
    # n.add_left(l)
    # n.add_right(m)
    # for c in n.left:
    #     print c.data
    # for c in n.right:
    #     print c.data
    # print n.data
    # n.data = 1
    # print n.data
