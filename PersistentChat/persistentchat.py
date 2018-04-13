from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail
import datetime

class ChatMessage(db.Model):
    user = db.StringProperty(required=True)
    timestamp = db.DateTimeProperty(auto_now_add=True)
    message = db.TextProperty(required=True)

    def __str__(self):
        return "%s (%s): %s" % (self.user, self.timestamp, self.message)


class ChatRoomPoster(webapp.RequestHandler):
    def post(self):
        chatter = self.request.get("name")
        msgtext = self.request.get("message")
        msg = ChatMessage(user=chatter, message=msgtext)
        msg.put()
        # Now that we've added the message to the chat, we'll redirect
        # to the root page,
        self.redirect('/')

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.out.write(
            """<html>
                <head>
                    <title>Georg's AppEngine Chat Room</title>
                </head>
                <body>
                    <h1>Welome to Georg's AppEngine Chat Room</h1>
                    <p> The current time is: %s</p>
                    <p> The service started at: %s</p>
            """ % (datetime.datetime.now(), serviceStartedTimeStamp))
        # Output the set of chat messages
        messages = db.GqlQuery("SELECT * From ChatMessage ORDER BY timestamp ASC")        
        for msg in messages:
            self.response.out.write("<p>%s</p>" % msg)
        self.response.out.write("""
            <form action="" method="post">
            <div><b>Name:</b>
            <textarea name="name" rows="1" cols="20"></textarea></div>
            <p><b>Message</b></p>
            <div><textarea name="message" rows="5" cols="60"></textarea></div>
            <div><input type="submit" value="Send ChatMessage"></input></div>
            </form>
            </body>
            </html>
        """)


class ChatRoomCountViewPage(webapp.RequestHandler):
    def post(self):
        chatter = self.request.get("name")
        msgtext = self.request.get("message")
        msg = ChatMessage(user=chatter, message=msgtext)
        msg.put()
        # Now that we've added the message to the chat, we'll redirect
        # to the root page,
        self.redirect('/')

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.out.write(
            """<html>
                <head>
                    <title>Georg's AppEngine Chat Room</title>
                </head>
                <body>
                    <h1>Welome to Georg's AppEngine Chat Room</h1>
                    <p> The current time is: %s</p>
                    <p> The service started at: %s</p>
            """ % (datetime.datetime.now(), serviceStartedTimeStamp))
        # Output the set of chat messages
        messages = db.GqlQuery("SELECT * From ChatMessage " +
                               "ORDER BY timestamp DESC LIMIT 20").fetch(20)
        messages.reverse()
        for msg in list(messages):
            self.response.out.write("<p>%s</p>" % msg)
        self.response.out.write("""
            <form action="" method="post">
            <div><b>Name:</b>
            <textarea name="name" rows="1" cols="20"></textarea></div>
            <p><b>Message</b></p>
            <div><textarea name="message" rows="5" cols="60"></textarea></div>
            <div><input type="submit" value="Send ChatMessage"></input></div>
            </form>
            </body>
            </html>
        """)


class ChatRoomTimeViewPage(webapp.RequestHandler):
    def post(self):
        chatter = self.request.get("name")
        msgtext = self.request.get("message")
        msg = ChatMessage(user=chatter, message=msgtext)
        msg.put()
        # Now that we've added the message to the chat, we'll redirect
        # to the root page,
        self.redirect('/')

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.out.write(
            """<html>
                <head>
                    <title>Georg's AppEngine Chat Room</title>
                </head>
                <body>
                    <h1>Welome to Georg's AppEngine Chat Room</h1>
                    <p> The current time is: %s</p>
                    <p> The service started at: %s</p>
            """ % (datetime.datetime.now(), serviceStartedTimeStamp))
        # Output the set of chat messages
        messages = ChatMessage.gql("WHERE timestamp > :fiveago ORDER BY timestamp", fiveago=datetime.datetime.now()-datetime.timedelta(minutes=5))
        for msg in messages:
            self.response.out.write("<p>%s</p>" % msg)
        self.response.out.write("""
            <form action="" method="post">
            <div><b>Name:</b>
            <textarea name="name" rows="1" cols="20"></textarea></div>
            <p><b>Message</b></p>
            <div><textarea name="message" rows="5" cols="60"></textarea></div>
            <div><input type="submit" value="Send ChatMessage"></input></div>
            </form>
            </body>
            </html>
        """)
            
chatapp = webapp.WSGIApplication([  ('/', ChatRoomPoster),
                                    ('/limited/count', ChatRoomCountViewPage),
                                    ('/limited/time', ChatRoomTimeViewPage)])

def main():    
    run_wsgi_app(chatapp)


if __name__ == "__main__":
    global serviceStartedTimeStamp 
    serviceStartedTimeStamp = datetime.datetime.now()
    main()