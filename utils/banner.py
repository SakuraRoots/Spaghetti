#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from .colors import Colors


class Banner:
    r = Colors().red(1)
    y = Colors().yellow(9)
    ny = Colors().yellow(0)
    nw = Colors().white(0)
    e = Colors().end()

    scan_types = [
        ("Full", "run all"),
        ("Bruteforce", "dirs, files, ..."),
        ("Disclosure", "ip, emails, ..."),
        ("Attacks", "sqli, lfi, ..."),
        ("Others", "webdav, ..."),
        ("Vulns", "shellshock, ..."),
        ("Fingerprint", "only fingerprint")
    ]

    @classmethod
    def banner(cls):
        print(cls.ny + "  _____             _       _   _   _ " + cls.e)
        print(cls.ny + " |   __|___ ___ ___| |_ ___| |_| |_|_|" + cls.e)
        print(cls.ny + " |__   | . | .'| . |   | -_|  _|  _| |" + cls.e)
        print(cls.ny + " |_____|  _|__,|_  |_|_|___|_| |_| |_|" + cls.e)
        print(cls.ny + "       |_|     |___|          " + cls.r + "v0.1.3\n" + cls.e)
        print(cls.nw + "~/#" + cls.e + " Spaghetti - Web Application Security Scanner" + cls.e)
        print(cls.nw + "~/#" + cls.e + " Codename - " + cls.y + "MR.R0B0T" + cls.e)
        print(cls.nw + "~/#" + cls.e + " Momo Outaadi (@M4ll0k)" + cls.e)
        print(cls.nw + "~/#" + cls.e + " https://github.com/m4ll0k/Spaghetti\n" + cls.e)

    @staticmethod
    def epiloge():
        ret = [
            "Scan Options:"
        ]

        ret.extend(
            "\t{}:\t{} ({})".format(idx, scan[0], scan[1]) for idx, scan in enumerate(Banner.scan_types)
        )

        ret.extend([
            "",
            "Examples:",
            "\t%(prog)s --url http://example.com",
            "\t%(prog)s --url http://example.com --scan [0-6]",
            "\t%(prog)s --url http://example.com --scan 1 --crawler",
        ])

        return "\n".join(ret)

    @classmethod
    def version(cls):
        cls.banner()
        print("~/# Spaghetti - Web Application Security Scanner (v0.1.3\n")
