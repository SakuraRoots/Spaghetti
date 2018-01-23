#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from __future__ import (absolute_import, division, print_function, unicode_literals)

import argparse
import sys
import time

from request import random_agent
from request import UrlParser
from utils import Banner
from utils import Output
from utils import manager


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=Banner.epiloge(),
    )

    parser.add_argument('-u', "--url", help="Target URL (eg: http://example.com)", required=True)
    parser.add_argument(
        '-s', "--scan",
        type=int,
        choices=range(len(Banner.scan_types)),
        default=0,
        help="Scan Options (default=0). See below."
    )
    parser.add_argument("--agent", help="Use the specified user-agent", default=random_agent())
    parser.add_argument("--no-redirect", action="store_true", help="Don't follow redirects")
    parser.add_argument("--timeout", type=int, default=10, help="Connection timeout in secounds (default: 10)")
    parser.add_argument("--cookie", help="Set request cookie")
    parser.add_argument("--proxy", help="Set proxy, (host:port)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--version", action="store_true", help="Show version")

    ops = parser.parse_args()

    if ops.version:
        Banner.version()
        return

    # starting
    Banner.banner()

    target_url = target(ops.url)
    urls = []

    strftime(target_url)

    # Do fingerprint
    manager.fingerprints(
        ops.agent,
        ops.proxy,
        ops.no_redirect,
        ops.timeout,
        target_url,
        ops.cookie
    )
    if ops.scan == 6:
        return

    # crawler
    if ops.scan == 0 or ops.scan == 3:
        print()
        urls.extend(
            manager.crawling(
                ops.agent,
                ops.proxy,
                ops.no_redirect,
                ops.timeout,
                target_url,
                ops.cookie
            )
        )
        if not urls:
            urls.append(target_url)

    # scan options
    if ops.scan == 0:
        manager.bruteforce(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
        manager.disc(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
        manager.attacks(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            urls,
            ops.cookie
        )
        manager.others(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
        manager.vuln(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
    if ops.scan == 1:
        manager.bruteforce(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
    if ops.scan == 2:
        manager.disc(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
    if ops.scan == 3:
        manager.attacks(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            urls,
            ops.cookie
        )
    if ops.scan == 4:
        manager.others(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )
    if ops.scan == 5:
        manager.vuln(
            ops.agent,
            ops.proxy,
            ops.no_redirect,
            ops.timeout,
            target_url,
            ops.cookie
        )


def strftime(url):
    Output.plus('URL: %s' % url)
    Output.plus('Started: %s' % (str(time.strftime('%d/%m/%Y %H:%M:%S'))))
    print()


def target(url):
    u = UrlParser(url).host_path()
    if u is None:
        sys.exit(Output.less('Url not found, please try with target url!'))
    return str(u)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(Output.less('Keyboard Interrupt by User!!'))
