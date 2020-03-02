tableData = [['oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

tableData2 = [['oranges', 'cherries', 'banana', 'Alice', 'Bob', 'Carol',
               'David'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(data):
    """gets output text in strings; checks for size of table; 
    feeds everything to the output function
    """
    table_length = []  # Stores individual table length
    output = []  # Stores Output
    for table in data:  # for every subtable create a string to check length
        text = table_to_string(table)
        output.append(text)  # String added to output list
        table_length.append(len(text))
    table_size = max(table_length)  # creates a table size for rjust methode
    plot_table(text, output, table_size)


def plot_table(text, output, table_size):
    """Prints each line of the table and adds seperation charakters"""
    for text in output:
        print(text.rjust(table_size))
        if text == output[-1]:
            print("\n".rjust(table_size, "-"))


def table_to_string(tablenum):
    """Converts lists of words into single strings with one space between"""
    string = ""
    for word in tablenum:
        word = word + " "
        string += word.title()  # adds words in table together
    return string


print_table(tableData)
print_table(tableData2)
