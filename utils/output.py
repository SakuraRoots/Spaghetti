#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from .colors import Colors


class Output:
    r = Colors().red(0)
    g = Colors().green(0)
    y = Colors().yellow(0)
    b = Colors().blue(0)
    w = Colors().white(0)
    e = Colors().end()

    @staticmethod
    def plus(msg):
        print(('{}[+]{} {}{}{}'.format(
            Output.g,
            Output.e,
            Output.w,
            msg,
            Output.e)
        ))

    @staticmethod
    def less(msg):
        print(('{}[-]{} {}{}{}'.format(
            Output.r,
            Output.e,
            Output.w,
            msg,
            Output.e)
        ))

    @staticmethod
    def test(msg):
        print(('{}[i]{} {}{}{}'.format(
            Output.b,
            Output.e,
            Output.w,
            msg,
            Output.e)
        ))

    @staticmethod
    def info(msg):
        print(('{}[i]{} {}{}{}'.format(
            Output.y,
            Output.e,
            Output.w,
            msg,
            Output.e)
        ))
