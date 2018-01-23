#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt


class Colors:
    # red
    @staticmethod
    def red(number):
        return "\033[" + str(number) + ";31m"

    # green
    @staticmethod
    def green(number):
        return "\033[" + str(number) + ";32m"

    # yellow
    @staticmethod
    def yellow(number):
        return "\033[" + str(number) + ";33m"

    # blue
    @staticmethod
    def blue(number):
        return "\033[" + str(number) + ";34m"

    # purple
    @staticmethod
    def purple(number):
        return "\033[" + str(number) + ";35m"

    # cyan
    @staticmethod
    def cyan(number):
        return "\033[" + str(number) + ";36m"

    # white
    @staticmethod
    def white(number):
        return "\033[" + str(number) + ";38m"

    # end
    @staticmethod
    def end():
        return "\033[0m"
