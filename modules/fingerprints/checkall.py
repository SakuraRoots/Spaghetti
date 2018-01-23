#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from request import request
from utils import output
from .cms import cms
from .framework import framework
from .header.cookie import Cookie
from .header import headers
from .lang import lang
from .os import os
from .server import server
from .waf import waf


class Checkall:
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
        self.output.info('Starting fingerprints module...')
        try:
            resp = self.request.send(
                url=self.url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            ser = server.Server(self.url).run(resp.headers)
            self.output.plus('Server: %s' % ser)
            os_ = ([x for x in os.operating_system(resp.headers)])
            for x in os_:
                if x is not None:
                    self.output.plus('Operating system: %s' % x)
            firewall = ([x for x in waf.waf(resp.headers, resp.content)])
            for x in firewall:
                if x is not None:
                    self.output.plus('Firewall: %s' % x)
            cms_ = ([x for x in cms.cms(resp.content)])
            for x in cms_:
                if x is not None:
                    self.output.plus('Content Management System (CMS): %s' % x)
            lang_ = ([x for x in lang.lang(resp.content, resp.headers)])
            for x in lang_:
                if x is not None:
                    self.output.plus('Language: %s' % x)
            frame = ([x for x in framework.framework(resp.headers, resp.content)])
            for x in frame:
                if x is not None:
                    self.output.plus('Framework: %s' % x)
            headers.Headers().run(resp.headers)
            Cookie().run(resp.headers)
        except Exception:
            pass
