
name = "rezgui"

@early()
def version():
    return this.__version

authors = [
    "Allan Johns"
]

description = \
    """
    GUI for the Rez packaging system.
    """

@early()
def requires():
    parts = this.__version.split('.')
    major = int(parts[0])
    minor = int(parts[1])

    rez_req = "rez-%d.%d+<%d" % (major, minor, major + 1)
    return [rez_req]

@early()
def variants():
    py_ver = this._python_version()
    py_major = py_ver.split('.')[0]
    return [
        ["python-%s" % py_major]
    ]

tools = [
    "rez-gui"
]

uuid = "recipes.rezgui"

build_command = "python {root}/install.py"

def commands():

    gui_libs = ["PySide", "PyQt"]
    if not any(x in resolve for x in gui_libs):
        stop("No GUI library present, expected one of: %s", gui_libs)

    env.PATH.append("{this.root}/bin")
    env.PYTHONPATH.append("{this.root}/python")

_native = True


# --- internals

def _version():
    from rez.package_py_utils import exec_command

    out, err = exec_command(
        "version",
        ["rez", "--version"])

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


__version = _version()
