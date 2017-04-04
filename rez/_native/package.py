"""
This makes a standalone rez package from the current rez installation.

Note: This package intentionally does not provide commandline tools, as these
would interfere with the rez installation's own commandline tools. This package
provides the rez API only.
"""

name = "rez"

@early()
def version():
    return this._version()

authors = [
    "Allan Johns"
]

description = \
    """
    An integrated package configuration, build and deployment system for software.
    """

@early()
def variants():
    py_ver = this._python_version()
    py_major = py_ver.split('.')[0]
    return [
        ["python-%s" % py_major]
    ]

uuid = "recipes.rez"

build_command = "python {root}/install.py"

def commands():
    env.PATH.append("{this.root}/bin")
    env.PYTHONPATH.append("{this.root}/python")

_native = True


# --- internals

def _version():
    from rez.package_py_utils import exec_command
    import os.path
    import sys

    rez_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    rez_exe = os.path.join(rez_dir, "rez")

    out, err = exec_command(
        "version",
        [rez_exe, "--version"])

    # https://bugs.python.org/issue18920
    txt = err or out

    # output is like 'Rez 2.10.0'
    return txt.split()[-1]


def _python_version():
    from rez.package_py_utils import exec_python

    out = exec_python(
        "_python_version",
        ["import sys",
         "print sys.version.split()[0]"],
         executable="rez-python")

    return out
