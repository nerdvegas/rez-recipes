name = "arch"

description = \
    """
    Architecture (eg x86_64)
    """

@early()
def version():
    from rez.system import system
    return system.arch

uuid = "recipes.arch"
