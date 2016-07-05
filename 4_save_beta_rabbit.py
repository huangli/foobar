def answer(food, grid):

# traverse the tree list
# x: the start row poistion of the root in grid, start from 0
# y: the start column poistion of the root in grid, start from 0
# result: the result tree list
# index: list node position, the left node = root*2 + 1, right node = root*2 + 2
    def create_tree(grid, x, y, result, index):
        row = len(grid)
        column = len(grid[0])
        # result = [-1] * (row + column - 1)
        # no doors
        if ((x+1 > row) and (y+1 > column)):
           return result
        else:
           result[index] = grid[x][y]
        # create node
        if (x+1 < row):
           create_tree(grid, x+1, y, result, index*2+1)
        if (y+1 < column):
           create_tree(grid, x, y+1, result, index*2+2)

        return result

# traverse the tree list
# x: the start row poistion of the root in grid, start from 0
# y: the start column poistion of the root in grid, start from 0
    def traverse(tree, x, food_for_zombie, result):
        tree_len = len(tree)

        # print "x: " + str(x)
        # print "food: " + str(food_for_zombie)
        # dead road
        if (2*x + 1 >= tree_len and tree[x] != -1):
            food_for_zombie += tree[x]
            result.append(food_for_zombie)
            food_for_zombie = 0
            return result
        elif (tree[x] == -1):
            return result
        else:
            food_for_zombie += tree[x]
            # left node
            traverse(tree, 2*x+1, food_for_zombie, result)
            # right node
            traverse(tree, 2*x+2, food_for_zombie, result)
            return result

    row = len(grid)
    column = len(grid[0])

    tree = [-1] * (pow(2, row+column-1) - 1)
    tree = create_tree(grid, 0, 0, tree, 0)
    # print tree
    result = traverse(tree, 0, 0, [])
    # print result
    can_be_save = False
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
    # result = [-1] * 31
    # l1 = [[1,2], [3, 4]]
    # result = [-1] * 7
    # l2 = create_tree(l1, 0, 0, result, 0)
    # print l2
    # l3 = []
    # re = traverse(l2, 0, 0, l3)
    # print re
    # print len(l2)
