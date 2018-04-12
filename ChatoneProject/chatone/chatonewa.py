# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:41:14 2018

@author: gbraun
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime

class WelcomePage(webapp.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.out.write(
            """<html>
                <head>
                    <title>Welcome to Georg's chat service</title>
                </head>
                <body>
                    <h1>Welome to Georg's chat service</h1>
                    <p> The current time is: %s</p>
                </body>
                <html>
            """ % (datetime.datetime.now()))

chatapp = webapp.WSGIApplication([('/',WelcomePage)])

def main():
    run_wsgi_app(chatapp)


if __name__ == "__main__":
    main()


