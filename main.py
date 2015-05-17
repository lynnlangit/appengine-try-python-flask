import webapp2
import google.appengine.ext.webapp.template as template
import os
import cloudstorage as gcs
import logging
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        bucket_name = 'virtualproctor'
        bucket = '/' + bucket_name
        try:
            stats = gcs.listbucket(bucket, max_keys=10)
            names = [x.filename.replace('/virtualproctor/','') for x in stats]

        except Exception as e:
            logging.exception(e)
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        template_values = {'names': names }
        self.response.write(template.render(path,template_values))

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)