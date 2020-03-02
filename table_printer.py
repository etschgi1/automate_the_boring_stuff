tableData = [['oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    table_length = []  # Stores individual table length
    output = []
    for table in data:
        text = table_to_string(table)
        table_length.append(len(text))
        output.append(text)
    table_size = max(table_length)
    for text in output:
        print(text.rjust(table_size))


def table_to_string(tablenum):
    string = ""
    for word in tablenum:
        word = word + " "
        string += word.title()
    return string


print_table(tableData)
