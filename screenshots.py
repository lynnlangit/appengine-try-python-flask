import logging
import os
import cloudstorage as gcs
import webapp2
import json
import datetime
import time

my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)
gcs.set_default_retry_params(my_default_retry_params)


class Screenshots(webapp2.RequestHandler):

    def post(self):
        screenshot = self.request.POST["file"]

        write_retry_params = gcs.RetryParams(backoff_factor=1.1)
        gcs_file = gcs.open('/virtualproctor/' + screenshot.filename,
                            'w',
                            content_type='application/octet-stream',
                            retry_params=write_retry_params)
        gcs_file.write(screenshot.value)
        gcs_file.close()
        self.response.status_int = 204

    def get(self):
        bucket_name = 'virtualproctor'

        self.response.headers['Content-Type'] = 'application/json'

        bucket = '/' + bucket_name

        try:
            stats = gcs.listbucket(bucket)
            ten_minutes = datetime.timedelta(minutes = 10)
            ten_minutes_ago = datetime.datetime.now()-ten_minutes
            names = []
            for x in stats:
                create_time = datetime.datetime.fromtimestamp(x.st_ctime)
                if ten_minutes_ago < create_time:
                    name = x.filename.replace('/virtualproctor/', '').split('.')
                    image = {'classroom':name[0],'student':name[1],'created':x.st_ctime}
                    names.append(image)
            self.response.write(json.dumps(names))

        except Exception as e:
            logging.exception(e)
            self.response.write('{"error": "oops"}')

class Screenshot(webapp2.RequestHandler):
    def get(self,created,filename):
        self.response.content_type = 'image/png'
        gcs_file = gcs.open('/virtualproctor/' + filename)

        self.response.write(gcs_file.read())
        gcs_file.close()


app = webapp2.WSGIApplication([

    (r'/screenshots/(\d+.?\d*)/(.+)', Screenshot),
    (r'/screenshots', Screenshots)
],
                              debug=True)
