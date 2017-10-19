import base64
import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def stringify(binary_file_path):
    """
    convert a binary file into a base64 string
    :param binary_file_path: string representing the file path
    :return: base64 string
    """
    logger.debug('stringifying {}'.format(binary_file_path))

    with open(binary_file_path, 'rb') as f:
        encoded_string = base64.b64encode(f.read())

    return encoded_string


def _file_name_to_var(binary_file_path):
    """
    converts a file path into a python-valid variable name
    :param binary_file_path: the full path, including extension
    :return: a valid python variable name
    """
    var_name = os.path.basename(binary_file_path).split('.')[0]  # remove the extension
    var_name = var_name.replace('-', '_')  # replace dashes with underscores

    return var_name


def bin_to_py_file(binary_file_path, destination_file='binary.py', overwrite=True):
    """
    creates a single file containing a single python variable

    :param binary_file_path: path to a binary file
    :param destination_file: the path to which to save the new variable, including the '.py' extension
    :param overwrite: True or False
    :return: None
    """
    logger.debug('attempting to save {} to {}'.format(binary_file_path, destination_file))

    if os.path.exists(destination_file) and not overwrite:
        raise ValueError('the file {} already exists and the overwrite flag is False'.format(destination_file))

    if os.path.splitext(destination_file)[1] != '.py':
        raise ValueError('the destination file must be a python type (extension must be ".py")')

    if not os.path.isfile(binary_file_path):
        raise ValueError('the file specified is not a file or does not exist')

    var_name = _file_name_to_var(binary_file_path)
    var_data = stringify(binary_file_path)

    py_file = '{} = {}\n'.format(var_name, var_data)

    with open(destination_file, 'w') as f:
        f.write(py_file)


def dir_to_py_file(directory_path, destination_file='binary.py', overwrite=True):
    """
    creates a single python file containing multiple variables representing binary files found
    in the 'directory_path'

    :param directory_path: path to a directory
    :param destination_file: the path to which to save the new variables, including the '.py' extension
    :param overwrite: True or False
    :return: None
    """
    logger.debug('attempting to save all files from {} to {}'.format(directory_path, destination_file))

    if os.path.exists(destination_file) and not overwrite:
        raise ValueError('the file {} already exists and the overwrite flag is False'.format(destination_file))

    if os.path.splitext(destination_file)[1] != '.py':
        raise ValueError('the destination file must be a python type (extension must be ".py")')

    if not os.path.isdir(directory_path):
        raise ValueError('the path specified is not a directory')

    py_file = ''

    for root, _, files in os.walk(directory_path):
        for name in files:
            file_path = os.path.join(root, name)

            var_name = _file_name_to_var(file_path)
            var_data = stringify(file_path)

            py_file += '{} = {}\n'.format(var_name, var_data)

    py_file += '\n'

    with open(destination_file, 'w') as f:
        f.write(py_file)
