name = "os"

description = \
    """
    Operating system (eg Ubuntu-16.04)
    """

@early()
def version():
    from rez.system import system
    return system.os

uuid = "recipes.os"

_native = True
