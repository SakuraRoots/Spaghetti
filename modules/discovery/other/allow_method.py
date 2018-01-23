#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import re

from request import request
from utils import output
from utils.data import read_data_file


class AllowMethod:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'AllowMethod',
            'fullname': 'Allow Method',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'HTTP Allow Method'
        }
        self.output.test('Checking http allow methods..')

        dbfiles = read_data_file('data/allowmethod.txt')

        try:
            for method in dbfiles:
                resp = self.request.send(url=self.url, method=method[0], payload=None, headers=None,
                                         cookies=self.cookie)
                if re.search(r'allow|public', str(list(resp.headers.keys())), re.I):
                    allow = resp.headers['allow']
                    if allow is None:
                        allow = resp.headers['public']
                    elif allow != '':
                        self.output.plus('HTTP Allow Method: %s' % allow)
                        break
        except Exception as e:
            pass
