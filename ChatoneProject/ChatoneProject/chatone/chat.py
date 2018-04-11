# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:08:30 2018

@author: gbraun
"""

import datetime

print 'Content-Type: text/html'
print ''
print '<html>'
print '<head>'
print '<title>Welcome to MarkCC\'s chat service</title>'
print '</head>'
print '<body>'
print '<h1>Welcome to MarkCC\'s chat service</h1>'
print ''
print 'Current timee is: %s' % (datetime.datetime.now())
print '</body>'
print '</html>'