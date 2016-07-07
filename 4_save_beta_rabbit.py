def answer(food, grid):

# traverse the tree list
# food_for_zombie: food need for zombie to leavel the room
# result: all the food needed saved in the list
# grid: the grid of the room
# x,y: the row and column index
# return: a list of each road zombie food needed
    def traverse(food, food_for_zombie, result, grid, x, y):
        row = len(grid)
        column = len(grid[0])

        # the exit of the grid
        if ((x+1 == row) and (y+1 == column)):
            food_for_zombie += grid[x][y]
            if food_for_zombie < food:
                result.append(food_for_zombie)
            elif food_for_zombie == food:
                result.append(food_for_zombie)
                return
            food_for_zombie = 0
            return result
        else:
            food_for_zombie += grid[x][y]
            # left node
            if x+1 < row:
                traverse(food, food_for_zombie, result, grid, x+1, y)
            # right node
            if y+1 < column:
                traverse(food, food_for_zombie, result, grid, x, y+1)
            return result

    result = traverse(food, 0, [], grid, 0, 0)
    # filter the food left, pick the smallest one
    if result:
        return food - max(result)
    else:
        return -1


if __name__ =="__main__":
    print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    # l1 = [[1,2,3], [4,5,6], [7,8,9]]
    # print answer(10, l1)
