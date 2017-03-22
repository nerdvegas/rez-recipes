name = "python"

version = "2.7.4"

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

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
