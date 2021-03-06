#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re


class Trafficshield:
    @staticmethod
    def run(headers):
        _ = False
        for item in list(headers.items()):
            _ = re.search(r'F5-TrafficShield', item[1], re.I) is not None
            _ |= re.search(r'ASINFO=', item[1], re.I) is not None
            if _:
                return "TrafficShield (F5 Networks)"

