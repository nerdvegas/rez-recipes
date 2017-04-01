"""
This makes a python rez package from the current system python install.

Note that the resulting package references the python system install; changing
the system install (via apt, yum, other) will invalidate this package.
"""

name = "python"

@early()
def version():
    return this.__version + "-native"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

@early()
def tools():
    version_parts = this.__version.split('.')

    return [
        "2to3",
        "pydoc",
        "python",
        "python%s" % (version_parts[0]),
        "python%s.%s" % (version_parts[0], version_parts[1])
    ]

uuid = "recipes.python"

def commands():
    env.PATH.append("{this._bin_path}")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

_native = True

@early()
def _site_paths():
    from rez.package_py_utils import exec_python
    import ast

    out = exec_python(
        "_site_paths",
        ["import site",
         "print site.getsitepackages()"])

    return ast.literal_eval(out.strip())


# --- internals

@early()
def _bin_path():
    from rez.package_py_utils import exec_python

    return exec_python(
        "_bin_path",
        ["import sys, os.path",
         "print os.path.dirname(sys.executable)"])


def _version():
    from rez.package_py_utils import exec_python

    return exec_python(
        "version",
        ["import sys",
         "print sys.version.split()[0]"])


__version = _version()
