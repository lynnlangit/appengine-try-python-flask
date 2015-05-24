import webapp2
import google.appengine.ext.webapp.template as template
import os
import cloudstorage as gcs
import logging


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        file = open(path)

        self.response.write(file.read())
        file.close()


app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
