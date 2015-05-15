import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import logging

class PhotoUploadFormHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/photo')
        logging.info("Upload URL is: %s" % upload_url)
        self.response.out.write(upload_url)

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        self.response.status = "200 OK"

app = webapp2.WSGIApplication([('/upload', PhotoUploadFormHandler),
                              ('/photo', PhotoUploadHandler),
                              # ('/view_photo/([^/]+)?', ViewPhotoHandler),
                              ], debug=True)