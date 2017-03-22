"""
This makes a python rez package from the current system python install.

Note that the resulting package references the python system install; changing
the system install (via apt, yum, other) will invalidate this package.
"""

name = "python"

@early()
def version():
    return this.__version + "-system"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**", "arch-**", "os-**"]
    return [expand_requires(*requires)]

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


# --- internals

def _exec_python(attr, src):
    import subprocess

    p = subprocess.Popen(
        ["python", "-c", src],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode:
        from rez.exceptions import InvalidPackageError
        raise InvalidPackageError(
            "Error determining package attribute '%s':\n%s" % (attr, err))

    return out.strip()


@early()
def _bin_path():
    return this._exec_python(
        "_bin_path",
        "import sys, os.path; print os.path.dirname(sys.executable)")


def _version():
    return _exec_python(
        "version",
        "import sys; print sys.version.split()[0]")


__version = _version()
