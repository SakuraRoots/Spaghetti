#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt


from . import asp
from . import java
from . import perl
from . import php
from . import python
from . import ruby


def lang(content, headers):
    return (
        asp.Asp().run(content, headers),
        java.Java().run(content, headers),
        php.Php().run(content, headers),
        perl.Perl().run(content, headers),
        python.Python().run(content, headers),
        ruby.Ruby().run(content, headers)
    )
