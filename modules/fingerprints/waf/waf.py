#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from . import airlock
from . import anquanboa
from . import aws
from . import baidu
from . import barracuda
from . import bigip
from . import binarysec
from . import blockdos
from . import chinacache
from . import ciscoacexml
from . import cloudflare
from . import cloudfront
from . import dotdefender
from . import edgecast
from . import fortiweb
from . import hyperguard
from . import incapsula
from . import isaserver
from . import modsecurity
from . import netcontinuum
from . import paloalto
from . import profense
from . import radware
from . import requestvalidationmode
from . import safedog
from . import secureiis
from . import sengnix
from . import sitelock
from . import sonicwall
from . import sucuri
from . import trafficshield
from . import urlscan
from . import varnish
from . import wallarm
from . import webknight


def waf(headers, content):
    return (
        airlock.Airlock().run(headers),
        anquanboa.Anquanboa().run(headers),
        aws.Aws().run(headers),
        baidu.Baidu().run(headers),
        barracuda.Barracuda().run(headers),
        bigip.Bigip().run(headers),
        binarysec.Binarysec().run(headers),
        blockdos.Blockdos().run(headers),
        chinacache.Chinacache().run(headers),
        ciscoacexml.Ciscoacexml().run(headers),
        cloudflare.Cloudflare().run(headers),
        cloudfront.Cloudfront().run(headers),
        dotdefender.Dotdefender().run(headers),
        edgecast.Edgecast().run(headers),
        fortiweb.Fortiweb().run(headers),
        hyperguard.Hyperguard().run(headers),
        incapsula.Incapsula().run(headers),
        isaserver.Isaserver().run(content),
        modsecurity.Modsecurity().run(headers),
        netcontinuum.Netcontinuum().run(headers),
        paloalto.Paloalto().run(headers),
        profense.Profense().run(headers),
        radware.Radware().run(headers),
        requestvalidationmode.Requestvalidationmode().run(content),
        safedog.Safedog().run(headers),
        secureiis.Secureiis().run(content),
        sengnix.Senginx().run(content),
        sitelock.Sitelock().run(content),
        sonicwall.Sonicwall().run(content),
        sucuri.Sucuri().run(headers),
        trafficshield.Trafficshield().run(headers),
        urlscan.Urlscan().run(headers),
        varnish.Varnish().run(headers),
        wallarm.Wallarm().run(headers),
        webknight.Webknight().run(headers)
    )
