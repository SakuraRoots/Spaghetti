#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from crawler import crawler
from modules.discovery.attack import attack
from modules.discovery.brute import brute
from modules.discovery.disclosure import disclosure
from modules.discovery.other import other
from modules.discovery.vulns import vulns
from modules.fingerprints import checkall


def fingerprints(agent, proxy, no_redirect, timeout, url, cookie):
    checkall.Checkall(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()


def crawling(agent, proxy, no_redirect, timeout, url, cookie):
    return crawler.Crawler(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).process()


def bruteforce(agent, proxy, no_redirect, timeout, url, cookie):
    brute.Brute(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()


def others(agent, proxy, no_redirect, timeout, url, cookie):
    other.Other(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()


def vuln(agent, proxy, no_redirect, timeout, url, cookie):
    vulns.Vulns(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()


def attacks(agent, proxy, no_redirect, timeout, url, cookie):
    attack.Attack(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()


def disc(agent, proxy, no_redirect, timeout, url, cookie):
    disclosure.Disclosure(
        agent=agent,
        proxy=proxy,
        redirect=not no_redirect,
        timeout=timeout,
        url=url,
        cookie=cookie
    ).run()
