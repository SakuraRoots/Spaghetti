#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from __future__ import (absolute_import, division, print_function, unicode_literals)

from future.standard_library import install_aliases

install_aliases()

import urllib.parse


class UrlParser:
    def __init__(self, url):
        self.url = url
        self.scheme = urllib.parse.urlsplit(url).scheme
        self.netloc = urllib.parse.urlsplit(url).netloc
        self.path = urllib.parse.urlsplit(url).path
        self.query = urllib.parse.urlsplit(url).query

    def host(self):
        if self.netloc == "":
            return self.path.split('/')[0]
        else:
            return self.netloc

    def host_path(self):
        if self.netloc == "":
            return "http://" + self.path
        else:
            return self.scheme + "://" + self.netloc + self.path

    def complete(self):
        if self.netloc == "":
            return "http://" + self.path + "?" + self.query
        else:
            return self.scheme + "://" + self.netloc + self.path + "?" + self.query
