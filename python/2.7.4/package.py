name = "python"

version = "2.7.4"

authors = [
    "Guido van Rossum"
]

description = \
    """
    The Python programming language.
    """

variants = [
    ["platform-osx", "arch-x86_64", "os-osx-10"]
]

tools = [
    "2to3",
    "idle",
    "pydoc",
    "python",
    "python2",
    "python2.7",
    "python2.7-config",
    "python2-config",
    "python-config",
    "smtpd.py"
]

uuid = "recipes.python"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python2.7")

    if building:
        env.PYTHON_INCLUDE_DIR = "{root}/include/python2.7"

        # only used to see libpythonX.X.a file
        env.LD_LIBRARY_PATH.append("{root}/lib")
