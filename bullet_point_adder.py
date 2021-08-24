#! python3

import pyperclip
text = pyperclip.paste()
split_lines = text.split("\n")
for i in range(len(split_lines)):
    split_lines[i] = '* ' + split_lines[i]
text = '\n'.join(split_lines)


pyperclip.copy(text)