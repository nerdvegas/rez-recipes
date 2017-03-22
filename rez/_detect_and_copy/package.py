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


# --- internals

def _exec(attr, cmd):
    import subprocess

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode:
        from rez.exceptions import InvalidPackageError
        raise InvalidPackageError(
            "Error determining package attribute '%s':\n%s" % (attr, err))

    return out.strip(), err.strip()


def _version():
    out, err = _exec(
        "version",
        ["rez", "--version"])

    # https://bugs.python.org/issue18920
    txt = err or out

    # output is like 'Rez 2.10.0'
    return txt.split()[-1]


def _python_version():
    out, _ = _exec(
        "_python_version",
        ["rez-python", "-c", "import sys; print sys.version.split()[0]"])

    return out
