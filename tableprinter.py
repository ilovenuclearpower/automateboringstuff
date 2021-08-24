

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def table_print(table) -> None:
    colwidths = [0] * len(tableData)
    lines = [ [] for i in range(len(tableData[0]))]
    print(lines)
    for i, col in enumerate(tableData):
        colmax = float("-inf")
        for val in col:
            colmax = max(colmax, len(val))
        colwidths[i] = colmax
    for i, col in enumerate(tableData):
        for j, val in enumerate(col):
            chars = list(val)
            blank_chars = [" "] * (colwidths[i] - len(chars) + 1)
            blank_chars.extend(chars)
            lines[j].append("".join(blank_chars))
    for line in lines:
        print("".join(line))
table_print(tableData)