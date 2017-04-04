
name = "PyQt"

@early()
def version():
    return this._version() + "-native"

description = \
    """
    Python binding of the cross-platform GUI toolkit Qt.
    """

@early()
def requires():
    from rez.package_py_utils import find_site_python
    py_package = find_site_python("PyQt4")
    return [py_package.qualified_name]

build_command = False

uuid = "recipes.pyqt"

def commands():
    # Qt.py support
    env.QT_PREFERRED_BINDING = "PyQt4"

_native = True


# --- internals

def _version():
    from rez.package_py_utils import exec_python

    return exec_python(
        "_version",
        ["from PyQt4.QtCore import QT_VERSION_STR",
         "print QT_VERSION_STR"])
