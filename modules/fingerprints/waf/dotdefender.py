#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re


class Dotdefender:
    @staticmethod
    def run(headers):
        _ = False
        for item in list(headers.items()):
            _ = re.search(r'X-dotDefender-denied', item[0], re.I) is not None
            if _:
                return "dotDefender Web Application Firewall (Applicure Technologies)"

