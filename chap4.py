
def list_output(l):
    if not l:
        print("No list")
        return
    last_index = len(l[-1])
    concatenated = ", ".join(l)
    print(concatenated)
    total_charts = len(concatenated)
    insertion = total_charts - last_index
    concatenated = concatenated[0:insertion] + "and " + concatenated[insertion:]
    print(concatenated)

test = [ "spam", "eggs", "bacon", "spam"]
list_output(test)


def swap(a, b):
    tmp = a
    a = b
    b = tmp
def pic_grid(l):
    out_grid = [[0 for i in range(len(l))] for i in range(len(l[0]))]
    for i, row in enumerate(l):
        for j, col in enumerate(row):
            out_grid[j][i] = l[i][j]
    print(out_grid)

grid = [[ ".",".",".",".",".","."],
        [ ".","0","0",".",".","."],
        [ "0","0","0","0",".","."],
        [ "0","0","0","0","0","."],
        [ ".","0","0","0","0","0"],
        [ "0","0","0","0","0","."],
        [ "0","0","0","0",".","."],
        [ ".","0","0",".",".","."],
        [ ".",".",".",".",".","."]]
pic_grid(grid)
