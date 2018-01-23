#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from request import request
from request import urlcheck
from utils import output
from utils.data import read_data_file


class Bfile:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.ucheck = urlcheck.UrlCheck()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'Bfile',
            'fullname': 'Backup Files',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Backup Files'
        }
        self.output.test('Checking common backup files..')

        dbfiles = read_data_file('data/bfile.txt')

        dbfiles1 = read_data_file('data/cfile.txt')

        try:
            for b in dbfiles:
                for d in dbfiles1:
                    bdir = b.replace('[name]', d)
                    url = self.ucheck.path(self.url, bdir)
                    resp = self.request.send(
                        url=url,
                        method="GET",
                        payload=None,
                        headers=None,
                        cookies=self.cookie
                    )
                    if resp.status_code == 200:
                        if resp.url == url.replace(' ', '%20'):
                            self.output.plus('Found file "%s" Backup at %s' % (d, resp.url))
        except Exception as e:
            print(e)
