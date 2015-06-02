import webapp2
import os

class VirtualProctor(webapp2.RequestHandler):
    def get(self):
        self.response.content_type = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        file = open(path)

        self.response.write(file.read())
        file.close()

app = webapp2.WSGIApplication([
    ('/', VirtualProctor),
], debug=True)
