import pyperclip
text = pyperclip.paste()
print(text)

text_line = text.split("\n")
for i in range(len(text_line)):
    text_line[i] = '- ' + text_line[i]
    print(text_line[i])

new_text = '\n'.join(text_line)
pyperclip.copy(new_text)
