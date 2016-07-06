def answer(food, grid):


    class Node(object):
        def __init__(self, data):
            self.data = data
            self.left = []
            self.right = []

        def add_left(self, obj):
            self.left.append(obj)

        def add_right(self, obj):
            self.right.append(obj)
# traverse the tree list
# grid: the array to convert from
# x: the start row poistion of the root in grid, start from 0
# y: the start column poistion of the root in grid, start from 0
# node: the node to add
# return: turn into a tree from a grid
    def create_tree(grid, x, y, node):
        row = len(grid)
        column = len(grid[0])

        # no doors
        if ((x+1 > row) and (y+1 > column)):
           return node
        # setting node value
        else:
            node.data = grid[x][y]
        # create children
        if (x+1 < row):
            left = Node(-1)
            node.add_left(left)
            create_tree(grid, x+1, y, left)
        if (y+1 < column):
            right = Node(-1)
            node.add_right(right)
            create_tree(grid, x, y+1, right)

        return node

# traverse the tree list
# food_for_zombie: food need for zombie to leavel the room
# result: all the food needed saved in the list
# child_node: child node of the tree
# return: a list of each road zombie food needed
    def traverse(food_for_zombie, result, child_node):

        # dead road, the end of tree
        if (not child_node.left and not child_node.right):
            food_for_zombie += child_node.data
            result.append(food_for_zombie)
            food_for_zombie = 0
            return result
        elif (not child_node):
            return result
        else:
            food_for_zombie += child_node.data
            # left node
            if child_node.left:
                traverse(food_for_zombie, result, child_node.left[0])
            # right node
            if child_node.right:
                traverse(food_for_zombie, result, child_node.right[0])
            return result

    start_node = Node(0)
    create_tree(grid, 0, 0, start_node)
    result = traverse(0, [], start_node)

    # filter the food left, pick the smallest one
    food_left = food
    for zombie_food_needed in result:
        if food >= zombie_food_needed:
            temp = food - zombie_food_needed
            if temp < food_left:
                food_left = temp

    if food_left == food:
        return -1
    else:
        return food_left


if __name__ =="__main__":
    print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    # l1 = [[1,2,3], [4,5,6], [7,8,9]]
    # print answer(10, l1)

    # result = [-1] * 31
    # l1 = [[1,2], [3, 4]]
    # result = [-1] * 7
    # l2 = create_tree(l1, 0, 0, result, 0)
    # print l2
    # l3 = []
    # re = traverse(l2, 0, 0, l3)
    # print re
    # print len(l2)
