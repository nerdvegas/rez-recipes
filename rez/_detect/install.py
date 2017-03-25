import subprocess
import shutil
import sys
import os
import os.path
import stat


if __name__ == "__main__":
    if os.getenv("REZ_BUILD_INSTALL") != "1":
        print >> sys.stderr, "Nothing to do (install with -i)."
        sys.exit(0)

    install_path = os.getenv("REZ_BUILD_INSTALL_PATH")

    install_py_path = os.path.join(install_path, "python")
    if not os.path.exists(install_py_path):
        os.mkdir(install_py_path)

    p = subprocess.Popen(
        ["rez-python", "-c", "import rez; print rez.__path__[0]"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, _ = p.communicate()
    site_path = os.path.dirname(out)

    filemode = stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH
    dirmode = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH | filemode

    for dirname in ("rez", "rezplugins"):
        src_path = os.path.join(site_path, dirname)
        dest_path = os.path.join(install_py_path, dirname)

        if os.path.exists(dest_path):
            print >> sys.stderr, "Package already installed."
            sys.exit(1)

        ignore = shutil.ignore_patterns("*.pyc", "*.pyo")
        shutil.copytree(src_path, dest_path, ignore=ignore)

        # make read-only
        for root, dirs, files in os.walk(dest_path):
            for name in files:
                os.chmod(os.path.join(root, name), filemode)
            for name in dirs:
                os.chmod(os.path.join(root, name), dirmode)

        os.chmod(dest_path, dirmode)
