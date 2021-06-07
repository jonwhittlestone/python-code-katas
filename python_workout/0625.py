
print('Chapter 06 - Exercise 25')
print('')
print('XML Generator')

def myxml(root_node, root_value='', **kwargs):
    """Reverses lines of input file to new output file
    Examples:
        `myxml('foo')` -> `<foo></foo>` 
        `myxml('foo', 'bar')` -> `<foo>bar</foo>` 
        `myxml('foo', 'bar', a=1, b=2, c=3)` -> `<foo a="1" b="2" c="3">bar</foo>` 
    Args:
        root_node (str): The tag
        root_value (str): The value of the tag
         *args: Variable length argument list representing root node attributes

    Returns:
        str: XML
    """
    attrs = ''.join([f' {key}="{value}"'
                        for key, value in kwargs.items()])
    return f"<{root_node}{attrs}>{root_value}</{root_node}"

if __name__ == '__main__':
    node = 'foo'
    value = 'bar'
    print(myxml(node, value, a=1))