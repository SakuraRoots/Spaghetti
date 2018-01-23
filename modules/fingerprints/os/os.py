#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt


from . import bsd
from . import linux
from . import mac
from . import solaris
from . import unix
from . import windows


def operating_system(headers):
    return (
        bsd.Bsd().run(headers),
        windows.Windows().run(headers),
        linux.Linux().run(headers),
        solaris.Solaris().run(headers),
        unix.Unix().run(headers),
        mac.Mac().run(headers)
    )
