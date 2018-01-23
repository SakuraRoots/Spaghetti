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


class Backdoor:
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
            'name': 'Backdoor',
            'fullname': 'Backdoor',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Common Backdoors'
        }
        self.output.test('Checking common backdoors...')

        dbfiles = read_data_file('data/backdoor.txt')

        with open('data/backdoor.txt', 'r') as db:
            dbfiles.extend(line.strip() for line in db.readlines())

        try:
            for payload in dbfiles:
                url = self.ucheck.path(self.url, payload)
                resp = self.request.send(
                    url=url,
                    method="GET",
                    payload=None,
                    headers=None,
                    cookies=self.cookie
                )
                if resp.status_code == 200:
                    if resp.url == url.replace(' ', '%20'):
                        self.output.plus('Found Backdoor at %s' % resp.url)
        except Exception as e:
            print(e)
