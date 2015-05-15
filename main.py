import webapp2
import google.appengine.ext.webapp.template as template
import os

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        template_values = { }
        self.response.write(template.render(path,template_values))

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)