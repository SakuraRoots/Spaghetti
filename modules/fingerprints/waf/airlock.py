#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import re


class Airlock:
    @staticmethod
    def run(headers):
        _ = False
        for item in list(headers.items()):
            _ = re.search(r'^AL[_-]SESS[_-]S=\S*', item[1], re.I) is not None
            _ |= re.search(r'X-Airlock-Test', item[0], re.I) is not None
            if _:
                return "InfoGuard Airlock (Phion/Ergon)"

