# test_rpy2.py

import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

def test_install_and_test_packages():
    utils = rpackages.importr('utils')

    # Select the first CRAN mirror
    utils.chooseCRANmirror(ind=1)

    # List of packages to install
    packnames = ('ggplot2', 'hexbin', 'ICS', 'dplyr')

    # Install the packages
    utils.install_packages(StrVector(packnames))

    # Load the installed packages and print their versions
    for package in packnames:
        pkg = rpackages.importr(package)
        print(f"{package} version: {pkg.__rname__}")

if __name__ == "__main__":
    test_install_and_test_packages()
