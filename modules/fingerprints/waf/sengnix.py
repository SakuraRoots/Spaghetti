#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re


class Senginx:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(r'SENGINX-ROBOT-MITIGATION', content, re.I) is not None
        if _:
            return "SEnginx (Neusoft Corporation)"
