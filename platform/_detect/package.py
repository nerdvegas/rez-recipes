name = "platform"

description = \
    """
    Platform (eg linux, osx, windows)
    """

@early()
def version():
    from rez.system import system
    return system.platform

uuid = "recipes.platform"
