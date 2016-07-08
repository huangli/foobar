def create_list( grid):

    def t(x, y):
        print grid[x][y]

    t(1,1)

# l1 = [1,2,3,4]
# def get_yield():
#     for i in l1:
#         yield i

if __name__ == "__main__":
    # for i in get_yield():
        # print i
    l1 = [[1,2,3],[4,5,6],[7,8,9]]
    create_list(l1)
