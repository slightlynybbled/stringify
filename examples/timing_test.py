import timeit
import os
from stringify import unstringify
from my_text_directory import text0


my_list = []
path = os.path.join('text_files', 'text0.txt')


def from_text_file():
    with open(path, 'r') as f:
        my_list.append(f.read())


def from_stringified_var():
    my_list.append(unstringify(text0))


print('file read time: ',
      timeit.timeit(from_text_file, setup='my_list = []', number=10000))


print('var read time: ',
      timeit.timeit(from_stringified_var, setup='my_list = []', number=10000))

