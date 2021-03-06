import platform
import os

# Architectures for which we can build packages.
ARCHITECTURES = {'x86_64-unknown-cloudabi'}

# Temporary directory where packages will be built. This directory has
# to be fixed, as the compilation process tends to hardcode paths to the
# build directory. Debug symbols and __FILE__ use absolute paths.
DIR_BUILDROOT = '/usr/obj/cloudabi-ports'

# Location where resource files are stored.
DIR_RESOURCES = os.path.join(os.getcwd(), 'misc')

# Name of the GNU Make executable.
GNU_MAKE = 'gmake' if platform.system() == 'FreeBSD' else 'make'
