""" Game fix The Lord of the Rings Online
"""
#pylint: disable=C0103
#
from protonfixes import util

def main():
    """ Disable libglesv2 """

    ## gpu acelleration on wined3d https://bugs.winehq.org/show_bug.cgi?id=44985
    # Make the store work.
    util.winedll_override('libglesv2', 'd')
