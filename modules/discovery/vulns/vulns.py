#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from utils import output
from . import anonymous
from . import crime
from . import shellshock
from . import strutsshock


class Vulns:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.agent = agent
        self.proxy = proxy
        self.redirect = redirect
        self.timeout = timeout
        self.url = url
        self.cookie = cookie
        self.output = output.Output()

    def run(self):
        print("")
        self.output.info('Starting vulns module...')
        crime.Crime(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run(
        )
        anonymous.Anonymous(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run(
        )
        shellshock.Shellshock(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run(
        )
        strutsshock.StrutsShock(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run(
        )
