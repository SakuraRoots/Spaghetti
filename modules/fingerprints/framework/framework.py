#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from . import cakephp
from . import cherrypy
from . import django
from . import flask
from . import fuelphp
from . import grails
from . import larvel
from . import mvc
from . import nette
from . import phalcon
from . import rails
from . import symfony
from . import yii
from . import zend


def framework(headers, content):
    return (
        cakephp.Cakephp().run(headers),
        cherrypy.Cherrypy().run(headers),
        django.Django().run(headers),
        flask.Flask().run(headers),
        fuelphp.Fuelphp().run(headers, content),
        grails.Grails().run(headers),
        larvel.Larvel().run(headers),
        mvc.Mvc().run(headers),
        nette.Nette().run(headers),
        phalcon.Phalcon().run(headers),
        rails.Rails().run(headers),
        symfony.Symfony().run(headers),
        yii.Yii().run(headers, content),
        zend.Zend().run(headers)
    )
