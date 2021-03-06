#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "libpgf"

def setup():
    shelltools.system("./autogen.sh")
    #pisitools.dosed("doc/Makefile.in", "^DOC_MODULE = .*$", "DOC_MODULE = ${PACKAGE}")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")
