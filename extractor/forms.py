#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import urllib.error
import urllib.parse
import urllib.request

import re

from request import urlcheck
from utils import text

from bs4 import BeautifulSoup


class Forms:
    def run(self, content, url):
        forms = []
        try:
            soup = BeautifulSoup(content)
            for match in soup.findAll('form'):
                if match not in forms:
                    forms.append(match)
            for form in forms:
                return urlcheck.UrlCheck().path(url, self.extractor(form))
        except Exception:
            pass

    @staticmethod
    def extractor(form):
        form = text.utf_8(form)
        method = []
        action = []
        names = []
        values = []
        try:
            method += re.findall(r'method=[\"](.+?)[\"]', form, re.I)
            action += re.findall(r'action=[\"](.+?)[\"]', form, re.I)
            names += re.findall(r'name=[\"](.+?)[\"]', form, re.I)
            values += re.findall(r'value=(\S*)', form, re.I)
        except Exception:
            pass
        params = []
        try:
            for i in range(len(names)):
                values[i] = values[i].split('"')[1]
                params.append(names[i])
                params.append(values[i])
        except:
            pass
        try:
            params = list(zip(*[iter(params)] * 2))
            data = urllib.parse.unquote(urllib.parse.urlencode(params))
            if not method:
                method = ['get']
            method = method[0]
            if method.upper() == "GET":
                return data
        except Exception:
            pass
