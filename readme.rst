----------------
Purpose
----------------

The ``stringify`` module allows you to easily include your project's binary files as python base64 strings.  This may not be useful for your little tkinter project until you try to bundle the project as an executable using pyinstaller.  Suddenly, you get to spend lots of time thinking about how to best write your spec files so that they capture the current files and any future changes as well.  Or you could use `stringify`.

----------------
Installation
----------------

Simply ``pip install stringify`` should do the trick.  You could also download this repository and ``python setup.py install``, but that isn't as fun, is it?

----------------
Use Case
----------------

Somewhere - probably within your module - you have a file that has static, non-code data.  You probably have a directory called ``images`` or ``bin`` that the python code references when building a GUI or executing a program... whatever.  This works great when using python directly - such as when you install the package via pip and call it from the command-line. This doesn't work so well when you try to bundle your package using `pyinstaller <http://www.pyinstaller.org/>`_, which doesn't natively recognize your non-code dependencies.

This library allows you to read those binary files into python code and include that data as python variables in your code base.

A quick note, this library has only been tested on relatively modestly-sized files - such as images.  Larger file packaging using this method has not been tested.

----------------
Quickstart
----------------

We will assume a project structure that starts begins as outlined below.  Note that the image paths are explicitly
called out as part of ``my_package/package_file_0.py``.::

    setup.py
    my_package/
        __init__.py
        package_file_0.py
        images/
            img1.png
            img2.png

==========================
Exile Binary Files
==========================

Move your binary files outside of the package that you wish to include them within.  We will put something in there to take their place, but dont worry about that for the moment.  Our new project structure::

    setup.py
    images/
        img1.png
        img2.png
    my_package/
        __init__.py
        package_file_0.py

==================================
Run ``dir_to_py_file()`` Utility
==================================

Our files are now located within `images` and our desired location will be ``images.py`` within the package.::

    from stringify import dir_to_py_file

    dir_to_py_file(source_path='images', destination_file='my_package/images.py')

Note that dashes will be replaced with underscores and spaces will be replaced with underscores and that the extensions will be removed before the name of the python variable is created.  For instance, ``green-dot one.png`` will become the variable ``green_dot_one``.

The source tree as it existed earlier remains intact, but we have an extra file within ``my_package`` called ``images.py``::

    setup.py
    images/
        img1.png
        img2.png
    my_package/
        __init__.py
        package_file_0.py
        images.py

Feel free to have a look at images.py, you can't hurt it and you can always regenerate it.  You should see two variables located within called ``img1`` and ``img2``.  Each of these has a long byte string assigned to it that can be easily referenced and mined for the data.

============================
Reference the Image Strings
============================

Recall that it was ``package_file_0.py`` that utilized the image data.  Within ``package_file_0.py``, import the new image strings::

    from images import img1, img2

Replace any absolute function calls to those images with the variable.  Note that some functions, such as ``tkinter.PhotoImage()`` can take image data directly in this format.::

    # tkinter.PhotoImage(file='./images/img1.png')  # replace this call...
    tkinter.PhotoImage(data=img1)                   # with this one

Depending on your use case, you may have to experiment with method of unpacking the data for use.

====================
Lock it Down
====================

To reduce the chances of messing this up later, you may wish to add this funcitonality to your workflow so that it is automatically completed as you are developing and distributing your package.  Simply include ``dir_to_py_file`` in your ``setup.py`` script for ``my_package`` just before the call to ``setup()``.::

    from setuptools import setup
    from stringify import dir_to_py_file

    dir_to_py_file(source_path='images', destination_file='my_package/images.py')

    setup(
        name='my_package',
        version=__version__,
        setup_requires=['stringify']
        ...

As shown, you may also wish to add ``stringify`` to your ``setup_requires``, but you will get an error on import if ``stringify`` isn't installed, so it won't mess up your packaging to skip this line.

=============================
Run your PyInstaller Script
=============================

Now that your files are simply bundled into your application, there should be nothing special about your package that requires ``MANIFEST.in`` or interferes with ``pyinstaller``.

Simply `pyinstaller my_package/package_file_0.py` (assuming that is where your entry point is), and you are ready to rock!

=======================
Drink
=======================

Now that you aren't spending all of your time trying to write customer pyinstaller scripts for your project, then you can celebrate by having a drink.  Enjoy!
