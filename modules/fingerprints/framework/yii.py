#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re


class Yii:
    @staticmethod
    def run(headers, content):
        _ = False
        for item in list(headers.items()):
            _ = re.search(r'_csrf=*', item[1], re.I) is not None
            _ |= re.search(r'Powered by <a href="http://www.yiiframework.com/" rel="external">Yii Framework</a>',
                           content) is not None
            if _:
                return "Yiiframework (PHP)"

