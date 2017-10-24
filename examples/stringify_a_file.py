import logging
from stringify import stringify, stringify_py

logging.basicConfig(level=logging.DEBUG)

# print the stringified representation of the yellow-dot.png file
print(stringify('binary_files/yellow-dot.png'))

# creates a python file 'images.py' from
# which one may import 'yellow_dot' to get the image data
stringify_py('binary_files/yellow-dot.png', destination_file='images.py')

# creates a single python file called
# 'my_directory.py' which contains string representations
# of 'yellow-dot.png' and 'green-dot.png' which accessible
# as variables 'yellow_dot' and 'green_dot'
stringify_py('binary_files', destination_file='my_directory.py')
